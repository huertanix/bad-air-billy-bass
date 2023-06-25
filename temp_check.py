import time
import board
import busio
import adafruit_scd30
import subprocess

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
sensor = adafruit_scd30.SCD30(i2c)
waiting_for_sensor_data = True

while waiting_for_sensor_data:

    if sensor.data_available:
        waiting_for_sensor_data = False
        temp_c = sensor.temperature

        print("Temperature: %d C" % temp_c)

        if temp_c > 25: #30:
            temp_announcement = "Ambient temperature is now %d celcius. So hot in here." % temp_c
            subprocess.run(['/usr/bin/espeak', '-v', 'us-mbrola-3'], input=temp_announcement.encode())

            # Play Hot In Herre by Nelly
            subprocess.run(['/usr/bin/mplayer', '/home/billy/03-Hot-In-Herre.ogg'])