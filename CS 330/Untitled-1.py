# """This code has to have 3 imports, serial, time, and struct. You then need to have line 12 due to the fact that you need to enstablish connection with the robot. You need to then have sleep code
# after each reset. This allows the robot to have time to do the commands that has been told to do. You need to make the code run normal speed which is set at 100 and then have it set at 2x speed.
# The biggest problem was the sensors and getting the wall sensors to work as it was not picking up the wall sensors but now does. """
# import serial
# import time
# import struct
# connection = serial.Serial('COM4',115200, timeout=1)


# #connection.write(b'\x80\x07')
# #time.sleep(10)
# #connection.write(b'\x80\x83')

# #This makes the robot go foward at 100 speed.
# connection.write(b'\x80')
# connection.write(b'\x07')
# time.sleep(10)
# connection.write(b'\x80')
# connection.write(b'\x83')
# time.sleep(10)
# connection.write(b'\x89\x01\x64\x01\x64')


# #go 2x speed
# connection.write(b'\x80\x07')
# #ime.sleep(10)
# connection.write(b'\x80')
# connection.write(b'\x83')
# time.sleep(10)
# connection.write(b'\x93\x01\xC8\x01\xC8')


# #This makes the robot go backwards
# connection.write(b'\x80\x07')
# time.sleep(10)
# connection.write(b'\x80')
# connection.write(b'\x83')
# time.sleep(10)
# connection.write(b'\x89\xFF\x40\x40\x00')


# #This makes the robot display the LED number 7
# connection.write(b'\x80\x07')
# time.sleep(10)
# connection.write(b'\xA3\x07\x07\x07\x07')


# #This makes the robot display the LED number 0
# connection.write(b'\xA4\x00\x00\x00\x00')


# #This makes the robot display the LED birth year
# connection.write(b'\xA4\x32\x30\x30\x34')


# #This makes one wheel drive and the other wheel not drive
# connection.write(b'\x89\x00\x00\x01\xC8')


# #This makes both wheels spin in oposite direction
# connection.write(b'\x91\xFF\x40\x40\x00')


# #Sensors for wheels and bumpers
# connection.write(b'\x80')
# connection.write(b'\x8E\x07')
# buttonState1=connection.read()
# byte=struct.unpack('B', buttonState1)[0]
# binary='{0:08b}'.format(byte)
# print(binary)


# #Wall sensors (very sensitive)
# connection.write(b'\x8E\x1B')
# buttonState = connection.read()
# byte = struct.unpack('B', buttonState)[0]
# binary1 = '{0:08b}'.format(byte)

# buttonState = connection.read()
# byte = struct.unpack('B', buttonState)[0]
# binary2 = '{0:08b}'.format(byte)
# print(binary1, binary2)
