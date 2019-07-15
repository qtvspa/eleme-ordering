# -*- coding:utf-8 -*-

""" 获取订单信息（含重复内容）
    存入txt """

import ssl
import datetime
from urllib import request
from eleme.utils import date2stamp
from eleme.conf import headers, user_id


def get_res(target_url):

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

        url = f'https://h5.ele.me/restapi/bos/v2/users/{user_id}/old_orders?limit=3&from_time={start_stamp}'
        data = get_res(url)
        with open('ele_0715.txt', 'a+') as f:
            f.writelines(str(data)+'$')
        print(data)
        start_stamp += 86400