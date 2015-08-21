# The token below is for the public project at
# https://rollbar.com/Rollbar/pyrollbar/
# Replace it with your own token.
import rollbar
rollbar.init('92c10f5616944b81a2e6f3c6493a0ec2', 'celerytest')

from celery import Celery
from celery.signals import task_failure


app = Celery('tasks', backend='rpc://', broker='redis://localhost:6379/0')


@task_failure.connect
def handle_task_failure(**kw):
    rollbar.report_exc_info(extra_data=kw)


@app.task
def add(x, y):
    foo = bar
    return x + y
