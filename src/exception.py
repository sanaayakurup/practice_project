import sys, os
import logging
import logger 

def error_message_details(error, error_detail:sys):
   _,_,exec_tb=error_detail.exc_info() #where has the exception occured
   file_name=exec_tb.tb_frame.f_code.co_filename
   error_message=f'Error occurerd in script name {file_name} in line no {exec_tb.tb_lineno} with error {str(error)}'
   return error_message


class CustomException(Exception): #inheriting the exception class 
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #passing the error message into the custom function written above 
        self.error_message=error_message_details(error_message,error_detail=error_detail)   

    def __str__(self):
        return self.error_message

