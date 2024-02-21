# process_input.py

def process_input(data):
    # Process the received data
    # For example, convert it to integers for UART communication
    processed_data = [int(val * 100) for val in data]
    return processed_data
