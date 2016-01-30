import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

f = open("picture.jpg","r") # picture.jpg is picture file name
pic = f.read()

ser.write('%s\n' % pic)
print 'Finished sending\n'
f.close()
