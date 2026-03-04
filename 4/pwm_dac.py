import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        self.pwm.stop()
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, number):
        if (0.0 <= voltage <= self.dynamic_range):
            duty_cycle = (voltage / self.dynamic_range * 100)
        else:
            print("Вне диапазона")
            return 0
        self.pwm.ChangeDutyCycle(duty_cycle)    
        print(f"КОффициент заполнения {duty_cycle:.2f} В")

        
if __name__ == "__main__":
    dac = PWM_DAC(12, 500, 3.183, True)
    try:

        while True:
            try:
                voltage = float(input('Введите напряжение в вотльтах: '))
                dac.set_voltage(voltage)

            except ValueError():
                        print('Вы ввели не числою')
    finally:
        dac.deinit()    