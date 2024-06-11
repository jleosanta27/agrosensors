import logging
import time
from mongodb_driver import mongodb_driver
from logging.handlers import RotatingFileHandler
from datetime import datetime

from enumerations import records_enum
from enumerations import recordsxdev_enum
from enumerations import sensors_enum
from enumerations import device_type_enum
from enumerations import data_enum


if __name__ == "__main__":
    # Constants
    HOST = "localhost"
    PORT = 2717
    DB_NAME = "mongodb"
    LOG_FILE_PATH = "log.log"

    # Logger
    log_formatter = logging.Formatter("[%(levelname)s] %(asctime)s : %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    log_handler = RotatingFileHandler(filename=LOG_FILE_PATH)
    log_handler.setFormatter(log_formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(log_handler)

    # Database Object
    db = mongodb_driver(host=HOST, port=PORT, db_name=DB_NAME, timeout=5000, logger=logger)

    # create id_record
    id = db.create_id_record()
    print(f"ID_RECORD created: {id}")
    time.sleep(2)

    # insert record with the id_record created previously
    data={data_enum.ID_RECORD: id,
          data_enum.ID_DEVICE: 24343434,
          data_enum.MOISTURE: 55.4,
          data_enum.TEMP: 23.2,
          data_enum.DEVICE_TYPE: device_type_enum.SENSOR}
    
    data={data_enum.ID_RECORD: id,
          data_enum.ID_DEVICE: 249934,
          data_enum.SOC: 98,
          data_enum.DEVICE_TYPE: device_type_enum.NODE,}

    
    db.insert_record(record=data)