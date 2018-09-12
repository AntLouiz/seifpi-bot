import json
import time
from datetime import datetime, timedelta

def get_schedules():
    with open('seifpi.json', 'r', encoding="utf8") as file:
        data = json.load(file)
        schedules = data['data']['schedule']

    return schedules


def get_time_delta(str_time=time.strftime('%H:%M')):
    date_time = datetime.strptime(str_time, "%H:%M")
    time_delta = timedelta(hours=date_time.hour, minutes=date_time.minute)

    return time_delta

def get_date(str_date=datetime.strftime(datetime.now(), '%Y-%m-%d')):
    return datetime.strptime(str_date, '%Y-%m-%d')
