
from pandas import DataFrame


def kd_passavation(data, x):  # kd值三日鈍化判斷
    if data.at[x, 'k'] > 0.8 and data.at[x-1, 'k'] > 0.8 and data.at[x-2, 'k'] > 0.8 and data.at[x-3, 'k'] < 0.8:
        kd = True
    else:
        kd = False
    return kd


def MApass(data, x):
    '''
    123
    '''
    if data.at[x-2, '20MA'] > data.at[x-2, '收盤價'] and data.at[x-1, '20MA'] > data.at[x-1, '收盤價'] and data.at[x, '20MA'] < data.at[x, '收盤價']:
        MApassJ = True
    else:
        MApassJ = False
    return MApassJ


def MAlowsupport(data: DataFrame, x: int):
    '''20MA有支撐'''
    if x < 2:
        return False
    if data.at[x-2, '20MA'] < data.at[x-2, '收盤價'] and data.at[x-1, '20MA'] < data.at[x-1, '收盤價'] and data.at[x, '最低價'] <= data.at[x, '20MA'] < data.at[x, '收盤價']:
        MAlowsupportJ = True
    else:
        MAlowsupportJ = False
    return MAlowsupportJ


def volume_explode(multi: int):
    '''
    curring化的偏函數
    '''
    def volume_explode2(data: DataFrame, x: int):
        ave_volume = data['成交股數'].mean()
        if data.at[x, "成交股數"] > multi*ave_volume:  # 低於平均交易量的1倍
            explode = True
        else:
            explode = False
        return explode
    return volume_explode2
