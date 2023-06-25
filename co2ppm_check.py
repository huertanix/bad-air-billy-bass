import time
import board
import busio
import adafruit_scd30
import subprocess

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
sensor = adafruit_scd30.SCD30(i2c)

def current_status(button_pressed=False):
    if sensor.data_available:

        # Stuff CO2 reading in a variable to not bother the sensor so much 
        co2ppm = sensor.CO2

        # Console output for debugging
        print("CO2: %d PPM" % co2ppm)

        # Announce when it's bad, chill otherwise
        if co2ppm > 1399:
            red_alert = "See Oh Two at %d parts per million, which is really bad by he way. Are you all trying to get covid?" % co2ppm
            subprocess.run(['/usr/bin/espeak', '-v', 'us-mbrola-3'], input=red_alert.encode())
        elif co2ppm > 999:
            yellow_alert = "See Oh Two at %d parts per million, consider opening a window." % co2ppm
            subprocess.run(['/usr/bin/espeak', '-v', 'us-mbrola-3'], input=yellow_alert.encode())

	    # Manual override
        if button_pressed is True:
            status_report = "See Oh Two at %d parts per million." % co2ppm
            subprocess.run(['/usr/bin/espeak', '-v', 'us-mbrola-3'], input=status_report.encode())

current_status()
