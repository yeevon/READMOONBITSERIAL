import serial
import pandas as pd
from graphData import GraphData
from datetime import datetime


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


def get_data(microbit_data: list) -> dict:
    
    data_dict = {}
    for data_point in microbit_data[-1].split(","):
        key, value = data_point.split(":", 1)
        key = key.strip().lower()
        if key in ("light", "temp"):
            data_dict[key] = int(value.strip())

    return data_dict


def collect_microbit_data():
    gd = None
    port_data = []
    try:
        # Instatiate serial to connect to Microbit
        with serial.Serial(port='/dev/ttyACM0', baudrate=115200) as ser: 
            gd = GraphData()

            print("Collecting data from micro:bit... \nThis can take a few minutes")

            while True:
                
                light_temp = ser.readline()
                light_temp_string = light_temp.decode('UTF-8', errors='ignore').strip() 

                if 'Light:' in light_temp_string and 'Temp:' in light_temp_string:
                    # Add time stamp for better logs and tracking
                    light_temp_string += f", TimeStamp: {datetime.now().isoformat()}" 
                    port_data.append(light_temp_string)
                    
                    light_temp_dict = get_data(port_data)
                    gd.input_plot_data(len(port_data), light=light_temp_dict["light"], temp=light_temp_dict["temp"])
                
    except serial.SerialException:
        print("Microbit disconnected")

    except KeyboardInterrupt:
        print("Data collection stopped by user")

    except Exception as e:
        print(e)
    
    finally:
        if gd: gd.stop_graph()
        return port_data


# Create data frame and create csv# Convert collected data into DataFrame and write to CSV
df = pd.DataFrame(data=create_dictionary(collect_microbit_data()))
df.to_csv('../logs/Microbit Read Out.csv', index=False)