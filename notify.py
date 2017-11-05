#!/bin/env python
# -*- encoding=utf8 -*-

"""自定义通知函数"""

import functools


def on_success_notify(*args, **kwargs):
    print(kwargs["ret"])
    print(args, kwargs)


def on_failed_notify(*args, **kwargs):
    print(args, kwargs)


class NotifyException(Exception):
    """
    This exception would be handled by send_emails decorator, the decorator will
    catch it and return its value to outer.

    """

    def __init__(self, value):
        self.value = value
        super(NotifyException, self).__init__(value)


def notify(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            ret = func(self, *args, **kwargs)
        except NotifyException as ex:
            on_failed_notify(*args, **kwargs)
            return ex.value
        except Exception:
            on_failed_notify(*args, **kwargs)
            raise
        else:
            kwargs["ret"] = ret
            on_success_notify(*args, **kwargs)
            return ret

    return wrapper
