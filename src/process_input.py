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
    safe_value = 10
    # y_axis = -y_axis
    # Motor configurations
    fr = -(y_axis + x_axis)  # Forward + Right
    fl = -(y_axis - x_axis)  # Forward + Left
    bl = -(y_axis - x_axis)  # Backward + Left
    br = -(y_axis + x_axis)  # Backward + Right

    # Limit motor speeds to the range -128 to 128
    fr = max(min(fr, safe_value), -safe_value)
    fl = max(min(fl, safe_value), -safe_value)
    bl = max(min(bl, safe_value), -safe_value)
    br = max(min(br, safe_value), -safe_value)

    # Print motor speeds for debugging
    print("fl Speed:", fl, " fr Speed:", fr)
    print("bl Speed:", bl, " br Speed:", br)

    motor_speeds = [fl, fr, bl, br]

    return motor_speeds 