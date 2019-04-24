
import smbus
import subprocess
from time import sleep

#firmware setup/functions
bus = smbus.SMBus(1)
address = 0x04

# 2= stop, 4 = backward, 5 = forward, turn right = 6, turnleft = 7, 
#spin right = 8, spin left =9
def write_number(value):
    bus.write_byte(address, value)
    return -1

def power_off_pi():
    tts.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    tts.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)
    
def get_cmds():
	print(" 2= stop, 4 = backward, 5 = forward, turn right = 6, turnleft = 7,"
      + "spin right = 8, spin left =9")

def right_100():
	write_number(8)
	sleep(.1)
	write_number(2)

def left_100():
        write_number(9)
        sleep(.1)
        write_number(2)

