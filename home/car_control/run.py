import RPi.GPIO as GPIO
import time

class CarRun:
    def __init__(self):
        IN = [20, 21, 19, 26]
        EN_A = 16
        EN_B = 13

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    @staticmethod
    def motor_init():
        global pwm_EN_A
        global pwm_EN_B
        global dt # Delaytime

        for i in range(4):
            GPIO.setup(IN[i], GPIO.OUT, initial = 0)

        GPIO.setup(EN_A, GPIO.OUT, initial = 1)
        pwm_EN_A = GPIO.PWM(EN_A, 2000)
        pwm_EN_A.start(0)

        GPIO.setup(EN_B, GPIO.OUT, initial = 1)
        pwm_EN_B = GPIO.PWM(EN_B, 2000)
        pwm_EN_B.start(0)

    @staticmethod
    def brake(dt = 1):
        for i in range(4):
            GPIO.output(IN[i], 0)

        pwm_EN_A.ChangeDutyCycle(80)
        pwm_EN_B.ChangeDutyCycle(80)

        time.sleep(dt)

    # Go Advance
    def advance(dt = 1, b_k = 0):
        for i in range(4):
            t = IN[i]%2 == 0
            GPIO.output(IN[i], t)

        pwm_EN_A.ChangeDutyCycle(80)
        pwm_EN_B.ChangeDutyCycle(80)

        time.sleep(dt)
        if b_k == 0:
            brake()

    # Go Back
    def back(dt = 1, b_k = 0):
        for i in range(4):
            t = IN[i]%2 == 1
            GPIO.output(IN[i], t)

        pwm_EN_A.ChangeDutyCycle(80)
        pwm_EN_B.ChangeDutyCycle(80)

        time.sleep(dt)
        if b_k == 0:
            brake()

    # Turn Left
    def left(dt = 2, b_k = 0):
        for i in range(4):
            t = IN[i] == 2
            GPIO.output(IN[i], t)

        pwm_EN_A.ChangeDutyCycle(80)
        pwm_EN_B.ChangeDutyCycle(80)

        time.sleep(dt)
        if b_k == 0:
            brake()

    # Turn Right
    def right(dt = 2, b_k = 0):
        for i in range(4):
            t = IN[i] == 0
            GPIO.output(IN[i], t)

        pwm_EN_A.ChangeDutyCycle(80)
        pwm_EN_B.ChangeDutyCycle(80)

        time.sleep(dt)
        if b_k == 0:
            brake()

    # Turn Left in Situ
    def situ_left(dt = 3, b_k = 0):
        for i in range(4):
            t = IN[i] in [1, 2]
            GPIO.output(IN[i], t)

        pwm_EN_A.ChangeDutyCycle(80)
        pwm_EN_B.ChangeDutyCycle(80)

        time.sleep(dt)
        if b_k == 0:
            brake()

    # Turn Right in Situ
    def situ_right(dt = 3, b_k = 0):
        for i in range(4):
            t = IN[i] in [0, 3]
            GPIO.output(IN[i], t)

        pwm_EN_A.ChangeDutyCycle(80)
        pwm_EN_B.ChangeDutyCycle(80)

        time.sleep(dt)
        if b_k == 0:
            brake()

    # Stop to Run the Car
    def stop_run():
        brake()

    # End Control
    def all_stop():
        pwm_EN_A.stop()
        pwm_EN_A.stop()

        GPIO.cleanup()
