import requests
from datetime import datetime
import RPi.GPIO as io
import time

from helpers import config, get_UTC_time
from led import green_light, red_light
from buzzer import sound_the_alarm
from oled import show_stats_on_oled

url = config['status-api']['url']
API_REFRESH_INTERVAL = 60 * 1


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


try:
    while True:
        timeout = time.time() + API_REFRESH_INTERVAL
        result = api_get_statuses()
        time_checked = get_UTC_time()
        while time.time() < timeout:
            if result:
                green_light()
                show_stats_on_oled(time_checked)
            else:
                red_light()
                show_stats_on_oled(time_checked)

except KeyboardInterrupt:
    print("Keyboard interrupt")

except Exception as e:
    print(e)

finally:
    io.cleanup()
