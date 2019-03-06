# -*- coding: UTF-8 -*-
#!/usr/local/bin/python3
import pandas as pd
import os,sys
pd.set_option('display.max_rows',None)
dirname = os.path.dirname(os.path.realpath(__file__))
x = ['[XIANGCB_BF].[dbo].[CAI_LIST_OLD].csv',
'[XIANGCB_BF].[dbo].[ORDERS_old].csv',
'[XIANGCB_BF].[dbo].[ZUOF_LISTTBL_OLD].csv',
'[XIANGCB_BF].[dbo].[FANT_ZENGSONG].csv']
filename = dirname + '/XIANGCB_BF/' + x[0]

print(filename)
df = pd.read_csv(filename, encoding='gbk')
df[:200].to_csv('a.csv')