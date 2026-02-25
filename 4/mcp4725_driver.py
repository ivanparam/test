import smbus
import time

class MCP4725:
    def __init__(self, dynamic_range, address = 0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        time.sleep(1)

        self.address  = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("НЕ целое число")

        if not (0 <= number <= 4095):
            print("Вне диапазона разрядности")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number * 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)
        
        if self.verbose:
            print(f"Число: {number}, данные на I2C: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self, voltage):
        if (0 <= voltage <= self.dynamic_range):
            number = int(voltage / self.dynamic_range * 4095)
            self.set_number(number)
        else:
            print("Вне динамического диапазона")


if __name__ == "__main__":
    mcp = MCP4725(dynamic_range=4.2, verbose=True)
    try:
        

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                mcp = mcp.set_voltage(voltage)
            except ValueError:
                print("Not a number")
    finally:
        mcp.deinit()