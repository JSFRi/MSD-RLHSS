import pandas as pd

all_tier=pd.read_csv('/Datasets/Airfoil/Msh_3100.csv')

ti_lfu=[]
all_tier_f=all_tier
all_tier_f['freq']=0
tier3=all_tier_f[0:0]
tier2=all_tier_f[0:0]
tier1=all_tier_f[0:]
for turn in range(600):
    req=pd.read_csv('/Datasets/Airfoil/Requests_angle_0_30/req_%d.csv'%turn)
    req_1=req.loc[req['request']==1]
    all_tier_f.loc[all_tier_f['No.'].isin(req_1['No.']),'freq']+=1
    ti=0
    for no in req_1['No.']:
        if no in list(tier3['No.']):
            ti+=tier3.loc[tier3['No.']==no,'weight'].item()/100000
        elif no in list(tier2['No.']):
            ti+=tier2.loc[tier2['No.']==no,'weight'].item()/50000
        elif no in list(tier1['No.']):
            ti+=tier1.loc[tier1['No.']==no,'weight'].item()/10000
        else:
            print('Error: no such file in tier3/2/1')
    ti_lfu.append(ti)
    tier=all_tier_f.sort_values(by='freq',ascending=False)
    i3=0
    while tier[0:i3]['weight'].sum() < 1000000:
        i3+=1
    tier3=tier[0:i3-1]
    #print(tier3['weight'].sum())
    i2=i3
    while tier[i3-1:i2]['weight'].sum() < 5000000:
        i2+=1
    tier2=tier[i3-1:i2-1]
    #print(tier2['weight'].sum())
    tier1=tier[i2-1:]
