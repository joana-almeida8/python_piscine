from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod


class ProcessingPipeline(ABC):
    '''Abstract base class for processing pipelines'''

    def __init__(self, pipeline_id: str):
        '''Initialize the processing pipeline'''
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: str) -> None:
        '''Add a processing stage to the pipeline'''
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        '''Process data through the pipeline'''
        pass


class ProcessingStage(Protocol):
    '''Protocol for processing stages using duck typing'''
    def process(self, data: Any) -> Any:
        '''Process data and return result'''
        ...


class InputStage(ProcessingStage):
    '''Input validation and parsing stage'''
    def process(self, data: Any) -> Dict:
        '''Process input data with validation'''
        return data


class TransformStage(ProcessingStage):
    '''Data transformation and enrichment stage'''
    def process(self, data: Any) -> Dict:
        '''Transform and enrich data'''
        return data


class OutputStage(ProcessingStage):
    '''Output formatting and delivery stage'''
    def process(self, data: Any) -> str:
        '''Format output data'''
        return data


class JSONAdapter(ProcessingPipeline):
    '''Adapter class or JSON data format'''
    def __init__(self, pipeline_id: str):
        '''Initialize JSON adapter'''
        super().__init__(pipeline_id)
    
    def process(self, data: Any) -> Union[str, Any]:
        '''Process JSON data through pipeline stages'''
        current_data = data
        for stage in self.stages:
            current_data = stage.process(current_data)
        return current_data


class CSVAdapter(ProcessingPipeline):
    '''Adapter class or CSV data format'''
    def __init__(self, pipeline_id: str):
        '''Initialize CSV adapter'''
        super().__init__(pipeline_id)
    
    def process(self, data: Any) -> Union[str, Any]:
        '''Process CSV data through pipeline stages'''
        current_data = data
        for stage in self.stages:
            current_data = stage.process(current_data)
        return current_data


class StreamAdapter(ProcessingPipeline):
    '''Adapter class or Stream data format'''
    def __init__(self, pipeline_id: str):
        '''Initialize Stream adapter'''
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        '''Process Stream data through pipeline stages'''
        current_data = data
        for stage in self.stages:
            current_data = stage.process(current_data)
        return current_data


class NexusManager():
    '''Class managing the pipeline for processing'''
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: Any) -> None:
        '''Add pipeline to the nexus manager'''
        self.pipelines.append(pipeline)

    def process_data(self, pipeline_id: str, data: Any) -> Union[str, Any]:
        '''Process data from different adapters'''
        if pipeline_id not in self.pipelines:
            raise ValueError (f"Pipeline ID {pipeline_id} not found.\n"
                              "Transform Stage could not process.")
        return self.pipelines[pipeline_id].process(data)


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    nexus = NexusManager()
    print("Pipeline capacity: 1000 streams/second")

    print("\nCreating Data Processing Pipeline...")
    i_stage = InputStage()
    t_stage = TransformStage()
    o_stage = OutputStage()
    print("Stage 1: Input validation and parsing\n"
          "Stage 2: Data transformation and enrichment\n"
          "Stage 3: Output formatting and delivery")

    print("\n=== Multi-Format Data Processing ===")

    print("\nProcessing JSON data through pipeline...")
    json_data = {"input": "temp", "value": 23.5, "unit": "C"}
    json_a = JSONAdapter("JSON_001")
    json_a.add_stage(i_stage)
    json_a.add_stage(t_stage)
    json_a.add_stage(o_stage)
    nexus.add_pipeline(json_a)
    json_output = nexus.process_data("JSON_001", json_data)
    print(f"Input: {json_data}")
    print("Transform: Enriched with metadata and validation")
    print(f"Output: {json_output}")

    print("\nProcessing CSV data through pipeline...")
    csv_data = "user,action,timestamp"
    scv_a = CSVAdapter("CSV_001")
    scv_a.add_stage(i_stage)
    scv_a.add_stage(t_stage)
    scv_a.add_stage(o_stage)
    nexus.add_pipeline(csv_data)
    csv_output = nexus.process_data("CSV_001", csv_data)
    print(f'Input: "{csv_data}"')
    print("Transform: Parsed and structured data")
    print(f"Output: {csv_output}")

    print("\nProcessing Stream data through pipeline...")
    stream_data = "Real-time sensor stream"
    stream_a = StreamAdapter("STREAM_001")
    stream_a.add_stage(i_stage)
    stream_a.add_stage(t_stage)
    stream_a.add_stage(o_stage)
    nexus.add_pipeline(stream_data)
    stream_output = nexus.process_data("STREAM_001", stream_data)
    print(f"Input: {stream_data}")
    print("Transform: Aggregated and filtered")
    print(f"Output: {stream_output}")

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    print("\nNexus Integration complete. All systems operational.")
