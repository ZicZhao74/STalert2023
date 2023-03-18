
def kd_passavation(data, x):  # kd值三日鈍化判斷
    if data.at[x, 'k'] > 0.8 and data.at[x-1, 'k'] > 0.8 and data.at[x-2, 'k'] > 0.8 and data.at[x-3, 'k'] < 0.8:
        kd = True
    else:
        kd = False
    return kd
