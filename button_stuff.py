import RPi.GPIO as io

from co2ppm_check import current_status

io.setmode(io.BCM)
io.setup(21, io.IN, pull_up_down=io.PUD_UP)

while True:
    # check for button press on GPIO pin 21
    if io.input(21) == io.LOW:
        # if pressed call current_status(True)
        current_status(True)