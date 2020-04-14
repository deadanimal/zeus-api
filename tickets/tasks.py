from __future__ import absolute_import, unicode_literals
from celery import task
from celery.decorators import periodic_task
from celery.task.schedules import crontab

from requests


@periodic_task(run_every=(crontab()), name="vehicle_custom_send_data")
def lol():

    asd = 'Running'
    print(asd)

    req = requests.get('https://webhook.site/2f3532f4-24f1-41e6-952d-b9482ebcd3b1')

    return asd