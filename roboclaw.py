import struct

import serial
from PyCRC.CRCCCITT import CRCCCITT

from roboclaw_cmd import Cmd

import time


class RoboClaw:
    def __init__(self, port):
        self.port = serial.Serial(baudrate=115200, timeout=0.1, interCharTimeout=0.01)
        self.port.port = port
        try:
            self.port.close()
            self.port.open()
        except serial.serialutil.SerialException as e:
            self.recover_serial()
            print(e)

    def _read(self, address, cmd, fmt):
        cmd_bytes = struct.pack('>BB', address, cmd)
        try:
            # self.port.reset_input_buffer()  # TODO: potential bug?
            self.port.write(cmd_bytes)
            return_bytes = self.port.read(struct.calcsize(fmt) + 2)
        except:
            self.recover_serial()
            raise Exception
            # TODO
        crc_actual = CRCCCITT().calculate(cmd_bytes + return_bytes[:-2])
        crc_expect = struct.unpack('>H', return_bytes[-2:])[0]
        if crc_actual != crc_expect:
            raise Exception
            # TODO
        return struct.unpack(fmt, return_bytes[:-2])

    def _write(self, address, cmd, fmt, *data):
        cmd_bytes = struct.pack('>BB', address, cmd)
        data_bytes = struct.pack(fmt, *data)
        write_crc = CRCCCITT().calculate(cmd_bytes + data_bytes)
        crc_bytes = struct.pack('>H', write_crc)
        try:
            self.port.write(cmd_bytes + data_bytes + crc_bytes)
            self.port.flush()
            verification = self.port.read(1)
        except:
            self.recover_serial()
            raise Exception
            # TODO
        if 0xff != struct.unpack('>B', verification)[0]:
            raise

    def set_speed(self, address, motor, speed):
        # assert  < speed < 128
        assert motor in [1, 2]
        if motor == 1:
            cmd = Cmd.M1SPEED
        else:
            cmd = Cmd.M2SPEED
        self._write(address, cmd, '>i', speed)

    def read_currents(self, address):
        currents = self._read(address, Cmd.GETCURRENTS, '>hh')
        return tuple([c / 100. for c in currents])

    def read_voltages(self, address):
        mainbatt = self._read(address, Cmd.GETMBATT, '>H')[0] / 10.
        logicbatt = self._read(address, Cmd.GETLBATT, '>H')[0] / 10.
        return mainbatt, logicbatt

    def recover_serial(self):
        self.port.close()
        while not self.port.isOpen():
            try:
                self.port.close()
                self.port.open()
            except serial.serialutil.SerialException as e:
                time.sleep(0.2)
                print('fail')
                print(e)
