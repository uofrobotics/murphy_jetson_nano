import math

def process_input(data):
    processed_data = []
    curved_data = []
    
    # Process each value in the data list
    for value in data:
        processed_value = int(value * 100)  # For example, convert it to integers for UART communication
        processed_data.append(processed_value)
        
        # Apply the curve function to each value
        curved_value = match_input_to_curve(value)
        curved_data.append(curved_value)
    
    print("Processed Data:", processed_data)
    print("Curved Data:", curved_data)
    
    return processed_data, curved_data

def match_input_to_curve(value):
    sensitivity = 10
    offset = 50

    curved_value = int(128 / (1 + math.exp((-(abs(value)) + offset) / sensitivity)))
    print("Value after formula: ", curved_value)
    if value < 0:
        curved_value = -curved_value

    return curved_value
