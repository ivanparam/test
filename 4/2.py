import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Вне диапазона")
            return 0
        
        value = int(voltage / self.dynamic_range * 255)
        return [int(element) for element in bin(value)[2:].zfill(8)]
    
    def set_voltage(self, voltage):
        bin = self.set_number(voltage)
        GPIO.output(self.gpio_bits, bin)

if __name__ == "__main__":
    dac = R2R_DAC(([16, 20, 21, 25, 26, 17, 27, 22]), 3.183, True)
    try:

        while True:
            try:
                voltage = float(input('Введите напряжение в вотльтах: '))
                dac.set_voltage(voltage)

            except ValueError():
                        print('Вы ввели не числою')
    finally:
        dac.deinit()