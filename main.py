import requests
import RPi.GPIO as io
import time

url = ""

io.setmode(io.BCM)
led_red = 27
led_blue = 22
io.setup(led_red, io.OUT)
io.setup(led_blue, io.OUT)


def api_get_statuses():
    category_statuses = []
    try:
        res = requests.get(url)
        data = res.json()
        for category in data:
            services_statuses = [service['operational'] for service in category['statuses']]
            category_statuses = category_statuses + services_statuses
    except Exception as e:
        print(e)
    finally:
        if all(category_statuses):
            return True
        return False


def green_light():
    io.output(led_red, False)
    io.output(led_blue, True)
    time.sleep(1)


def red_light():
    io.output(led_blue, False)
    io.output(led_red, True)
    time.sleep(1)
    io.output(led_red, False)
    time.sleep(1)


try:
    while True:
        timeout = time.time() + 60 * 5
        result = api_get_statuses()
        while time.time() < timeout:
            if result:
                green_light()
            else:
                red_light()

except KeyboardInterrupt:
    print("Keyboard interrupt")

except Exception as e:
    print(e)

finally:
    io.cleanup()
