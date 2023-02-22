import pandas as pd
import os
name='stocklist'
a=[]
path = os.getcwd()
#讀取歷史資料檔名列表
indir=path
filename='/historylist.csv'
fostocklist=pd.read_csv(indir+filename,thousands=',')

totalaveprofit=[]
#turn days trade
for i in range(0,len(fostocklist)):#
    profit = []
    hisfilename=fostocklist.iat[i,0]
    print (hisfilename)
    data=pd.read_csv(path+'/kdnewhistory/'+hisfilename,thousands=',',index_col=0)
    cd=0
    for x in range(11,len(data)-10):#
        list=[]
        for y in range(0,4):
            list.append(data.at[x - y, 'k'])
        if list[0]>0.8 and list[1]>0.8 and list[2]>0.8 :
            #print (data.at[x,'日期'],'alert')
            if cd<=0:
                dayprofit = round(((data.at[x + 3, '收盤價']) - data.at[x+1, '開盤價']) / data.at[x, '收盤價'] * 100, 2)
                profit.append(dayprofit)
                # profit[j] = round(((data.at[j + 5, '收盤價']) - todayprice),2)# / todayprice) * 100
                print('購買當天=',data.at[x , '日期'],data.at[x , '收盤價'],',3天後=',data.at[x + 3, '收盤價'],'差異=',dayprofit)
                cd=10
        cd=cd-1
    aveprofit = sum(profit) / (len(profit) + 0.0001)
    print('average profit=', aveprofit)
    totalaveprofit.append(aveprofit)
    print (totalaveprofit)
    # avetotalprofit = sum(totolaveprofit) / (len(totolaveprofit) + 0.0001)
# print ('total average profit=',aveprofit)
filt = [n for n in totalaveprofit if n < -0.01 or n > 0.01]
print('filt=',filt)
print(sum(filt) / len(filt))





'''
    for j in range(0,len(data)):
        #print (data.at[j,'日期'])
        if data.at[j,'日期']=='2023/01/03':
        #    print (data.at[j, '日期'])
            data.at[j, '日期'] = data.at[j,'日期'].replace('2023/01/03', "112/01/03", 1)
        #    print(data.at[j, '日期'])
    print (data)

    data.to_csv(path + '/20230104/' + hisfilename, encoding='utf-8-sig', index_label=0)
    data['filter']=filter
    data.drop(data[data['filter']==True].index,inplace=True)
    print (data)
    data.to_csv(path+'/20230104/'+hisfilename,encoding='utf-8-sig',index_label=0)
    '''