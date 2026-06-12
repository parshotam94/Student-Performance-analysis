
import sys

class CustomException(Exception):
    def __init__(self, error):
        _, _, trace = sys.exc_info()
        file_name = trace.tb_frame.f_code.co_filename if trace else 'Unknown'
        line_number = trace.tb_lineno if trace else 'Unknown'
        self.message = f'Error in {file_name} line {line_number}: {error}'
        super().__init__(self.message)

    def __str__(self):
        return self.message
    
