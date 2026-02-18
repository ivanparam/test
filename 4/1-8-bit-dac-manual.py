import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
pins = [22 ,27, 17, 26, 25, 21, 20, 16][::-1]
GPIO.setup(pins, GPIO.OUT)
d_r = 3.1711

def v_t_n(v):
    if not (0.0 <= v <= d_r):
        print("Вне диапазона")
        return 0
    return int(v / d_r * 255)
    
def n_t_d(value):
    GPIO.output(pins, [int(element) for element in bin(value)[2:].zfill(8)])

try:
    while True:
        try:
            v = float(input("Введите напряжение в вольтах: "))
            n = v_t_n(v)
            n_t_d(n)

        except ValueError:
            print("Это не число")


finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()