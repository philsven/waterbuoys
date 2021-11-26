#parses the input
from pythonserial import serialcoms

while True: 
    data_read = serialcoms("COM4", 9600)
    
    start_str  = 1001 
    msg_flag = 0
    
    if (data_read == start_str):
        msg_flag = 1
    elif(data_read == end_str): 
        msg_flag = 0
    