import logging
from mongodb_driver import mongodb_driver_dev_type
from mongodb_driver import mongodb_driver
from logging.handlers import RotatingFileHandler
from datetime import datetime

if __name__ == "__main__":
    # Constants
    HOST = "localhost"
    PORT = 2717
    DB_NAME = "mongodb"
    LOG_FILE_PATH = "mongodb_driver_log.log"

    # Logger
    log_formatter = logging.Formatter("[%(levelname)s] %(asctime)s : %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    log_handler = RotatingFileHandler(filename=LOG_FILE_PATH)
    log_handler.setFormatter(log_formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(log_handler)

    # Database Object
    dbinverters = mongodb_driver(host=HOST, port=PORT, db_name=DB_NAME)

    # Insert registers
    # Iterate from  1st to April 26th
    for day in range(15, 20):
        # Define the data for the register
        data = {
            "id_device": 10140,
            "timestamp": f"2024-05-{day:02d} 08:00:00",
            "moisture": 50.45,
        }

        dbinverters.insert_record(device_type=mongodb_driver_dev_type.MOISTURE_SENSOR, record=data)

    lsdata: list = []
    for day in range(15, 20):
        # Define the data for the register
        data = {
            "id_device": 10141,
            "timestamp": f"2024-05-{day:02d} 08:00:00",
            "temp": 25.23,
        }

        lsdata.append(data)
    
    # Insert the register into the database
    dbinverters.insert_record(device_type=mongodb_driver_dev_type.TEMP_SENSOR, record=lsdata)