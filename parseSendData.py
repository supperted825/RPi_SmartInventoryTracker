import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

#CONNECTION_STRING = "2DmUEtae0rAgcT37KoUOmjzDjoKcnsZPjskEp9WR01i69B62HkHOxgmaZgRU24foWgh5+wY3wXwCqizzhhqRwA=="
CONNECTION_STRING = "HostName=iotc-63d32082-e94b-4f92-9aa1-3bd1635dd1c1.azure-devices.net;DeviceId=RPi26ly4vvdzqt;SharedAccessKey=kACc5Wugca7Fq1SFcymvJfpJjoZE74AuxGKCk/HGHc0="  

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