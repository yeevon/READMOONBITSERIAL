import serial
from datetime import datetime
import pandas as pd

LINES_OF_DATA_COLLECTED = 10

def create_dictionary(data_list: list) -> dict:
    """
    Convert a list of 'key:value' strings into a dictionary with lists of values.
    Assumes each string contains Light, Temp, and Timestamp fields.
    """
    split_data = [d for data in data_list for d in data.split(',')]


    data_dict = {'Light': [], 'Temp': [], 'TimeStamp': []}
    
    for data in split_data:
        get_value = data.split(':', 1)
        data_dict[get_value[0].strip()].append(get_value[1].strip())

    return data_dict

try:
    with serial.Serial(port='/dev/ttyACM0', baudrate=115200) as ser: # Instatiate serial to connect to Microbit
        port_data = []

        print("Collecting data from micro:bit... \nThis can take a few minutes")
        while len(port_data) < LINES_OF_DATA_COLLECTED:
            
            light_temp = ser.readline()
            light_temp_string = light_temp.decode('UTF-8').strip() 

            if 'Light' in light_temp_string:
                light_temp_string += f", TimeStamp: {datetime.now().isoformat()}" # Add time stamp for better logs and tracking
                port_data.append(light_temp_string)


except serial.SerialException as e:
    print(f"[ERROR] Could not open serial port: {e}")
    exit(1)


# Create data frame and create csv# Convert collected data into DataFrame and write to CSV
df = pd.DataFrame(data=create_dictionary(port_data))
df.to_csv('../logs/Microbit Read Out.csv')