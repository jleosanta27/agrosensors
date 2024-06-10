import logging
from pymongo import MongoClient
from pymongo.cursor import Cursor
from datetime import datetime, timedelta
from enum import Enum
from typing import Union

# Constants
BD_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class mongodb_driver_dev_type(Enum):
    MOISTURE_SENSOR = "moisture_sensor"
    TEMP_SENSOR = "temp_sensor"
    NODE_DEV = "node_dev"

class mongodb_driver:
    def __init__(self, host: str, port: int, db_name: str, timeout: int = 5, logger: logging = None) -> None:
        self.__client = MongoClient(host, port)
        self.__db = self.__client[db_name]
        __timeout: int = timeout

    def insert_record(self, device_type: mongodb_driver_dev_type, record: Union[dict, list[dict]]) -> bool:
        collection = self.__db[device_type.value]
        if type(record) == dict:
            collection.insert_one(record)
        if type(record) == list:
            collection.insert_many(record)

    def exist_record(self, device_type: mongodb_driver_dev_type, record: dict) -> bool:
        collection = self.__db[device_type.value]
        query = {'timestamp': record['timestamp'], 'id_device': record['id_device']}
        
        return collection.find_one(query) is not None
    
    def set_record_as_sent(self, device_type: mongodb_driver_dev_type, id_device: int, timestamp: str) -> bool:
        val_return: bool = False

        collection = self.__db[device_type.value]
        query = {'id_device': id_device, 'timestamp': timestamp}
        update = {'$set': {'sent': True}}
        
        if collection.update_one(query, update):
            val_return = True
        
        return val_return

    def search_unsent_records(self, device_type: mongodb_driver_dev_type) -> Cursor:
        collection = self.__db[device_type.value]
        query = {'$or': [{'sent': False}, {'sent': {'$exists': False}}]}
        
        return collection.find(query)
    
    def search_all_records(self, device_type: mongodb_driver_dev_type) -> Cursor:
        collection = self.__db[device_type.value]
        return collection.find()

    #def delete_old_records(self, device_type, days):
    #    collection = self.db[device_type]
    #    query = {'timestamp': {'$lt': datetime.utcnow() - timedelta(days=days)}}
    #    collection.delete_many(query)