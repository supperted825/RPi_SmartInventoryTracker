import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "YOUR CONNECTION STRING"  

def output_to_dict(result_path):
    # Parse the result.txt file from the command line call
    with open(result_path) as f:
        begin = False
        EIP_count = 0
        output = []
        for line in f:
            if "Enter Image Path:" in line:
                EIP_count += 1
            if begin == True and EIP_count == 1:
                result = line.split("\t")
                output.append(result[0])
            if "./img.jpg" in line:
                begin = True
    
    # Replace the keys with your class names
    count_items = {"Egg" : 0,
                "Milk" : 0,
                "Yoghurt": 0}

    # Increment the count of the relevant class for each instance
    for item in output:
        result = item.split(":")
        item_type = result[0]
        count_items[item_type] += 1

    return count_items
  
def iothub_client_init():  
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
    return client  
  
def iothub_client_send_telemetry(message):  
    client = iothub_client_init()  
    print("Attempting to Send Messages to Azure IoT")  
    print("Sending message: {}".format(message))  
    client.send_message(message)  
    print("Message Sent")
  
if __name__ == '__main__':  
    message = output_to_dict('result.txt')
    iothub_client_send_telemetry(str(message))  
