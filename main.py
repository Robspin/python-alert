import requests
import RPi.GPIO as io
import time

from helpers import config
from buzzer import sound_the_alarm

url = config['status-api']['url']
API_REFRESH_INTERVAL = 60 * 5
LED_RED = 27
LED_BLUE = 22


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
        else:
            sound_the_alarm(2)
            return False


def green_light():
    io.setmode(io.BCM)
    io.setup(LED_RED, io.OUT)
    io.setup(LED_BLUE, io.OUT)
    io.output(LED_RED, False)
    io.output(LED_BLUE, True)
    time.sleep(1)


def red_light():
    io.setmode(io.BCM)
    io.setup(LED_RED, io.OUT)
    io.setup(LED_BLUE, io.OUT)
    io.output(LED_BLUE, False)
    io.output(LED_RED, True)
    time.sleep(1)
    io.output(LED_RED, False)
    time.sleep(1)


try:
    while True:
        timeout = time.time() + API_REFRESH_INTERVAL
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
