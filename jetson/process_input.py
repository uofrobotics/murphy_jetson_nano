import math

def process_input(data):
    processed_data = []
    curved_data = []
    mixed_data = []
    
    # Process each value in the data list
    for value in data:
        processed_value = int(value * 100)  # For example, convert it to integers for UART communication
        processed_data.append(processed_value)
        
        # Apply the curve function to each value
        curved_value = match_input_to_curve(processed_value)
        curved_data.append(curved_value)
    
    mixed_data = mixing(curved_data[0], curved_data[1])

    print("Processed Data:", processed_data)
    print("Curved Data:", curved_data)
    print("Mixed Data:", mixed_data)
    return mixed_data

def match_input_to_curve(value):
    sensitivity = 10
    offset = 50

    curved_value = int(128 / (1 + math.exp((-(abs(value)) + offset) / sensitivity)))

    if value < 0:
        curved_value = -curved_value

    return curved_value

def mixing(y_axis, x_axis):

    # Motor configurations
    fl = -(y_axis + x_axis)  # Forward + Right
    fr = -(y_axis - x_axis)  # Forward + Left
    bl = -(y_axis - x_axis)  # Backward + Left
    br = -(y_axis + x_axis)  # Backward + Right

    # Limit motor speeds to the range -128 to 128
    fl = max(min(fr, 128), -128)
    fr = max(min(fl, 128), -128)
    bl = max(min(bl, 128), -128)
    br = max(min(br, 128), -128)

    # Print motor speeds for debugging
    print("Motor 1 Speed:", fl)
    print("Motor 2 Speed:", fr)
    print("Motor 3 Speed:", bl)
    print("Motor 4 Speed:", br)

    motor_speeds = [fr, fl, br, bl]

    return motor_speeds 