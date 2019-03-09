# -*- coding: UTF-8 -*-
#!/usr/local/bin/python3
import pandas as pd
import os
pd.set_option('display.max_rows',None)
dirname = os.path.dirname(os.path.realpath(__file__))
x = ['/data/[XIANGCB_BF].[dbo].[CAI_LIST_OLD].csv',
     '/data/[XIANGCB_BF].[dbo].[ORDERS_old].csv']
filename_cai = dirname + x[0]
filename_order = dirname + x[1]


def get_cai(filename):
    print(filename)
    df = pd.read_csv(filename, encoding='gbk',
                     infer_datetime_format=True)
    no_use_col = ['HAS_DADAN','SF_SJ','SFDD_VAR',
                  'JSR_NAME','RNAM_VAR','ZHUOWEI_VAR',
                  'DASK_VAR','PRIN_VAR','SFWF_BIT',
                  'BT_PRICE','CJDW_VAR','FJFY_FLO',
                  'LBXH', 'BT_PRICE','CCSJ_DTE',
                  'CJNUM_FLO','XISHU_INT','EACHDASK_NUM',
                  'DCY_VAR','DC_DTE']
    df.drop(no_use_col,axis=1, inplace=True)
    return df


def get_order(filename):
    print(filename)
    df = pd.read_csv(filename, encoding='gbk',
                 infer_datetime_format=True)
    no_use_col = ['SFYC_VAR', 'CHAJNEW_FLV', 'JFJS_INT',
                  'DYTD_VAR','DDR_USNO','FELV_FLO',
                  'MDST_INT','CAOZ_ZHANDIAN','STATION_ID',
                  'SFJB_BIT','KATOU_VAR','BNAM_VAR',
                  'ZHAO_LIN','RYZX_FLO','GBZX_FLO',
                  'WZX_FLO','MJZX_FLO','GB_XIANGGANG',
                  'MEIJIN_FLO','RIYUAN_FLO','GANGB_FLO',
                  'KAIP_FLO','MIAN_FLO','REAS_FLO',
                  'BEIZ_VAR','FKFS_VAR','FPRT_VAR',
                  'KGBZ_VAR','XIAN_FLO','CANJ_FLO',
                  'ZHIP_FLO','QIAN_FLO','SHUA_FLO',
                  'CHAJ_FLV','CHAJ_FLV','DADAN_NAME',
                  'MDSDR_NAME','ZHEK_BIAOZ','OVIP_FLA',
                  'ZHEK_NAME','ZHEK_JIEBIE','ZHEK_RENID',
                  'FWF_FLV','PDAT_VAR','RMB_FLO',
                  'PRIN_NUM','VINO_VAR','RSTA_VAR',
                  'RSTA_VAR','CANB_VAR','SOXF_FLO',
                  'ZKV_FLO','ZKR_NO','ZKR_NAME',
                  'FALL_FLO','GALL_FLO','SERV_FLO',
                  'CAOZ_NAME','RUSR_VAR']
    df.drop(no_use_col,axis=1, inplace=True)
    return df


cai = get_cai(filename_cai)  # len(df) == 1967292
order = get_order(filename_order) # len(order) == 172199







