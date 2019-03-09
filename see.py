# -*- coding: UTF-8 -*-
#!/usr/local/bin/python3
import pandas as pd
import os, sys
pd.set_option('display.max_rows',None)
dirname = os.path.dirname(os.path.realpath(__file__))
x = ['[XIANGCB_BF].[dbo].[CAI_LIST_OLD].csv',
'[XIANGCB_BF].[dbo].[ORDERS_old].csv',
'[XIANGCB_BF].[dbo].[ZUOF_LISTTBL_OLD].csv',
'[XIANGCB_BF].[dbo].[FANT_ZENGSONG].csv']
filename = dirname + '/data/use/' + x[0]
del x

print(filename)
df = pd.read_csv(filename, encoding='gbk', infer_datetime_format=True)
#df = df[:3000]

no_use_col = ['HAS_DADAN','SF_SJ','SFDD_VAR',
              'JSR_NAME','RNAM_VAR','ZHUOWEI_VAR',
              'DASK_VAR','PRIN_VAR','SFWF_BIT',
              'BT_PRICE','CJDW_VAR','FJFY_FLO',
              'LBXH', 'BT_PRICE','CCSJ_DTE']
df.drop(no_use_col,axis=1, inplace=True)
del no_use_col
# df.to_excel('a.xlsx')

col = df.columns
ODNO = df.ODNO_VAR.drop_duplicates() # len(ODNO) == 172183
