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
    def process_batch(self, data_batch: List[Any]) -> str:
        '''Process a batch of data'''
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        '''Filter data based on criteria'''
        # criteria is High-priority
        pass


class SensorStream(DataStream):
    ''''''
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''Return stream statistics'''
        stats = super().get_stats()
        stats.update({"Type": self.type})
        return stats

    def process_batch(self, data_batch: List[Any]) -> str:
        '''Process a batch of data'''


class TransactionStream(DataStream):
    ''''''
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''Return stream statistics'''
        stats = super().get_stats()
        stats.update({"Type": self.type})
        return stats

    def process_batch(self, data_batch: List[Any]) -> str:
        '''Process a batch of data'''


class EventStream(DataStream):
    ''''''
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        '''Return stream statistics'''
        stats = super().get_stats()
        stats.update({"Type": self.type})
        return stats

    def process_batch(self, data_batch: List[Any]) -> str:
        '''Process a batch of data'''


if __name__ == "__main__":
    ids = ("SENSOR_001", "TRANS_001", "EVENT_001")

    sensor = SensorStream(ids[0])
    trans = TransactionStream(ids[1])
    event = EventStream(ids[2])

    s_batch = [{'temp': 22.5}, {'humidity': 65}, {'pressure': 1013}]
    t_batch = [{'buy': 100}, {'sell': 150}, {'buy': 75}]
    e_batch = ["login", "error", "logout"]

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    print(f"{sensor.get_stats()}")
    print(f"Processing sensor batch: {sensor.process_batch(ids[0])}")
    # print(f"Sensor analysis: {sensor}")
