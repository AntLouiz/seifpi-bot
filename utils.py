import json
import time
from datetime import datetime, timedelta

def get_schedules():
    with open('seifpi.json', 'r', encoding="utf8") as file:
        data = json.load(file)
        schedules = data['data']['schedule']

    return schedules


def get_now_schedules():
    schedules = get_schedules()
    delta_now = get_time_delta()
    date_now = get_date()
    now_schedules = []

    for schedule in schedules:
        schedule_date = get_date(schedule['date'])
        start_delta = get_time_delta(schedule['start'])
        end_delta = get_time_delta(schedule['end'])

        if (delta_now >= start_delta) and (delta_now <= end_delta) and date_now == schedule_date:
            now_schedules.append(schedule)

    return now_schedules


def get_tasks():
    with open('seifpi.json', 'r', encoding="utf8") as file:
        data = json.load(file)
        tasks = data['data']['task']

    return tasks

def get_task_by_id(task_id):
    pass

def get_workshops():
    with open('seifpi.json', 'r', encoding="utf8") as file:
        data = json.load(file)
        workshop = data['data']['workshop']

    return workshop

def get_workshop_by_id(workshop_id):
    pass

def get_minicourses():
    with open('seifpi.json', 'r', encoding="utf8") as file:
        data = json.load(file)
        minicourses = data['data']['minicourse']

    return minicourses

def get_minicouse_by_id(minicourse_id):
    pass

def get_schedule_data(schedule_id, schedule_type):
    if schedule_type == 'task':
        data = get_tasks()

    elif schedule_type == 'schedule':
        data = get_schedules()

    elif schedule_type == 'workshop':
        data = get_workshops()

    elif schedule_type == 'minicourse':
        data = get_minicourses()

    else:
        data = None

    if data:
        for d in data:
            if d['id'] == schedule_id:
                return d

    return data

def get_schedule_description(schedules):
    data = None

    for schedule in schedules:
        if schedule['activity_id'] == activity_id and schedule['type'] == activity_type:
            data = get_schedule_data(schedule['activity_id'], schedule['type'])

    return data


def get_time_delta(str_time=time.strftime('%H:%M')):
    date_time = datetime.strptime(str_time, "%H:%M")
    time_delta = timedelta(hours=date_time.hour, minutes=date_time.minute)

    return time_delta

def get_date(str_date=datetime.strftime(datetime.now(), '%Y-%m-%d')):
    return datetime.strptime(str_date, '%Y-%m-%d')
