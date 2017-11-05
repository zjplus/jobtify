#!/bin/env python
# -*- encoding=utf8 -*-
import os
import time
# from tasks import execute
from notify import send_emails
# from tasks import check_jobs

import subprocess
from celery import Celery
import config

# 初始化 celery
broker = config.celery_broker
backend = config.celery_backend
celery = Celery('jobtify', broker=broker, backend=backend)


class Job(object):
    def __init__(self, env, name, cwd=os.getcwd()):
        self.py_env = env
        self.name = name
        self.cwd = cwd

    def get_dict(self):
        res_dict = {
            "py_env": self.py_env,
            "name": self.name,
            "cwd ": self.cwd
        }
        return res_dict


class Jobtify(object):
    """docstring for Jobtify"""

    def __init__(self):
        self.__cwd__ = os.getcwd()
        self.job_dict = dict()

    def execute_example(self):
        job = Job("python", "test.py", "/Users/calvin/Project/jobtify")
        print("execute 1")
        # job1 = execute.delay([job.py_env, job.name], job.cwd)
        job_name = job.get_dict()
        job1 = execute.delay(job_name)
        print("execute 2")
        job2 = execute.delay(job_name)
        print("execute end")
        self.job_dict[job1.id] = job.name
        self.job_dict[job2.id] = job.name

    @staticmethod
    def exe_jobs(_cmd_list, _cwd=os.getcwd()):
        print(_cmd_list, _cwd)
        sp = subprocess.run(_cmd_list, stdout=subprocess.PIPE, cwd=_cwd)
        if sp.returncode == 0:
            return True
        else:
            return False


jobtify = Jobtify()


@celery.task
@send_emails
def execute(job):
    result = jobtify.exe_jobs([job["py_env"], job["name"]])
    return job, result


if __name__ == "__main__":
    print(jobtify)
    jobtify.execute_example()
