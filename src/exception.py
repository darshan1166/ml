import sys
import logger
import logging

def custom_error(error_message,error_detail:sys):
    _,_,error_info= error_detail.exc_info()
    filename = error_info.tb_frame.f_code.co_filename
    line_number = error_info.tb_lineno
    return "error occured in file - {0}, line number - {1}, error - {2}".format(filename,line_number,error_message)

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = custom_error(error_message,error_detail)
        logging.info(self.error_message)
    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    try :
        1/0
    except Exception as e:
        raise CustomException(e,sys)
