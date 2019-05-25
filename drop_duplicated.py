# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:00:09 2019

@author: Zhijie Cao
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

file1 = '201903'
file2 = '201904'
csv = '.csv'

def sumup(filename):
    c04 = pd.read_csv(filename+csv, encoding='gbk')
    c04.drop(['销售单价','分摊优惠', '单卖数量', '套餐内销量',
              '折后金额', '实收'],
             axis=1, inplace=True)
    drop_class = ['手写单', '杂项', '啤酒', '白酒',
                  '红酒', '药酒', '洋酒','香烟', '饮料']
    c04 = c04[~c04['菜类'].isin(drop_class)]
    drop_items = ['消毒餐具','白饭','纸巾']
    c04 = c04[~c04['菜品名称'].isin(drop_items)]
    drop_words = ['\(例\)', '\(例牌\)', '\(中牌\)', '（美团）']
    for x in drop_words:
        c04['菜品名称'] = c04['菜品名称'].str.replace(x, "")
    h04 = c04.groupby('菜品名称').sum()
    h04.sort_values(by='数量', ascending=False, inplace=True)
    h04.to_csv(filename+'+'+csv, float_format='%d')
    
sumup(file1)
sumup(file2)