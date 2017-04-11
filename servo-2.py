import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servoPin=11
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm.start(7)
for j in range(0,50):
	for i in range(0,180):
		DC=9./170.*(i)+1
		pwm.ChangeDutyCycle(DC)	
		time.sleep(.001)
	for i in range(180,0,-1):
		DC=9./170*(i)+1	
		pwm.ChangeDutyCycle(DC)
		time.sleep(.001)
pwm.stop()
GPIO.cleanup()

