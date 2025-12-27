"""
This file contains the model for a MODBUS device.

:author: guylev38
:date: 13/12/2025
"""

# ----- Imports ----- #

from enum import Enum

from pydantic import BaseModel

# ----- Classes ----- # 

class ModbusDeviceStatus(Enum):
    ONLINE: int = 1
    OFFLINE: int = 0
    UNKNOWN: int = -1


class ModbusDevice(BaseModel):
    ip : str
    status: ModbusDeviceStatus = ModbusDeviceStatus.UNKNOWN
