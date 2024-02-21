import socket
import json


def receive_udp_data(jetson_ip='0.0.0.0', jetson_port='6868'):
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
                print_count+=1
                print("(", print_count, ") Received joystick data:", joystick_data)
                
                # Process the received data here (e.g., control your robot)
                # Example:
                # for i, axis_value in enumerate(joystick_data):
                #     print(f"Axis {i}: {axis_value}")
                
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {str(e)}")
            
            except Exception as e:
                print(f"Error processing received data: {str(e)}")
