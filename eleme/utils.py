# -*- coding:utf-8 -*-
import time
import datetime


def date2stamp(date_time):
    """
    :param date_time: datetime
    :return: int timestamp
    """
    time_stamp = int(time.mktime(date_time.timetuple()))
    return time_stamp


def stamp2date(timestamp):
    """
    :param timestamp: int timestamp
    :return: datetime
    """
    date_time = datetime.datetime.utcfromtimestamp(timestamp)
    return date_time