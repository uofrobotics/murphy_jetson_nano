# udp_receive.py

import socket
import json
import time
from process_input import process_input
from uart_send import MotorDriver

def receive_udp_and_send_uart(jetson_ip='0.0.0.0', jetson_port=6868, uart_port='/dev/ttyUSB0'):
    motor_driver = MotorDriver()
    print_count = 0

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        # Bind to the specified IP address and port
        udp_socket.bind((jetson_ip, jetson_port))
        
        print(f"Listening for UDP packets on {jetson_ip}:{jetson_port}...")
        
        while True:
            # Receive data from the socket
            data, addr = udp_socket.recvfrom(1024)  # Buffer size is 1024 bytes
            
            # Decode the received data as JSON
            try:
                joystick_data = json.loads(data.decode('utf-8'))
                print_count += 1
                print("(", print_count, ") Received joystick data:", joystick_data)
                
                # Process the received data
                processed_data = process_input(joystick_data)
                
                # TODO: Change input going into motor_driver
                # Send the processed data over UART
                # motor_driver.control_motors(processed_data)
                
                # Optional: Add a small delay to avoid flooding the UART interface
                time.sleep(0.1)
                
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {str(e)}")
            
            except Exception as e:
                print(f"Error processing received data: {str(e)}")

# Example usage
if __name__ == "__main__":
    receive_udp_and_send_uart()
