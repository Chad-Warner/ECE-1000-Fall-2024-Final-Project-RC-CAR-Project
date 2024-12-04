# Author: peppe8o
# Blog: https://peppe8o.com
# Date: Jun 3st, 2021
# Version: 1.0

from machine import Pin, PWM
from time import sleep

servoPin = PWM(Pin(00))
servoPin.freq(50)

def servo(degrees):
    # limit degrees beteen 0 and 180
    if degrees > 115: degrees=115
    if degrees < 65: degrees=65
    # set max and min duty
    maxDuty=9000
    minDuty=1000
    # new duty is between min and max duty in proportion to its value
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    # servo PWM value is set
    servoPin.duty_u16(int(newDuty))
#
#while True:
  # start increasing loop
#  for degree in range(0,180,1):
#    servo(degree)
#    sleep(0.001)
    #print("increasing -- "+str(degree))
  # start decreasing loop
#  for degree in range(180, 0, -1):
#    servo(degree)
#    sleep(0.001)
    #print("decreasing -- "+str(degree))