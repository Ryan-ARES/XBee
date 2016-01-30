import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
string = 'Hello from ARES-pi!'
print 'Sending "%s" ' % string
ser.write('%s\n' % string)
