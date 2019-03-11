# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:14:27 2019

@author: Zhijie Cao
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig = 'fig/'
high = 6
width = 8
dpi = 175


def get_cai_order():
    dirname = os.path.dirname(os.path.realpath(__file__))
    x = ['/data/cai.csv',
         '/data/order.csv']
    cai = pd.read_csv(dirname + x[0])
    cai['DCY_DTIM'] = pd.to_datetime(cai['DCY_DTIM'])
    order = pd.read_csv(dirname + x[1])
    order['OOPE_TIM'] = pd.to_datetime(order['OOPE_TIM'])
    order['OPAY_TIM'] = pd.to_datetime(order['OPAY_TIM'])
    order['year'] = pd.Index(order.OOPE_TIM).year
    order['dayofweek'] = pd.Index(order.OOPE_TIM).dayofweek + 1
    return cai,order


## daily

def plot_daily_orders(daily_group,year):
    daily_orders = daily_group.size()
    if year is not None:
        plt.figure(figsize=(width, high), dpi=dpi)
        daily_orders[str(year)].plot(style='o-',linewidth=1.0)
        plt.tight_layout(pad=2)
        plt.title(str(year)+'年每日订单量')
        plt.xlabel('日期')
        plt.ylabel('订单量')
        plt.savefig(fig + str(year) + '年每日订单量.png')
        plt.close()
        return
    temp = pd.DataFrame()
    temp['order'] = daily_orders.values
    temp['year'] = daily_orders.index.year
    temp['date'] = pd.to_datetime(
            pd.DataFrame(
                    {'month':daily_orders.index.month,
                     'day':daily_orders.index.day,
                     'year':2000}))
    daily_orders_matrix = temp.pivot(index='date',
                                     columns='year',
                                     values='order')
    plt.figure(figsize=(width, high), dpi=dpi)
    daily_orders_matrix.T.mean().plot(style='o-',linewidth=1.0)
    plt.tight_layout(pad=2)
    plt.title('日均订单量')
    plt.xlabel('日期')
    plt.ylabel('订单量')
    plt.savefig(fig + '日均订单量.png')
    plt.close()


def plot_daily_sales_mean(daily_group, year):
    daily_sales = daily_group.OPAY_FLO.sum()
    if year is not None:
        plt.figure(figsize=(width, high), dpi=dpi)
        daily_sales[str(year)].plot(style='o-',linewidth=1.0)
        plt.tight_layout(pad=2)
        plt.title(str(year)+'年每日营业额')
        plt.xlabel('日期')
        plt.ylabel('营业额')
        plt.savefig(fig + str(year) + '年每日营业额.png')
        plt.close()
        return
    temp = pd.DataFrame()
    temp['order'] = daily_sales.values
    temp['year'] = daily_sales.index.year
    temp['date'] = pd.to_datetime(
            pd.DataFrame(
                    {'month':daily_sales.index.month,
                     'day':daily_sales.index.day,
                     'year':2000}))
    daily_orders_matrix = temp.pivot(index='date',
                                     columns='year',
                                     values='order')
    plt.figure(figsize=(width, high), dpi=dpi)
    daily_orders_matrix.T.mean().plot(style='o-',linewidth=1.0)
    plt.tight_layout(pad=2)
    plt.title('日均营业额')
    plt.xlabel('日期')
    plt.ylabel('营业额')
    plt.savefig(fig + '日均营业额.png')
    plt.close()
    
    
def plot_order_open_time(order):
    pass
    

## monthly
    
def plot_monthly_sales(monthly_group):
    monthly_sales = monthly_group.OPAY_FLO.sum()/10000
    plt.figure(figsize=(width, high), dpi=dpi)
    monthly_sales[1:-1].plot(style='o-',linewidth=1.0)
    plt.hlines(80,monthly_sales.index[0],
               monthly_sales.index[-1],'r')
    plt.tight_layout(pad=2)
    plt.title('月营业额')
    plt.xlabel('日期')
    plt.ylabel('营业额(万)')
    plt.savefig(fig + '月营业额.png')
    plt.close()
    

def plot_monthly_orders(monthly_group):
    monthly_orders = monthly_group.size()
    plt.figure(figsize=(width, high), dpi=dpi)
    monthly_orders[1:-1].plot(style='o-',linewidth=1.0)
    plt.hlines(1300,monthly_orders.index[0],
               monthly_orders.index[-1],'r')
    plt.tight_layout(pad=2)
    plt.title('月订单量')
    plt.xlabel('日期')
    plt.ylabel('订单量')
    plt.savefig(fig + '月订单量.png')
    plt.close()


def plot_weekly_sales(order):
    year_week = order.groupby(['year','dayofweek'])
    a = year_week.OPAY_FLO.sum()
    b = year_week.OOPE_TIM.agg(
            lambda x: len(
                    pd.Series(pd.Index(x).date).drop_duplicates()))
    c = (a/b).unstack()
    c[:-1].plot.bar(figsize=(width, high))
    plt.tight_layout(pad=2)
    plt.title('周1~周7：日均营业额')
    plt.xlabel('')
    plt.ylabel('营业额')
    plt.legend('一二三四五六日')
    plt.savefig(fig + '周1~周7的日均营业额.png')
    plt.close()


if __name__ == "__main__":
    pass
#    cai, order = get_cai_order()
#    daily_group = order.groupby(
#            pd.Grouper(key='OOPE_TIM',freq='1d'))
#    monthly_group = order.groupby(
#            pd.Grouper(key='OOPE_TIM', freq='1m'))
    
    # 日均订单量
#    plot_daily_orders(daily_group,2018)
    
    # 日均营业额
#    plot_daily_sales_mean(daily_group,2018)
    
    #月营业额
#    plot_monthly_sales(monthly_group)
    
    # 月订单量
#    plot_monthly_orders(monthly_group)
    
    # 周1~周7的日均营业额
#    plot_weekly_sales(order)
    
    
    
    
    
    