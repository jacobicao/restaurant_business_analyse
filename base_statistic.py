# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:14:27 2019

@author: Zhijie Cao
"""
import os
import pandas as pd

dirname = os.path.dirname(os.path.realpath(__file__))
x = ['/data/CAI_LIST_OLD.csv',
     '/data/ORDERS_old.csv']
cai = pd.read_csv( dirname + x[0])
order = pd.read_csv(dirname + x[1])

# daily sales
daily_group = order.groupby(pd.Grouper(key='OOPE_TIM', freq='1d'))
daily_orders = daily_group.size()
temp = pd.DataFrame()
temp['order'] = daily_orders.values
temp['year'] = daily_orders.index.year
temp['date'] = pd.to_datetime(
        pd.DataFrame(
                {'month':daily_orders.index.month,
                 'day':daily_orders.index.day,
                 'year':2000}))
daily_orders_matrix = temp.pivot(index='date',
                                 columns='year',values='order')
daily_orders_matrix.plot(style='.-')
daily_orders_matrix.T.mean().plot()


# monthly sales
monthly_group = order.groupby(pd.Grouper(key='OOPE_TIM', freq='1M'))
