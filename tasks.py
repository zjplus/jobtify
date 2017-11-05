# tasks.py
import time
import subprocess
from celery import Celery
import config

broker= config.celery_broker
backend = config.celery_backend

celery = Celery('tasks', broker=broker,backend=backend)

def exe_jobs(_cmd_list,_cwd):
	sp = subprocess.run(_cmd_list,stdout=subprocess.PIPE,cwd=_cwd)
	if sp.returncode == 0:
		return True
	else:
		return False

@celery.task
def execute(job):
	return exe_jobs([job["py_env"],job["name"]],job["cwd"])