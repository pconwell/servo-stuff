from machine import Pin, PWM
from time import sleep

led_onboard = Pin(25, Pin.OUT)
servo_pin = Pin(0)
servo = PWM(servo_pin)

def angle_to_duty(angle):
    angle *= 31
    angle = angle + 4600
    if angle > 7400 or angle < 1800:
        print("error, angle is invalid")
    else:
        return angle

servo.freq(50)

min = 1800
max = 7400

print(angle_to_duty(90))
print(angle_to_duty(0))
print(angle_to_duty(-90))
print(angle_to_duty(180))


servo.duty_u16(angle_to_duty(-71))

sleep(.33)

servo.duty_u16(angle_to_duty(-85))
