import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename

    error_msg= 'error occured in script [{}] line number [{}] error message [{}]'.format(file_name,exc_tb.tb_lineno,str(error))
    return error_msg

class CustomException(Exception):
    def __init__(self,error,error_detail:sys):
        super().__init__(error)
        self.error_message=error_message_detail(error,error_detail)
    def __str__(self):
        return self.error_message