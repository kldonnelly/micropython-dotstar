import time
import random
import python_dotstar as dotstar
import spidev

# On-board DotStar for the raspi
# We only have SPI bus 0 available to us on the Pi
bus = 0

# Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 1

# Enable SPI
spi = spidev.SpiDev()

# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

# spi = SPI(sck=Pin(12), mosi=Pin(13), miso=Pin(18)) # Configure SPI - note: miso is unused
dots = dotstar.DotStar(spi, 10, brightness=0.5)

# Using a DotStar Digital LED Strip with 30 LEDs connected to SPI
# dots = dotstar.DotStar(spi=SPI(sck=Pin(x), mosi=Pin(y)), 30, brightness=0.2)

# HELPERS
# a random color 0 -> 224
def random_color():
    return random.randrange(0, 7) * 32


# MAIN LOOP
n_dots = len(dots)
while True:
    # Fill each dot with a random color
    for dot in range(n_dots):
        dots[dot] = (random_color(), random_color(), random_color())

    time.sleep(.25)
