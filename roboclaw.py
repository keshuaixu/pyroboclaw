import struct

from PyCRC.CRCCCITT import CRCCCITT

from roboclaw_cmd import Cmd


class RoboClaw:
    def __init__(self, port):
        self.port = port

    def _read(self, address, cmd, fmt):
        cmd_bytes = struct.pack('>BB', address, cmd)
        try:
            self.port.reset_input_buffer()  # TODO: why?
            self.port.write(cmd_bytes)
            return_bytes = self.port.read(struct.calcsize(fmt) + 2)
        except:
            raise
            # TODO
        crc_actual = CRCCCITT().calculate(cmd_bytes + return_bytes[:-2])
        crc_expect = struct.unpack('>H', return_bytes[-2:])[0]
        if crc_actual != crc_expect:
            raise
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
            raise
            # do recevery
        if 0xff != struct.unpack('>B', verification)[0]:
            raise

    def set_speed(self, address, motor, speed):
        # assert  < speed < 128
        assert motor in [1, 2]
        if motor == 1:
            cmd = Cmd.M1SPEED
        elif motor == 2:
            cmd = Cmd.M1SPEED
        else:
            raise
        self._write(address, cmd, '>i', speed)

    def read_voltages(self, address):
        mainbatt = self._read(address, Cmd.GETMBATT, '>H')[0] / 10
        logicbatt = self._read(address, Cmd.GETLBATT, '>H')[0] / 10
        return mainbatt, logicbatt
