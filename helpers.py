import os
import yaml
from datetime import datetime

config = yaml.safe_load(open(os.path.dirname(__file__) + '/config.yml'))


def get_UTC_time():
    utc_datetime = datetime.now()
    now = utc_datetime.time()
    return now.strftime("%H:%M:%S")
