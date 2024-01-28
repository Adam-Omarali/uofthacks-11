import serial
import time

port = serial.Serial('/dev/cu.usbmodem14201',9600)

def led_on_off(x):
    port.write(x.to_bytes(1,'big'))

with open ("test.txt", "r") as myfile:
    data = myfile.read()
    arr = data.split(", ")[:-1]

print(len(arr) / 130)

while(True):
    choice = input("Make your choice!(on/off/quit) ")

    if choice == 'on':
        led_on_off(1)
        
    elif choice =='off':
        led_on_off(0)
        
    elif choice == 'quit':
        break

    else:
        counter = 0
        for l in range(0, 1300):
            print(arr[l])
            led_on_off(int(arr[l]))
            # for k in range(0, 13):
            #     for i in range(0,130):
            #         led_on_off(int(arr[i + counter]))

            #     counter += 130
                # time.sleep(0.0001)
            # time.sleep(0.0001)