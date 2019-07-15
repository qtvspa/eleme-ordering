# -*- coding:utf-8 -*-

import ssl
import datetime
from urllib import request
from eleme.utils import date2stamp


def get_res(target_url):

    headers = {'此处填写自己的cookie和user-agent等信息'}
    context = ssl._create_unverified_context()
    req = request.Request(url=target_url, headers=headers)
    res = request.urlopen(req, context=context)

    result = str(res.read(), 'utf-8')
    return eval(result)['orders']


if __name__ == '__main__':

    start_time = datetime.datetime.strptime('2018-08-01', '%Y-%m-%d')
    end_time = datetime.datetime.strptime('2019-07-10', '%Y-%m-%d')
    start_stamp = date2stamp(start_time)
    end_stamp = date2stamp(end_time)

    while start_stamp < end_stamp:

        user_id = 123456789 # 个人用户id
        url = f'https://h5.ele.me/restapi/bos/v2/users/{user_id}/old_orders?limit=3&from_time={start_stamp}'
        data = get_res(url)
        with open('ele_0715.txt', 'a+') as f:
            f.writelines(str(data)+'$')
        print(data)
        start_stamp += 86400