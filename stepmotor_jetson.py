import Jetson.GPIO as GPIO
Import time
GPIO.setmode(GPIO.BOARD)

dirPin1 = 21
stepPin1 = 22
dirPin1 = 23
stepPin1 = 24

stepsPerRevolution = 200

GPIO.setup(dirPin1, GPIO.OUT)
GPIO.setup(stepPin1, GPIO.OUT)
GPIO.setup(dirPin1, GPIO.OUT)
GPIO.setup(stepPin1, GPIO.OUT)

while(1):
	GPIO.output(dirPin1, GPIO.HIGH)
	GPIO.output(dirPin2, GPIO.HIGH)

	for I in range(stepsPerRevolution):
		GPIO.output(stepPin1, GPIO.HIGH)
		GPIO.output(stepPin2, GPIO.HIGH)
		time.sleep(0.02)
		GPIO.output(stepPin1, GPIO.LOW)
		GPIO.output(stepPin2, GPIO.LOW)
		time.sleep(0.02)

	time.sleep(1)
		
