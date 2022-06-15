from machine import Pin, PWM
from time import sleep

# set pins
led_onboard = Pin(25, Pin.OUT)
servo_pin = Pin(0)
servo = PWM(servo_pin)

# set servo duty cycle range
min = 1800
max = 7400

# convert angle to "duty cycle"
def angle_to_duty(angle):
    angle *= 31
    angle = angle + 4600
    if angle > max or angle < min:
        print("error, angle is invalid")
    else:
        return angle

servo.freq(50)



#print(angle_to_duty(90))
#print(angle_to_duty(0))
#print(angle_to_duty(-90))
#print(angle_to_duty(180))

while True:
    servo.duty_u16(angle_to_duty(-30))
    sleep(15)
    servo.duty_u16(angle_to_duty(-75))
    sleep(30)
