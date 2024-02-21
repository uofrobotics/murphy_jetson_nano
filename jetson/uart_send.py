# uart_send.py

import serial
import json

def send_uart_data(data, uart_port='/dev/ttyTHS1'):
    # Open UART connection
    with serial.Serial(uart_port, baudrate=115200, timeout=1) as ser:
        # Convert data to bytes
        serialized_data = bytes(json.dumps(data), 'utf-8')
        
        # Send data over UART
        ser.write(serialized_data)
