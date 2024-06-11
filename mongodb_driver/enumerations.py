from enum import Enum
from enum import auto

class data_enum(str, Enum):
    ID_RECORD       = "_id",
    ID_DEVICE       = "id_dev",
    DEVICE_TYPE     = "dev_type",
    TIMESTAMP       = "ts",
    SENT            = "sent",

    # NODE
    SOC             = "soc",
    CPU_TEMP        = "cpu_temp"

    # SENSOR
    MOISTURE        = "moisture",
    TEMP            = "temp"

    def __str__(self) -> str:
        return self.value

class records_enum(str, Enum):
    ID_RECORD       = data_enum.ID_RECORD,
    TIMESTAMP       = data_enum.TIMESTAMP

    def __str__(self) -> str:
        return self.value

class recordsxdev_enum(str, Enum):
    ID_RECORD       = data_enum.ID_RECORD,
    ID_DEVICE       = data_enum.ID_DEVICE,
    DEVICE_TYPE     = data_enum.DEVICE_TYPE,
    SENT            = data_enum.SENT

    def __str__(self) -> str:
        return self.value

class node_enum(str, Enum):
    ID_RECORD       = data_enum.ID_RECORD,
    ID_DEVICE       = data_enum.ID_DEVICE,
    SOC             = data_enum.SOC,
    CPU_TEMP        = data_enum.CPU_TEMP

    def __str__(self) -> str:
        return self.value

class sensors_enum(str, Enum):
    ID_RECORD       = data_enum.ID_RECORD,
    ID_DEVICE       = data_enum.ID_DEVICE,
    MOISTURE        = data_enum.MOISTURE,
    TEMP            = data_enum.TEMP

    def __str__(self) -> str:
        return self.value
    
class device_type_enum(int, Enum):
    NODE            = auto()
    SENSOR          = auto()

    def __str__(self) -> str:
        return self.value

class collections_enum(str, Enum):
    RECORDS         = "records",
    RECORDSXDEV     = "recordsxdev"
    SENSOR          = "sensors"
    NODE            = "nodes"

    def __str__(self):
        return self.value