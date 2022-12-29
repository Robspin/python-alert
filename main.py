import requests
import RPi.GPIO as io
import time

url = ""


def operational():
    category_statuses = []
    try:
        res = requests.get(url)
        data = res.json()
        for category in data:
            new_list = [service['operational'] for service in  category['statuses']]
            category_statuses = new_list
    except Exception as error:
        print(error)
    finally:
        print(category_statuses)
        print(all(category_statuses))
        if all(category_statuses):
            return True
        return False


io.setmode(io.BCM)
led_red = 27
led_blue = 22
io.setup(led_red, io.OUT)
io.setup(led_blue, io.OUT)

result = operational()


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
        if result:
            green_light()
        else:
            red_light()

except KeyboardInterrupt:
    print("Keyboard interrupt")

except Exception as error:
    print(error)

finally:
    io.cleanup()