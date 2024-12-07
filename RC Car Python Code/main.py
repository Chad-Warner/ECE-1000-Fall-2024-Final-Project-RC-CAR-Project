# Import necessary modules
from machine import Pin, PWM
import bluetooth
from time import sleep
from L298N_motor import L298N
from time import sleep
from ble_simple_peripheral import BLESimplePeripheral
import picoSg90servo

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

servoPin = PWM(Pin(00))
servoPin.freq(50)

timer = 0
trimmedDataString = ""

led = Pin("LED", Pin.OUT)
led2 = Pin("GP17", Pin.OUT)

ENA = Pin("GP16", Pin.OUT)
IN1 = Pin("GP1", Pin.OUT)
IN2 = Pin("GP2", Pin.OUT)

motor = L298N(ENA, IN1, IN2)
degree = 90
led_state = 0
led2.value(0)


def servo(degrees):
    # limit degrees beteen 0 and 180
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    # set max and min duty
    maxDuty=9000
    minDuty=1000
    # new duty is between min and max duty in proportion to its value
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    # servo PWM value is set
    servoPin.duty_u16(int(newDuty))
#


# Define a callback function to handle received data
def on_rx(data):
    print("Data received: ", data)  # Print the received data
    global led_state  # Access the global variable led_state
    if data == b'toggle\r\n':  # Check if the received data is "toggle"
        led.value(not led_state)  # Toggle the LED state (on/off)
        led_state = 1 - led_state  # Update the LED state
    if "forward" in data:
        led2.value(100)

        dataString = str(data)
        trimmedDataString = str(dataString.split(',')[1])
        timer = int(trimmedDataString.split('\\r')[0])
        
        motor.forwardFor(timer)
        led2.value(0)

        
    if "backward" in data:
        led2.value(100)

        dataString = str(data)
        trimmedDataString = str(dataString.split(',')[1])
        timer = int(trimmedDataString.split('\\r')[0])
        
        motor.backwardFor(timer)
        led2.value(0)
        
    if "left" in data:
        
        servo(55)
        
        
        
    if "right" in data:
        servo(125)
        
    if data == b'straight\r\n':
        servo(90)
        
# Start an infinite loop
while True:
    if sp.is_connected():  # Check if a BLE connection is established
        sp.on_write(on_rx)  # Set the callback function for data reception
        led.value(100)
    else:
        led.value(0)