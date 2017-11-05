#!/bin/env python
#-*- encoding=utf8 -*-
import os
from tasks import execute
from notify import notify

__cwd__ = os.getcwd()

if __name__=="__main__":

	job = dict(py_env="python",name="test.py",cwd=__cwd__)
	
	execution = execute.delay(job)
	while True:
		if not execution.ready():
			continue
		break

	result = execution.get()
	notify(job["name"],result)

    # print("__file__=%s" % __file__)
    # print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))
    # print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))
    # print("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])
    # print("os.path.abspath(__file__)=%s" % os.path.abspath(__file__))
    # print("os.getcwd()=%s" % os.getcwd())
    # print("sys.path[0]=%s" % sys.path[0])
    # print("sys.argv[0]=%s" % sys.argv[0])
