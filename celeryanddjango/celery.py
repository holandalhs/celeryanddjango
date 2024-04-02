from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryanddjango.settings')

app = Celery('celeryanddjango')

app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks() ##**Automaticamente descobre e registra tarefas (tasks)
                ##**em diferentes módulos do aplicativo.

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


    