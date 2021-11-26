#parses the input
from pythonserial import serialcoms
import time

msg = {
    "nodeId": 0,
    "userId": 0,
    "datekey": 0,
    "gps": {
      "lat": 0,
      "long": 0,  
    },
    1: {
        "sensorId": 0,
        "value": 0}, 
    2: {
        "sensorId": 0,
        "value": 0
    },
    3: {
        "sensorId": 0,
        "value": 0
    }};

while True: 
    data_read = serialcoms("COM4", 9600)
    
    start_str  = 1001 
    msg_flag = 0
    
    if (data_read == start_str):
        msg_flag = 1
    elif(data_read == end_str): 
        msg_flag = 0
    
    if(msg_flag):
        sensor_code  = data_read[:4]
        data_value = data_read[5:]
        
        match sensor_code:
            #1010 -> Temp; 1011 -> TDS; 1101 -> Turbidity
            case 1001:
                msg[1]["sensorId"] = sensor_code
                msg[1]["value"] = data_value
                pass
            case 1010:
                msg[2]["sensorId"] = sensor_code
                msg[2]["value"] = data_value
                pass
            case 1011:
                msg[3]["sensorId"] = sensor_code
                msg[3]["value"] = data_value
                pass
        