import serial
import time

BAUD_RATE=115200

ser = serial.Serial("/dev/cu.usbmodem14201", BAUD_RATE)  # Replace 'COMX' with your Arduino's port

SAMPLE_RATE = 10
with open ("test.txt", "r") as myfile:
    data = myfile.read()
    arr = data.split(", ")[:-1]

for i in range(0, len(arr), SAMPLE_RATE):
    remainingLen = len(arr) - i
    if remainingLen < SAMPLE_RATE:
        subArr = arr[i:i+remainingLen]
    else:
        subArr = arr[i:i+SAMPLE_RATE]

    print(len(subArr))
    count = 0
    for num in subArr:
        ser.write(num.encode())
        print(count)
        count += 1
        time.sleep(1/BAUD_RATE * 50000)
        print(int.from_bytes(ser.read(), byteorder='big', signed=False))

    break

while True:
    print("reading")
    print(int.from_bytes(ser.read(), byteorder='big', signed=False))
    time.sleep(1/BAUD_RATE * 50000)
# ser.close()

# def send_data(data_to_send):
#     loopTime = time.time()
#     print(data_to_send)
#     while time.time() - loopTime < 5:
#         ser.write(data_to_send.encode())

# def sleep():
#     print("sleeping")
#     ser.write('0'.encode())
#     ser.close()
#     time.sleep(3)
#     ser.open()


# start = time.time()
# print(start)
# state = True
# while time.time() - start < 50:
#     sleep()
#     if (state):
#         data_to_send = '100'
#     else:
#         data_to_send = '50'
    
#     send_data(data_to_send)
#     sleep()

#     data_to_send = '0'
#     send_data(data_to_send)
#     sleep()

#     state = not state

# ser.close()