import time

from upm import pyupm_grove as grove

def main():
    # Create the Grove LED object using GPIO pin 2
    led = grove.GroveLed(13)
    btn = grove.GroveButton(3)

    while 1:
        if btn.value() == 0:
            led.on()
        else:
            led.off()

    # Delete the Grove LED object
    del led
    del btn
if __name__ == '__main__':
    main()
