# # tasks.py
# import time
# import subprocess
# from celery import Celery
# import config

# job_dict = {}
# broker= config.celery_broker
# backend = config.celery_backend

# celery = Celery('tasks', broker=broker,backend=backend)

# def exe_jobs(_cmd_list,_cwd):
# 	sp = subprocess.run(_cmd_list,stdout=subprocess.PIPE,cwd=_cwd)
# 	if sp.returncode == 0:
# 		return True
# 	else:
# 		return False

# @celery.task
# def execute(job):
# 	celery_job = exe_jobs([job["py_env"],job["name"]],job["cwd"])
# 	return job,result

# @celery.task
# def check_jobs():
# 	if job_dict:
# 		return job_dict
# 	else:
# 		return "nodata",len(job_dict)
# 	# 	for _job,job_name in job_dict.keys():
# 	# 		if _job.ready():
# 	# 			job_dict.pop(_job)
# 	# 			result = _job.get()
# 	# 			notify(job_name,result)
# 	# 			return job_name,result