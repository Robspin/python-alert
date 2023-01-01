import os
import yaml
from datetime import datetime
import time


config = yaml.safe_load(open(os.path.dirname(__file__) + '/config.yml'))


def local_time():
    utc_datetime = datetime.now()
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    now_local = utc_datetime + offset
    return now_local.time()


