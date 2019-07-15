# -*- coding:utf-8 -*-
import time
import datetime
import pandas as pd


def clean_data(file_path):
    """ 对txt内容进行清洗去重 把所需数据拼接成dataframe返回"""

    ori_data = pd.read_csv(file_path, header=None, sep='$')
    count = ori_data.shape[1]
    k = 0
    time_list = []

    data_frame = pd.DataFrame(columns=['restaurant', 'foods', 'price'])

    while k < count:
        k += 1
        try:
            data = eval(ori_data[k][0])[0]
        except:
            continue
        create_time = data['formatted_created_at']
        if create_time in time_list:
            continue
        else:
            time_list.append(create_time)
            foods = data['basket']['group']
            total_amount = data['total_amount']
            restaurant_name = data['restaurant_name']
            food_data = ''
            if len(foods[0]) > 0:
                for i in foods[0]:
                    food_data += i['name'] + ' '

            data_frame.loc[create_time] = [restaurant_name, food_data, total_amount]

    return data_frame


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