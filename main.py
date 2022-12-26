import requests
import RPi.GPIO as io
import time

url = ""

def operational():
    all_operational = False
    try:
        res = requests.get(url)
        all_operational = res.status_code == 200
    except Exception as error:
        print(error)
    finally:
        if all_operational:
            return True
        return False

io.setmode(io.BCM)
led_red = 27
led_blue = 22
io.setup(led_red, io.OUT)
io.setup(led_blue, io.OUT)

result = operational()

try:
    while True:
        if result:
            io.output(led_red, False)
            io.output(led_blue, True)
            time.sleep(1)
        else:
            io.output(led_blue, False)
            io.output(led_red, True)
            time.sleep(1)
            io.output(led_red, False)
            time.sleep(1)

except KeyboardInterrupt:
    print("Keyboard interrupt")

except Exception as error:
    print(error)

finally:
    io.cleanup()
