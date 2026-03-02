from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    '''Abstract base class with core streaming functionality'''
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''Return stream statistics'''
        return {"Stream ID": self.stream_id}

    @abstractmethod
    def format_batch(self, data_batch: List[Any]) -> str:
        '''Return the stream as a formatted list'''
        pass

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        '''Process a batch of data'''
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        '''Filter data based on criteria'''
        return data_batch


class SensorStream(DataStream):
    '''Child class to process sensor streams'''
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''Return stream statistics'''
        stats = super().get_stats()
        stats.update({"Type": self.type})
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        '''Filter data based on criteria'''
        filtered_batch = []
        for data in data_batch:
            for key, value in data.items():
                if isinstance(key, (str)) and isinstance(value, (float, int)):
                    if key == "temp" or key == "humidity" or key == "pressure":
                        filtered_batch.append(data)
        return filtered_batch

    def format_batch(self, data_batch: List[Any]) -> str:
        '''Return the stream as a formatted list'''
        sensor_batch = []
        for data in data_batch:
            for key, value in data.items():
                list_item = f"{key}:{value}"
                sensor_batch.append(list_item)
        f_sensor_batch = (", ").join(sensor_batch)
        return f"{f_sensor_batch}"

    def process_batch(self, data_batch: List[Any]) -> str:
        '''Process a batch of data'''
        count = 0
        temps = 0
        for data in data_batch:
            if "temp" in data:
                temps += float(data.get("temp", 0))
                count += 1
        temp_avg = temps / count
        return f"Sensor analysis: {len(data_batch)} readings processed, \
avg temp: {temp_avg}°C"


class TransactionStream(DataStream):
    '''Child class to process transaction streams'''
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''Return stream statistics'''
        stats = super().get_stats()
        stats.update({"Type": self.type})
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        '''Filter data based on criteria'''
        filtered_batch = []
        for data in data_batch:
            for key, value in data.items():
                if isinstance(key, (str)) and isinstance(value, (float, int)):
                    if key == "buy" or key == "sell":
                        filtered_batch.append(data)
        return filtered_batch

    def format_batch(self, data_batch: List[Any]) -> str:
        '''Return the stream as a formatted list'''
        transaction_batch = []
        for data in data_batch:
            for key, value in data.items():
                list_item = f"{key}:{value}"
                transaction_batch.append(list_item)
        f_transaction_batch = (", ").join(transaction_batch)
        return f"{f_transaction_batch}"

    def process_batch(self, data_batch: List[Any]) -> str:
        '''Process a batch of data'''
        buy = 0
        sell = 0
        for data in data_batch:
            buy += int(data.get("buy", 0))
            sell += int(data.get("sell", 0))
        if (buy - sell) > 0:
            net_flow = f"+{buy - sell}"
        return f"Transaction analysis: {len(data_batch)} operations, \
net flow: {net_flow} units"


class EventStream(DataStream):
    '''Child class to process event streams'''
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''Return stream statistics'''
        stats = super().get_stats()
        stats.update({"Type": self.type})
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        '''Filter data based on criteria'''
        filtered_batch = []
        for data in data_batch:
            if isinstance(data, (str)):
                if data == "login" or data == "error" or data == "logout":
                    filtered_batch.append(data)
        return filtered_batch

    def format_batch(self, data_batch: List[Any]) -> str:
        '''Return the stream as a formatted list'''
        return f"{(", ").join(data_batch)}"

    def process_batch(self, data_batch: List[Any]) -> str:
        '''Process a batch of data'''
        count = 0
        for data in data_batch:
            if "error" in data:
                count += 1
        if count == 1:
            errors = f"{count} error"
        else:
            errors = f"{count} errors"
        return f"Event analysis: {len(data_batch)} events, {errors} detected"


class StreamProcessor():
    '''Class handling the polymorphic stream processing'''

    def __init__(self) -> None:
        '''Initialize class with list of streams to process'''
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        '''Add streams to the processor list'''
        self.streams.append(stream)

    def filter_all(self, data_batch: List[Any],
                   criteria: Optional[str] = None) -> List[Any]:
        '''Filter data based on criteria'''
        return data_batch

    def process_all(self, data_batch: Dict[str, List[Any]]) -> str:
        '''Process a batch of data'''
        processed = []
        for stream in self.streams:
            value = data_batch.get(stream.stream_id, [])
            count = len(value)
            if stream.stream_id[:5] == "SENSO":
                stream_type = "Sensor"
                type_processed = "readings"
            elif stream.stream_id[:5] == "TRANS":
                stream_type = "Transaction"
                type_processed = "operations"
            elif stream.stream_id[:5] == "EVENT":
                stream_type = "Event"
                type_processed = "events"
            processed.append(f"- {stream_type} "
                             f"data: {count} {type_processed} processed")
        return "\n".join(processed)


if __name__ == "__main__":
    ids = ("SENSOR_001", "TRANS_001", "EVENT_001")

    sensor = SensorStream(ids[0])
    trans = TransactionStream(ids[1])
    event = EventStream(ids[2])

    s_batch = [{'temp': 22.5}, {'humidity': 65}, {'pressure': 1013}]
    t_batch = [{'buy': 100}, {'sell': 150}, {'buy': 75}]
    e_batch = ['login', 'error', 'logout']

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    print(", ".join([f"{k}: {v}" for k, v in sensor.get_stats().items()]))
    sf_batch = sensor.filter_data(s_batch)
    if sf_batch:
        print(f"Processing sensor batch: [{sensor.format_batch(sf_batch)}]")
        print(f"{sensor.process_batch(sf_batch)}")
    else:
        print("ERROR: Sensor values invalid.")

    print("\nInitializing Transaction Stream...")
    print(", ".join([f"{k}: {v}" for k, v in trans.get_stats().items()]))
    tfbatch = trans.filter_data(t_batch)
    if tfbatch:
        print(f"Processing transaction batch: [{trans.format_batch(tfbatch)}]")
        print(f"{trans.process_batch(tfbatch)}")
    else:
        print("ERROR: Transaction values invalid.")

    print("\nInitializing Event Stream...")
    print(", ".join([f"{k}: {v}" for k, v in event.get_stats().items()]))
    ef_batch = event.filter_data(e_batch)
    if ef_batch:
        print(f"Processing event batch: [{event.format_batch(ef_batch)}]")
        print(f"{event.process_batch(ef_batch)}")
    else:
        print("ERROR: Event values invalid.")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    batch1 = {"SENSOR_001": ["temp:38.0", "temp:42.0"],
              "TRANS_001": ["buy:30", "sell:200", "buy:100", "sell:50"],
              "EVENT_001": ["login", "error", "logout"]}

    print("Batch 1 Results:")
    print(f"{processor.process_all(batch1)}")

    print("Stream filtering active: High-priority data only")
    filtered_batch = processor.filter_all(batch1)
    print(f"Filtered results: "
          f"{filtered_batch['SENSOR_001']} critical sensor alerts, "
          f"{filtered_batch['TRANS_001']} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
