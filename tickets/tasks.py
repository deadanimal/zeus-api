from __future__ import absolute_import, unicode_literals
from celery import task
from celery.decorators import periodic_task
from celery.task.schedules import crontab



@periodic_task(run_every=(crontab()), name="vehicle_custom_send_data")
def lol():

    asd = 'Running'
    print(asd)

    return asd