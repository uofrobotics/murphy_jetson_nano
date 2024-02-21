# process_input.py

def process_input(data):
    count = 0
    # Process the received data
    # For example, convert it to integers for UART communication
    processed_data = [int(val * 100) for val in data]
    count += 1
    print("(", count, ") Processed Data: ", processed_data)
    return processed_data
