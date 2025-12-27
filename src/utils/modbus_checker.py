"""
This file contains code that checks the MODBUS communciation.

:author: guylev38
:date: 13/12/2025
"""

# ----- Imports ----- #

import logging

from pymodbus.client import AsyncModbusTcpClient
from pymodbus.pdu import ModbusPDU

from models.modbus_device import ModbusDevice, ModbusDeviceStatus

# ----- Consts ----- #

MODBUS_PORT = 502

# ----- Classes ----- #

class ModbusNoResponseError(Exception):
    pass

class ModbusChecker:
    def __init__(self, devices: list[ModbusDevice]):
        self._devices: list[ModbusDevice] = devices

    async def _check_device(self, device: ModbusDevice) -> ModbusDevice:
        """
        Checks a given MODBUS device.

        :param device: The MODBUS device to check.  
        :returns: The MODBUS device with it's updated status.
        """

        client: AsyncModbusTcpClient = AsyncModbusTcpClient(host=device.ip, port=MODBUS_PORT)

        try:
            logging.debug(f"Checking device {device.ip}...")
            await client.connect()
            
            data: ModbusPDU = await client.read_holding_registers(0)

            if data is None:
                logging.error(f"Got no response from device {device.ip}!")
                raise ModbusNoResponseError
            
            if data.isError():
                logging.warning(f"Device {device.ip} ONLINE with ERROR") 

            else:
                logging.info(f"Device {device.ip} ONLINE!") 

            device.status = ModbusDeviceStatus.ONLINE 

        except Exception as exc:
            logging.error(f"Occured a MODBUS exception {exc}\nCouldn't connect to device {device.ip}")
            device.status = ModbusDeviceStatus.OFFLINE  

        client.close()
        
        return device

    async def check(self) -> list[ModbusDevice]:
        """
        Checks a all of the devices given to the checker.

        :returns: A list of MODBUS devices with their updated status.
        """        

        updated_devices: list[ModbusDevice] = []

        for device in self._devices:
            updated_device = await self._check_device(device)
            updated_devices.append(updated_device)

        return updated_devices
        