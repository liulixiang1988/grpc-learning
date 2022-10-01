from collections import namedtuple
from datetime import datetime, timedelta
from time import sleep

LocationEvent = namedtuple("LocationEvent", 'car_id time lat lng')

def rnd_event(count):
    time = datetime.now()
    lat, lng = 51.4871871, -0.1266743
    for _ in range(count):
        yield LocationEvent(7, time, lat, lng)
    time += timedelta(seconds=17.3)
    lat += 0.0001
    lng -= 0.0001
    sleep(0.1)
    