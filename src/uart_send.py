#!/usr/bin/python3
import time
import serial
from sys import exit
from subprocess import run, PIPE
# https://jetsonhacks.com/2019/10/10/jetson-nano-uart/
# https://github.com/JetsonHacksNano/UARTDemo/blob/master/uart_example.py
# https://github.com/uofrobotics/jetson-core/blob/main/code/nucleo_driver.py
SERIAL_READ_TIMEOUT = 1  # seconds

UART_DEVICE = "/dev/ttyTHS1"


class MotorDriver:
    def __init__(self) -> None:
        # check that no one else is using the uart port:
        output = run(["lsof",  "-w",  "/dev/ttyTHS1"], stdout=PIPE, stderr=PIPE)

        if output.stderr != b'' or output.stdout != b'' or output.returncode != 1:
            # there is someone using the port, print that:
            print(f"Some other process is using {UART_DEVICE}, cannot safely start another motor driver")
            print("Kill that process, then run again")
            print(f"stdout: {output.stdout}")
            print(f"stderr: {output.stderr}")

            # hard exit our script, continuing to run is unsafe
            # don't raise Exception, it could be caught and neglected = bad
            exit(1);

        self.serial_port = serial.Serial(
            port=UART_DEVICE,
            baudrate=115200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=SERIAL_READ_TIMEOUT,  # wait at most one second for a response from nucleo
        )
        # Wait a second to let the port initialize
        time.sleep(1)

    # inputs are in the range [-127, 127] where positive numbers drive a motor forward, negative backwards
    def control_motors(self, fl: int, fr: int, bl: int, br: int):
        assert fl <= 127 and fl >= -127
        assert fr <= 127 and fr >= -127
        assert bl <= 127 and bl >= -127
        assert br <= 127 and br >= -127

        # drive motor control packet between [129, 144]

        if bl > 0:
            bl_bit = 1
        else:
            bl_bit = 0

        if br > 0:
            br_bit = 1
        else:
            br_bit = 0

        if fl > 0:
            fl_bit = 1
        else:
            fl_bit = 0

        if fr > 0:
            fr_bit = 1
        else:
            fr_bit = 0

        motor_dir_control_packet = 129 + (
            (bl_bit << 3) | (br_bit << 2) | (fl_bit << 1) | (fr_bit << 0)
        )

        self.serial_port.write(motor_dir_control_packet.to_bytes(1, "big"))
        # any slower and motor speed commands are not reliable
        time.sleep(0.001)

        self.serial_port.write(abs(bl).to_bytes(1, "big"))
        time.sleep(0.001)

        self.serial_port.write(abs(br).to_bytes(1, "big"))
        time.sleep(0.001)

        self.serial_port.write(abs(fl).to_bytes(1, "big"))
        time.sleep(0.001)

        self.serial_port.write(abs(fr).to_bytes(1, "big"))
        time.sleep(0.001)

    def close(self):
        self.serial_port.close()