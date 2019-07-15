# -*- coding:utf-8 -*-

import pandas as pd


if __name__ == '__main__':

    data_frame = pd.read_csv('ele.txt', header=None, sep='$')
    count = data_frame.shape[1]
    restaurant_dict = {}
    k = 0
    time_list = []
    cost = 0

    while k < count:
        k += 1
        try:
            data = eval(data_frame[k][0])[0]
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
            if restaurant_name in restaurant_dict:
                restaurant_dict[restaurant_name] += 1
            else:
                restaurant_dict[restaurant_name] = 1

            food_data = ''
            if len(foods[0]) > 0:
                for i in foods[0]:
                    food_data += i['name'] + ' '
            cost += total_amount
            print_data = f'此用户于{create_time}在{restaurant_name}点了{food_data} 共花费{total_amount}元'
            # print(print_data)


    print(f'此用户过去一年 在饿了么一点过{len(restaurant_dict)}家的外卖 累计共{count}次 共消费{round(cost, 2)}元\n各商家点餐次数明细如下\n')
    for i in sorted(restaurant_dict.items(), key=lambda x: x[1], reverse=True):
        print(i[0], i[1], '次')
