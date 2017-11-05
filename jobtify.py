#!/bin/env python
# -*- encoding=utf8 -*-
import os
import subprocess
import config

import argparse

from celery import Celery

from notify import notify

# 初始化 celery
broker = config.celery_broker
backend = config.celery_backend
celery = Celery('jobtify', broker=broker, backend=backend)


class Job(object):
    def __init__(self, cmd, cwd=os.getcwd()):
        self.cmd = cmd
        self.cwd = cwd

    def to_dict(self):
        res_dict = {
            "cmd": self.cmd,
            "cwd": self.cwd
        }
        return res_dict


class Jobtify(object):
    def __init__(self):
        self.job_dict = dict()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-cmd', action='store', dest='cmd', help='shell command')
        self.parser.add_argument('-dir', action='store', dest='dir', help='work dir')
        self.job = None
        self.args = None

    def parse_args(self):
        self.args = self.parser.parse_args()
        if not self.args.cmd:
            raise KeyError(""" arg cmd is needed """)
        cmd_list = self.args.cmd.split(" ")
        self.job = Job(cmd_list, self.args.dir)

    @staticmethod
    @celery.task
    @notify
    def execute(_job):
        _cmd_list = _job["cmd"]
        _cwd = _job["cwd"]

        sp = subprocess.run(_cmd_list, stdout=subprocess.PIPE, cwd=_cwd)
        if sp.returncode == 0:
            return _job, True
        else:
            return _job, False

    def run(self):
        self.execute.delay(self.job.to_dict())


if __name__ == "__main__":
    try:
        jobtify = Jobtify()
        jobtify.parse_args()
        jobtify.run()
    except Exception as e:
        print(e)

        jobtify.parser.print_help()
        # job = Job("python", "test.py", "/Users/calvin/Project/jobtify")
        # jobtify.execute.delay(job.to_dict())
