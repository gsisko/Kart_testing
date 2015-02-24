#!/user/bin/env python

import serial
import rospy
from std-msgs.msg import Char

port serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

def callback(data):
	#right now, all we a doing is logging the 
	#data received from the node
	rosppy.loginfo(data.data)
	poprt.write(data)

def listener():
	#initialize the listener node for the motor controller
	#feed the char data coming in on the subscriber to the
	#call back function
	rospy.init_node('motor_listener', anonymous=True)
	rospy.Subscriber("motor_signal", Char, callback)
	
	#keeps node from exiting
	rospy.spin()


#use for pwm, which will not work because of software calculation.
'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)	#setup an oputut pin on port 25
p = GPIO.PWM(25, 50)		#crate the pwm obejct at 50 hz

p.start(50)
p.ChangeDutyCycle(90)		#duty cycle of the PWM signal
p.ChangeFrequency(1000)		#frequency of PWM Signal in Hz
p.stop()

GPIO.cleanup()
'''
