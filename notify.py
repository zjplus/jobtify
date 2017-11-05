#!/bin/env python
# -*- encoding=utf8 -*-

"""自定义通知函数"""

import functools


def notify(_job_name, _status):
    print(_job_name, _status)


def send_success_mail(mail, this_task_id):
    print(mail, this_task_id)


class NotifyException(Exception):
    '''
    This exception would be handled by send_emails decorator, the decorator will
    catch it and return its value to outer.
    '''

    def __init__(self, value):
        self.value = value
        super(NotifyException, self).__init__(value)


def send_emails(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        this_task_id = args
        email = kwargs.pop('email', False)  # get email and remove it from kwargs
        notify("tesst", True)
        # try:
        #     ret = func(self, *args, **kwargs)
        # except NotifyException as ex:
        #     if email:
        #         send_failure_mail(email, this_task_id)
        #     return ex.value
        # except Exception:
        #     if email:
        #         send_failure_mail(email, this_task_id)
        #     # It would be better to raise again to allow celery knows the task has failed
        #     raise
        # else:
        #     if email:
        #         send_success_mail(mail, this_task_id)
        #     return ret

    return wrapper
