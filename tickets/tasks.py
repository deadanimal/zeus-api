from __future__ import absolute_import, unicode_literals
from celery import task
from celery.decorators import periodic_task
from celery.task.schedules import crontab

import requests

@periodic_task(run_every=(crontab()), name="check_flespi_galileosky_events", ignore_result=True)
def lol():

    asd = 'Running'
    print(asd)

    link_provided = 'https://webhook.site/2f3532f4-24f1-41e6-952d-b9482ebcd3b1'
    r = requests.get(link_provided)
    
