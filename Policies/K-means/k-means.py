import pandas as pd
from sklearn.cluster import KMeans

ti_kmeans=[]
## read corresponding table for each dataset
all_tier=pd.read_csv('/Dataset/Airfoil/Msh_3100.csv')

all_tier_f=all_tier
all_tier_f['freq']=0
tier3=all_tier_f[0:50]
tier2=all_tier_f[50:500]
tier1=all_tier_f[500:]
for turn in range(600):
    print('Turn',turn)
    ## read corresponding requests
    req=pd.read_csv('/Datasets/Airfoil/Requests_angl3_0_30/req_%d.csv'%turn)
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
    ti_kmeans.append(ti)
    all_tier_f['label']=-KMeans(n_clusters=100, random_state=0, n_init=10).fit(all_tier_f[['freq','weight']]).labels_    
    tier=all_tier_f.sort_values(by=['freq','label'],ascending=False)
    i3=0
    while tier[0:i3]['weight'].sum() < 1000000:
        i3+=1
    tier3=tier[0:i3-1]

    i2=i3
    while tier[i3-1:i2]['weight'].sum() < 5000000:
        i2+=1
    tier2=tier[i3-1:i2-1]

    tier1=tier[i2-1:]
