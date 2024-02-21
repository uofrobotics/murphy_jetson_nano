# Host2Jetson

Host2Jetson is a Python project that enables communication between a host computer, a controller input device (such as a joystick), and a Jetson computer over UDP protocol

### Features

1. Read controller input from a host computer using Pygame.
2. Send controller input data over UDP to a specified IP address and port.
3. Receive data on a Jetson Nano and process it.

### Installation

- Clone the repository:

``` bash
git clone https://github.com/uofrobotics/Host2Jetson.git
```

- Install the required dependencies:
``` bash
pip install -r requirements.txt
```

### Usage

1. Connect your controller input device (e.g., joystick) to the host computer.

2. Modify the host_computer.py script to configure the IP address and port of the Jetson Nano (the receiver) and run it:
```
python3 host_computer.py
```
