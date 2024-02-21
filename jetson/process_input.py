# process_input.py
import math

def process_input(data):
    # Process the received data
    # For example, convert it to integers for UART communication
    processed_data = [int(val * 100) for val in data]
    print("     Processed Data: ", processed_data)
    curved_data = match_input_to_curve(data)
    print("     Curved Data: ", curved_data)

    return processed_data

def match_input_to_curve(value):
    sensitivity = 10
    offset = 50
    curved_value = []

    for i in range(value):
        curved_value[i] = int(128 / (1 + math.exp((-(abs(value[i])) + offset) / sensitivity)))

        if value[i] < 0:
            curved_value[i] = -curved_value

    

    return curved_value
