from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    '''Abstract base class defining the common processing interface'''
    @abstractmethod
    def validate(self, data: Any) -> bool:
        '''Validate if data is appropriate'''
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        '''Process the data and return result string'''
        pass

    def format_output(self, result: str) -> str:
        '''Format the output string'''
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        '''Validate if data is appropriate for this processor'''
        try:
            [int(num) for num in data]
            return True
        except ValueError:
            return False

    def process(self, data: Any) -> str:
        '''Process the data and return result string'''
        num = len(data)
        n_sum = sum(d for d in data)
        n_avg = n_sum / num
        return f"Processed {num} numeric values, sum={n_sum}, avg={n_avg:.1f}"

    def format_output(self, result: str) -> str:
        '''Format the output string'''
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        '''Validate if data is appropriate for this processor'''

    def process(self, data: Any) -> str:
        '''Process the data and return result string'''
        chars = len(data)
        word_count = len(data.split())
        return f"Processed text: {chars} characters, {word_count} words"

    def format_output(self, result: str) -> str:
        '''Format the output string'''
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        '''Validate if data is appropriate for this processor'''

    def process(self, data: Any) -> str:
        '''Process the data and return result string'''

    def format_output(self, result: str) -> str:
        '''Format the output string'''
        return super().format_output(result)


if __name__ == "__main__":
    num_data = [1, 2, 3, 4, 5]
    str_data = "Hello Nexus World"
    logstr_data = "ERROR: Connection timeout"
    process_data = ([1, 2, 3], "Hello World!", "INFO: System ready")

    numeric_data = NumericProcessor()
    text_data = TextProcessor()
    log_data = LogProcessor()

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    print(f"Processing data: {num_data}")
    if numeric_data.validate(num_data):
        print("Validation: Numeric data verified")
        numeric_result = numeric_data.process(num_data)
        print(f"{numeric_data.format_output(numeric_result)}")
    else:
        print("Validation: ERROR (data non-numeric)")

    print("\nInitializing Text Processor...")
    print(f"Processing data: {str_data}")
    if text_data.validate(str_data):
        print("Validation: Text data verified")
        text_result = text_data.process(str_data)
        print(f"{text_data.format_output(text_result)}")
    else:
        print("Validation: ERROR (data non-textual)")

    print("\nInitializing Log Processor...")
    print(f"Processing data: {logstr_data}")
    if log_data.validate(logstr_data):
        print("Validation: Log entry verified")
        log_result = log_data.process(logstr_data)
        print(f"{log_data.format_output(log_result)}")
    else:
        print("Validation: ERROR (log entry not found)")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    i = 0
    for pd in process_data:
        print(f"Result {i + 1}: {numeric_data.process(pd)}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
