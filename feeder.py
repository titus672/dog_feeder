from gpiozero import OutputDevice
import time


class DogFeeder:
    def __init__(self, enable_pin, pulse_pin, dir_pin):
        self.enable_pin = OutputDevice(enable_pin, active_high=True, initial_value=True)
        self.pulse_pin = OutputDevice(pulse_pin, active_high=True)
        self.dir_pin = OutputDevice(dir_pin, active_high=True)
        self.status = 0
    # function to test stepper motor, accepts a number of steps and a delay in milliseconds

    def drive_stepper(self, steps, delay):
        if steps <= 0:
            self.status = 1
            print("Error, steps must be a positive integer")
        else:
            self.enable_pin.off()
            d = delay / 1000.0
            while steps > 0:
                self.pulse_pin.on()
                time.sleep(d)
                self.pulse_pin.off()
                print("Steps: ", steps)
                steps -= 1
            self.enable_pin.on()
