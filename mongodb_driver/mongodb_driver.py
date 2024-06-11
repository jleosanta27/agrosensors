import logging

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.database import Database
from bson import ObjectId

from datetime import datetime
from datetime import timedelta

from enum import Enum
from typing import Union
from dataclasses import dataclass
from dataclasses import field

from enumerations import records_enum
from enumerations import recordsxdev_enum
from enumerations import sensors_enum
from enumerations import collections_enum
from enumerations import device_type_enum
from enumerations import node_enum

# Constants
BD_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

@dataclass
class mongodb_driver:
    # Required Parameters
    host: str = field(init=True)
    port: int = field(init=True)
    db_name: str = field(init=True)
    timeout: int = field(init=True)
    logger: logging.Logger = field(default=None, init=True)

    # Non-required Parameters
    client: MongoClient = field(default=None, init=False)
    db: Database = field(default=None, init=False)
    
    def __post_init__(self) -> str:
        try:
            self.client = MongoClient(host=self.host, port=self.port, connectTimeoutMS=self.timeout)
            self.db = self.client[self.db_name]
            if self.logger:
                self.logger.info("MongoDB connection established.")
        except Exception as e:
            self.logger.error(f"Error establishing connection: {e}")

    
    def create_id_record(self) -> str:
        val_return: str = str()
        
        try:
            collection = self.db[collections_enum.RECORDS]
            record = {records_enum.TIMESTAMP: datetime.now().strftime(BD_DATE_FORMAT)}
            val_return = collection.insert_one(record).inserted_id
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error creating id_record: {e}")

        return val_return

    def insert_record(self, record: dict) -> bool:
        val_return: bool = False        

        try:
            # save data in recordsxdev collection
            valid_keys = {val for val in recordsxdev_enum}
            filtered_data = {key: val for key, val in record.items() if key in valid_keys}
            filtered_data[recordsxdev_enum.SENT] = False
            collection = self.db[collections_enum.RECORDSXDEV]
            collection.insert_one(filtered_data)

            # save data in sensor or node collection
            match record[recordsxdev_enum.DEVICE_TYPE]:
                case device_type_enum.SENSOR:
                    valid_keys = {val for val in sensors_enum}
                    filtered_data = {key: val for key, val in record.items() if key in valid_keys}
                    collection = self.db[collections_enum.SENSOR]
                    if collection.insert_one(filtered_data): val_return=True

                case device_type_enum.NODE:
                    valid_keys = {val for val in node_enum}
                    filtered_data = {key: val for key, val in record.items() if key in valid_keys}
                    collection = self.db[collections_enum.NODE]
                    if collection.insert_one(filtered_data): val_return=True

            if val_return and self.logger:
                self.logger.debug(f"Record inserted succesfully: {record}")
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error inserting {record}: {e}")

        return val_return






    def exist_record(self, collection_type: collections_enum, record: dict) -> bool:
        collection = self.__db[collection_type]
        query = {'timestamp': record['timestamp'], 'id_device': record['id_device']}
        
        return collection.find_one(query) is not None 

    def set_record_as_sent(self, device_type: collections_enum, id_device: int, timestamp: str) -> bool:
        val_return: bool = False

        collection = self.__db[device_type.value]
        query = {'id_device': id_device, 'timestamp': timestamp}
        update = {'$set': {'sent': True}}
        
        if collection.update_one(query, update):
            val_return = True
        
        return val_return

    def search_unsent_records(self, collection_type: collections_enum) -> Cursor:
        collection = self.db[collection_type]
        query = {'$or': [{'sent': False}, {'sent': {'$exists': False}}]}
        
        return collection.find(query)


'''
class mongodb_driver:
    def __init__(self, host: str, port: int, db_name: str, timeout: int = 5, logger: logging = None) -> None:
        self.__client = MongoClient(host, port)
        self.__db = self.__client[db_name]
        __timeout: int = timeout

    def insert_record(self, device_type: collection_type, record: Union[dict, list[dict]]) -> bool:
        collection = self.__db[device_type.value]
        if type(record) == dict:
            collection.insert_one(record)
        if type(record) == list:
            collection.insert_many(record)

    def exist_record(self, device_type: collection_type, record: dict) -> bool:
        collection = self.__db[device_type.value]
        query = {'timestamp': record['timestamp'], 'id_device': record['id_device']}
        
        return collection.find_one(query) is not None
    
    def set_record_as_sent(self, device_type: collection_type, id_device: int, timestamp: str) -> bool:
        val_return: bool = False

        collection = self.__db[device_type.value]
        query = {'id_device': id_device, 'timestamp': timestamp}
        update = {'$set': {'sent': True}}
        
        if collection.update_one(query, update):
            val_return = True
        
        return val_return

    def search_unsent_records(self, device_type: collection_type) -> Cursor:
        collection = self.__db[device_type.value]
        query = {'$or': [{'sent': False}, {'sent': {'$exists': False}}]}
        
        return collection.find(query)
    
    def search_all_records(self, device_type: collection_type) -> Cursor:
        collection = self.__db[device_type.value]
        return collection.find()

    #def delete_old_records(self, device_type, days):
    #    collection = self.db[device_type]
    #    query = {'timestamp': {'$lt': datetime.utcnow() - timedelta(days=days)}}
    #    collection.delete_many(query)
'''