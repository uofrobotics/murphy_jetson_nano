# PyControlNucleo

PyControlNucleo is a Python project that enables communication between a host computer, a controller input device (such as a joystick), and a Nucleo board over UDP and UART protocols.

### Features

1. Read controller input from a host computer using Pygame.
2. Send controller input data over UDP to a specified IP address and port.
3. Receive data on a Nucleo board over UART and process it.

### Installation

- Clone the repository:

``` bash
git clone https://github.com/yourusername/PyControlNucleo.git
```

- Install the required dependencies:
``` bash
    pip install -r requirements.txt
```

### Usage

- Connect your controller input device (e.g., joystick) to the host computer.

- Modify the host_computer.py script to configure the IP address and port of the Jetson Nano (the receiver) and run it:
```
python host_computer.py
```
- Modify the nucleo_communication.py script to configure the UART settings and Nucleo board serial port, and run it:
```
python nucleo_communication.py
```