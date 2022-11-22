import time

from celery import Celery, current_task, Task
from celery.schedules import crontab
from datetime import timedelta
from os import environ

# celery_app = Celery('celery_app', broker='redis://127.0.0.1:6379/0',
#                     backend='redis://127.0.0.1:6379/1')

BROKER_URL = environ.get('BROKER_URL', 'redis://redis:6379/0')
RESULT_BACKEND = environ.get('RESULT_BACKEND', 'redis://redis:6379/1')
# print('----------------------------------')
# print(BROKER_URL)
# print(RESULT_BACKEND)
# print('----------------------------------')

celery_app = Celery('celery_app', broker=BROKER_URL,
                    backend=RESULT_BACKEND)

celery_app.conf.timezone = 'Asia/Taipei'
celery_app.conf.enable_utc = False

celery_app.conf.beat_schedule = {
    # 'crontab_test': {
    #     'task': 'tasks.crontab_test',
    #     'schedule': timedelta(seconds=5, minutes=0, hours=0),
    # },
    'zero_oclock': {
        'task': 'tasks.zero_oclock',
        'schedule': crontab(minute=0, hour=0),
    },
    'one_oclock': {
        'task': 'tasks.one_oclock',
        'schedule': crontab(minute=0, hour=1),
    },
    'two_oclock': {
        'task': 'tasks.two_oclock',
        'schedule': crontab(minute=0, hour=2),
    },
    'three_oclock': {
        'task': 'tasks.three_oclock',
        'schedule': crontab(minute=0, hour=3),
    },
    'four_oclock': {
        'task': 'tasks.four_oclock',
        'schedule': crontab(minute=0, hour=4),
    },
    'five_oclock': {
        'task': 'tasks.five_oclock',
        'schedule': crontab(minute=0, hour=5),
    },
    'six_oclock': {
        'task': 'tasks.six_oclock',
        'schedule': crontab(minute=0, hour=6),
    },
    'seven_oclock': {
        'task': 'tasks.seven_oclock',
        'schedule': crontab(minute=0, hour=7),
    },
    'eight_oclock': {
        'task': 'tasks.eight_oclock',
        'schedule': crontab(minute=0, hour=8),
    },
    'nine_oclock': {
        'task': 'tasks.nine_oclock',
        'schedule': crontab(minute=0, hour=9),
    },
    'ten_oclock': {
        'task': 'tasks.ten_oclock',
        'schedule': crontab(minute=0, hour=10),
    },
    'eleven_oclock': {
        'task': 'tasks.eleven_oclock',
        'schedule': crontab(minute=0, hour=11),
    },
    'twelve_oclock': {
        'task': 'tasks.twelve_oclock',
        'schedule': crontab(minute=0, hour=12),
    },
    'thirteen_oclock': {
        'task': 'tasks.thirteen_oclock',
        'schedule': crontab(minute=0, hour=13),
    },
    'fourteen_oclock': {
        'task': 'tasks.fourteen_oclock',
        'schedule': crontab(minute=0, hour=14),
    },
    'fifteen_oclock': {
        'task': 'tasks.fifteen_oclock',
        'schedule': crontab(minute=0, hour=15),
    },
    'sixteen_oclock': {
        'task': 'tasks.sixteen_oclock',
        'schedule': crontab(minute=0, hour=16),
    },
    'seventeen_oclock': {
        'task': 'tasks.seventeen_oclock',
        'schedule': crontab(minute=0, hour=17),
    },
    'eighteen_oclock': {
        'task': 'tasks.eighteen_oclock',
        'schedule': crontab(minute=0, hour=18),
    },
    'nineteen_oclock': {
        'task': 'tasks.nineteen_oclock',
        'schedule': crontab(minute=0, hour=19),
    },
    'twenty_oclock': {
        'task': 'tasks.twenty_oclock',
        'schedule': crontab(minute=0, hour=20),
    },
    'twenty_one_oclock': {
        'task': 'tasks.twenty_one_oclock',
        'schedule': crontab(minute=0, hour=21),
    },
    'twenty_two_oclock': {
        'task': 'tasks.twenty_two_oclock',
        'schedule': crontab(minute=0, hour=22),
    },
    'twenty_three_oclock': {
        'task': 'tasks.twenty_three_oclock',
        'schedule': crontab(minute=0, hour=23),
    },
}


@celery_app.task()
def add(x, y):
    for i in range(1, 101):
        time.sleep(0.1)
        current_task.update_state(state='PROGRESS',
                                  meta={
                                      'current': i, 'total': 100
                                  })
        print("進度：{0}/{1}".format(i, 100))
    print("計算完成")
    return x + y


class subtration(Task):
    def run(self, x, y):
        for i in range(1, 101):
            time.sleep(0.1)
            current_task.update_state(state='PROGRESS',
                                      meta={
                                          'current': i, 'total': 100
                                      })
            print("進度：{sec}/{total}".format(sec=i, total=100))
        print("計算完成")
        return x - y


subtract = celery_app.register_task(subtration())


@celery_app.task()
def crontab_test():
    output = "歡迎使用定時任務系統"
    return output


@celery_app.task()
def zero_oclock():
    output = "現在時間=>00:00"
    return output


@celery_app.task()
def one_oclock():
    output = "現在時間=>01:00"
    return output


@celery_app.task()
def two_oclock():
    output = "現在時間=>02:00"
    return output


@celery_app.task()
def three_oclock():
    output = "現在時間=>03:00"
    return output


@celery_app.task()
def four_oclock():
    output = "現在時間=>04:00"
    return output


@celery_app.task()
def five_oclock():
    output = "現在時間=>05:00"
    return output


@celery_app.task()
def six_oclock():
    output = "現在時間=>06:00"
    return output


@celery_app.task()
def seven_oclock():
    output = "現在時間=>07:00"
    return output


@celery_app.task()
def eight_oclock():
    output = "現在時間=>08:00"
    return output


@celery_app.task()
def nine_oclock():
    output = "現在時間=>09:00"
    return output


@celery_app.task()
def ten_oclock():
    output = "現在時間=>10:00"
    return output


@celery_app.task()
def eleven_oclock():
    output = "現在時間=>11:00"
    return output


@celery_app.task()
def twelve_oclock():
    output = "現在時間=>12:00"
    return output


@celery_app.task()
def thirteen_oclock():
    output = "現在時間=>13:00"
    return output


@celery_app.task()
def fourteen_oclock():
    output = "現在時間=>14:00"
    return output


@celery_app.task()
def fifteen_oclock():
    output = "現在時間=>15:00"
    return output


@celery_app.task()
def sixteen_oclock():
    output = "現在時間=>16:00"
    return output


@celery_app.task()
def seventeen_oclock():
    output = "現在時間=>17:00"
    return output


@celery_app.task()
def eighteen_oclock():
    output = "現在時間=>18:00"
    return output


@celery_app.task()
def nineteen_oclock():
    output = "現在時間=>19:00"
    return output


@celery_app.task()
def twenty_oclock():
    output = "現在時間=>20:00"
    return output


@celery_app.task()
def twenty_one_oclock():
    output = "現在時間=>21:00"
    return output


@celery_app.task()
def twenty_two_oclock():
    output = "現在時間=>22:00"
    return output


@celery_app.task()
def twenty_three_oclock():
    output = "現在時間=>23:00"
    return output
