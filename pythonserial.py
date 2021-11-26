#this function handles serial communication
# Importing Libraries
import serial

def serialcoms(_port, _baudrate, _timeout): 
    comms = serial.Serial(port=_port, baudrate=_baudrate, timeout=_timeout)
    data = comms.readline()
    return data