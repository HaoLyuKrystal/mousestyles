## Please do it under ../mousestyles/ 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mousestyles import data

intervals_AS=data.load_intervals('AS')
intervals_F=data.load_intervals('F')
intervals_W=data.load_intervals('W')
intervals_IS=data.load_intervals('IS')

## 136 or 137 days totally
days=np.array(intervals_AS.iloc[:,0:3].drop_duplicates().reset_index(drop=True))

## set time range for columns
initial=int(min(intervals_IS['stop']))
end=int(max(intervals_IS['stop']))+1
columns=np.arange(initial,end+1)

## result matrix 
matrix=np.zeros((days.shape[0],len(columns)))


## we set 0 as IS, 1 as F, 2 as W, 3 as Others
for i range(days.shape[0]):
    W=np.array(intervals_W[(intervals_W['strain']==days[i,0])&(intervals_W['mouse']==days[i,1])&(intervals_W['day']==days[i,2])].iloc[:,3:5])
    F=np.array(intervals_F[(intervals_F['strain']==days[i,0])&(intervals_F['mouse']==days[i,1])&(intervals_F['day']==days[i,2])].iloc[:,3:5])
    AS=np.array(intervals_AS[(intervals_AS['strain']==days[i,0])&(intervals_AS['mouse']==days[i,1])&(intervals_AS['day']==days[i,2])].iloc[:,3:5])
    n=W.shape[0]
    index=(np.array(np.where(W[1:,0]-W[0:n-1,1]>4))).ravel()
    stop_W=W[np.append(index,n-1),1]
    start_W=W[np.append(0,index+1),0]
    n=F.shape[0]
    index=(np.array(np.where(F[1:,0]-F[0:n-1,1]>4))).ravel()
    stop_F=F[np.append(index,n-1),1]
    start_F=F[np.append(0,index+1),0]
    n=AS.shape[0]
    index=(np.array(np.where(AS[1:,0]-AS[0:n-1,1]>4))).ravel()
    stop_AS=AS[np.append(index,n-1),1]
    start_AS=AS[np.append(0,index+1),0]
    for j in range(len(columns)):
        if sum(np.logical_and(columns[j]>start_AS, columns[j]<stop_AS))!=0:
            if sum(np.logical_and(columns[j]>start_F, columns[j]<stop_F))!=0:
                matrix[i,j]=1 ## food
            elif sum(np.logical_and(columns[j]>start_W, columns[j]<stop_W))!=0:
                matrix[i,j]=2 ## water
            else:
                matrix[i,j]=3 ## others
    print(i) ## give you which days has been processed

## format data frame
matrix=pd.DataFrame(matrix,columns=columns)
title=pd.DataFrame(days,columns=['strain','mouse','day'])
time=pd.concat([title,matrix],axis=1)