import serial, time
  
ser = serial.Serial()
ser.port = "COM6"
  
# 115200, N, 8, 1
# ser.baudrate = 9600, 14400, 19200, 38400, 57600, 115200, 128000
ser.baudrate = 128000
ser.bytesize = serial.EIGHTBITS # Number of bits per bytes
ser.parity = serial.PARITY_NONE # Set parity check
ser.stopbits = serial.STOPBITS_ONE # Number of stop bits
  
ser.timeout = 3          # Non-block read 3 seconds
ser.writeTimeout = 3     # Timeout for write 3 seconds
ser.xonxoff = False    # Disable software flow control
ser.rtscts = False     # Disable hardware (RTS/CTS) flow control
ser.dsrdtr = False     # Disable hardware (DSR/DTR) flow control
  
try: 
    ser.open()
except Exception as ex:
    print ("Open serial port error " + str(ex))
    exit()
  
if ser.isOpen():
  
    try:
        ser.flushInput() # Flush input buffer
        ser.flushOutput() # Flush output buffer
  
        # Write 8 byte data
        write_string = ser.write([78, 78, 78, 78, 78, 78, 78, 78])
        # write_string = ser.write(b'\x41')
        print("Write byte data: %s"%(write_string))
  
        time.sleep(0.5)  # Wait 0.5 seconds
  
        # Read byte data
        response = ser.read(write_string)
        print("Read byte data:")
        print(response)
  
        ser.close()
    except Exception as e:
        print ("Communicating error " + str(e))
  
else:
    print ("Open serial port error")