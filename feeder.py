from gpiozero import OutputDevice
import time


class DogFeeder:
    def __init__(self, enable_pin, pulse_pin):
        self.enable_pin = OutputDevice(enable_pin, False, False)
        self.pulse_pin = OutputDevice(pulse_pin, False, False)
        self.status = 0
    # function to test stepper motor, accepts a number of steps and a delay in milliseconds

    def test_stepper(self, steps, delay):
        if steps <= 0:
            self.status = 1
            print("Error, steps must be a positive integer")
        else:
            self.enable_pin.on()
            d = delay / 1000.0
            while steps > 0:
                self.pulse_pin.on()
                time.sleep(d)
                self.pulse_pin.off()
                print("Steps: ", steps)
                steps -= 1
