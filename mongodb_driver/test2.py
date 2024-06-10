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
    db = mongodb_driver(host=HOST, port=PORT, db_name=DB_NAME)

    records = db.search_unsent_records(device_type=mongodb_driver_dev_type.MOISTURE_SENSOR)
    for record in records:
        print(record)
        
    #print(db.set_record_as_sent(device_type=mongodb_driver_dev_type.MOISTURE_SENSOR, id_device=data["id_device"], timestamp=data["timestamp"]))

    records = db.search_all_records(device_type=mongodb_driver_dev_type.MOISTURE_SENSOR)
    for record in records:
        print(record)

    data = {
            "id_device": 10140,
            "timestamp": f"2024-05-15 08:00:00",
            "moisture": 50.45,
        }
    print(db.exist_record(device_type=mongodb_driver_dev_type.MOISTURE_SENSOR, record=data))