import pandas as pd
import os
name = 'stocklist'
a = []
path = os.getcwd()
# 讀取歷史資料檔名列表
indir = path
filename = '/historylist.csv'
fostocklist = pd.read_csv(indir+filename, thousands=',')
win = 0
lose = 0

totalaveprofit = []
# turn days trade
for i in range(0, len(fostocklist)):  #
    stockprofit = []
    hisfilename = fostocklist.iat[i, 0]
    print(hisfilename)
    data = pd.read_csv(path+'/112kdnewhistory/'+hisfilename,
                       thousands=',')  # , index_col=0
    cd = 0

    for x in range(11, len(data)-10):
        list = []
        kd = False
        shadow = False
        # kd三日鈍化_data.at[x, 'k'] > 0.8 and data.at[x-1, 'k'] > 0.8 and data.at[x-2, 'k'] > 0.8 and data.at[x-3, 'k'] < 0.8
        if data.at[x, 'k'] > 0.8 and data.at[x-1, 'k'] > 0.8 and data.at[x-2, 'k'] > 0.8 and data.at[x-3, 'k'] < 0.8:
            kd = True
        # 下影線>4%
        if data.at[x, "開盤價"] > data.at[x, "收盤價"]:
            loshadow = (data.at[x, "收盤價"] -
                        data.at[x, "最低價"]) / data.at[x, "開盤價"]
            # print('綠下影線=', loshadow)
        else:
            loshadow = (data.at[x, "開盤價"] -
                        data.at[x, "最低價"]) / data.at[x, "開盤價"]
            # print('紅下影線=', loshadow)
        if loshadow > 0.03:
            shadow = True

        # 如果購入條件成立
        if shadow == True:
            # print (data.at[x,'日期'],'alert')
            buyprice = data.at[x+1, '開盤價']
        # 賣出條件_漲跌達7%
            d = 0
            while ((data.at[x + d, '收盤價']-buyprice)/buyprice) < 0.1 and ((data.at[x + d, '收盤價']-buyprice)/buyprice) > -0.1 and x+d < len(data)-10:
                d += 1
                # print((len(data)-11), x, d)
                # print(data.at[x + d, '收盤價'])
            saleprice = data.at[x+d+1, '收盤價']
            # 排除因為到資料最後一天賣
            if x+d == (len(data)-10):
                continue

        # 獲利與勝率統計
            tradeprofit = round((saleprice - buyprice) / buyprice * 100, 2)
            if tradeprofit > 0:
                win += 1
            else:
                lose += 1
            stockprofit.append(tradeprofit)
            # profit[j] = round(((data.at[j + 5, '收盤價']) - todayprice),2)# / todayprice) * 100
            print('購買日期與價格=', data.at[x, '日期'], buyprice,
                  ',超過7%的日期=', data.at[x+d, '日期'], '價格與差值=', saleprice, tradeprofit)
            # cd = 10

    aveprofit = sum(stockprofit) / (len(stockprofit) + 0.0001)
    try:
        print('average profit=', aveprofit, 'winning rate=', win/(win+lose))
    except:
        pass
    totalaveprofit.append(aveprofit)

# avetotalprofit = sum(totolaveprofit) / (len(totolaveprofit) + 0.0001)
# print ('total average profit=',aveprofit)
filt = [n for n in totalaveprofit if n < -0.01 or n > 0.01]
# print("==============================\n所有股票收益=", filt)
# print('filt=', filt)
print('==============================\n所有股票平均收益=', sum(filt) / len(filt))


'''
    for j in range(0,len(data)):
        #print (data.at[j,'日期'])
        if data.at[j,'日期']=='2023/01/03':
        #    print (data.at[j, '日期'])
            data.at[j, '日期'] = data.at[j,'日期'].replace(
                '2023/01/03', "112/01/03", 1)
        #    print(data.at[j, '日期'])
    print (data)

    data.to_csv(path + '/20230104/' + hisfilename,
                encoding='utf-8-sig', index_label=0)
    data['filter']=filter
    data.drop(data[data['filter']==True].index,inplace=True)
    print (data)
    data.to_csv(path+'/20230104/'+hisfilename,encoding='utf-8-sig',index_label=0)
    '''
