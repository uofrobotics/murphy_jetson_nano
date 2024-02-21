import serial
import time
import json

def send_data_over_uart(data):
    # Open UART connection
    with serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1) as ser:
        # Convert data to integers (example: multiply by 100 for precision)
        integer_data = [int(val * 100) for val in data]
        
        # Convert integer data to bytes
        serialized_data = bytes(json.dumps(integer_data), 'utf-8')
        
        # Send data over UART
        ser.write(serialized_data)
        
        # Wait for a short time to ensure the data is transmitted
        time.sleep(0.1)
        