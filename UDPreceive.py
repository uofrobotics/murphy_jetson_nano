import socket
from time import sleep

# Set the IP address and port to receive data from the PC
jetson_ip = '142.3.21.101'  # Replace with the Jetson Nano's IP address
jetson_port = 6868  # Replace with the same port as on the PC

# Create a UDP socket and bind it to the specified IP address and port
print("Listening on", jetson_ip, ":", jetson_port)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.bind(('0.0.0.0', jetson_port))

        try:
            # Receive gamepad input data
            data, addr = udp_socket.recvfrom(1024)
            decoded_data = data.decode('utf-8')
            # print("Received Data:", decoded_data)
            new_data = decoded_data.translate(str.maketrans('','','[] '))
            # print("Parsed Data:", new_data)

            # Split the received data by comma to extract axis values
            axis_values = new_data.split(',')
            # print("Axis Values:", axis_values)

            for i in range(len(axis_values)):
                try:
                    axis_value = round(float(axis_values[i]) * 100, 2)
                    print(f"Axis {i}: {axis_value}")
                except ValueError:
                    print(f"Invalid value at Axis {i}: {axis_values[i]}")

        except socket.error as e:
            print(f"Socket error: {e}")
        print()
