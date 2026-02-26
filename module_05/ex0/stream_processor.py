from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    '''Abstract base class defining the common processing interface'''
    @abstractmethod
    def process(self, data: Any) -> str:
        '''Process the data and return result string'''
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        '''Validate if data is appropriate'''
        pass

    def format_output(self, result: str) -> str:
        '''Format the output string'''
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        '''Process the data and return result string'''
        return (f"Processing data: {data}")

    def validate(self, data: Any) -> bool:
        '''Validate if data is appropriate for this processor'''
        try:
            [int(num) for num in data]
            print("Validation: Numeric data verified")
            return True
        except ValueError:
            print("Validation: ERROR (data non-numeric)")
            return False

    def format_output(self, result: str) -> str:
        '''Format the output string'''


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        '''Process the data and return result string'''

    def validate(self, data: Any) -> bool:
        '''Validate if data is appropriate for this processor'''

    def format_output(self, result: str) -> str:
        '''Format the output string'''


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        '''Process the data and return result string'''

    def validate(self, data: Any) -> bool:
        '''Validate if data is appropriate for this processor'''

    def format_output(self, result: str) -> str:
        '''Format the output string'''


if __name__ == "__main__":
    num_data = [1, 2, 3, 4, 5]
    str_data = "Hello Nexus World"
    logstr_data = "ERROR: Connection timeout"
    process_data = ([1, 2, 3], "Hello World!", "INFO: System ready")

    numeric_data = NumericProcessor()
    text_data = TextProcessor()
    log_data = LogProcessor()

    i = 0

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    print(f"Processing data: {num_data}")
    numeric_data.validate(num_data)
    print(f"{numeric_data.format_output(num_data)}")

    print("\nInitializing Text Processor...")
    print(f"Processing data: {str_data}")
    text_data.validate(str_data)
    print(f"{text_data.format_output(text_data)}")

    print("\nInitializing Log Processor...")
    print(f"Processing data: {logstr_data}")
    log_data.validate(logstr_data)
    print(f"{log_data.format_output(logstr_data)}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    for pd in process_data:
        print(f"Result {i + 1}: {numeric_data.process(pd)}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
