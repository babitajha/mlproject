import logging
import os
from datetime import datetime

#Defining the file name formatting in this how data will get save
Log_file = f"{datetime.now().strftime('%m-%d-%Y.%H-%M-%S')}.log"

# Mentioning the path as per each directiory the log file will create and save
logs_path= os.path.join(os.getcwd(),"logs",Log_file)

#after creating the log file it will append the logs if file is already created in that path
os.makedirs(logs_path,exist_ok=True)

Logs_file_path = os.path.join(logs_path,Log_file)

#doing the baseconfig for the logging need to create in flie
logging.basicConfig(
    filename=Logs_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

#testing
# if __name__ == "__main__" :
#     logging.info("logging has started")
