#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import time


# In[27]:


def cleaning(df):

    #select the desired columns
    df=df[['pid','yr','age','gender','g_hei','g_wei','g_bmi','g_ssr','drinkornot_96','drinkornot_97','drinkornot_98','drinkornot_17','psick09','psick10','psick11','mdrug07']]
    
    #cleaning each column
    #for numeric data, value out of selected range would be set as -999, null stays null
    #for categorical data, value out of options, including null, would be labeled as Z
    
    #age
    for i in range(len(df)):
        if df.loc[i,'age'] <0 or df.loc[i,'age'] >100:
            df.loc[i,'age']=-999
    
    #gender to category
    for i in range(len(df)):
        if df.loc[i,'gender'] not in [1,2] and df.loc[i,'gender']+1==True:
            df.loc[i,'gender']='Z'

    #g_hei to float with one decimal
    for i in range(len(df)):
        if df.loc[i,'g_hei'] <0 or df.loc[i,'g_hei'] >200:
            df.loc[i,'g_hei']=-999
    df.loc[:,'g_hei']=df.loc[:,'g_hei'].round(1)

    #g_wei to float with one decimal
    for i in range(len(df)):
        if df.loc[i,'g_wei'] <0 or df.loc[i,'g_wei'] >150:
            df.loc[i,'g_wei']=-999
    df.loc[:,'g_wei']=df.loc[:,'g_wei'].round(1)
    
    #g_bmi to float with one decimal
    for i in range(len(df)):
        if df.loc[i,'g_bmi'] <0 or df.loc[i,'g_bmi'] >50:
            df.loc[i,'g_bmi']=-999
    df.loc[:,'g_bmi']=df.loc[:,'g_bmi'].round(1)
    
    #g_ssr to float with one decimal
    for i in range(len(df)):
        if df.loc[i,'g_ssr'] <60 or df.loc[i,'g_ssr'] >300:
            df.loc[i,'g_ssr']=-999
    df.loc[:,'g_ssr']=df.loc[:,'g_ssr'].round(1)

    #combine the 4 different drinkornot, since their choices are quite similar
    df.loc[:,'drinkornot']=df.loc[:,'drinkornot_98'].combine_first(df.loc[:,'drinkornot_97']).combine_first(df.loc[:,'drinkornot_96']).combine_first(df.loc[:,'drinkornot_17'])

    for i in range(len(df)):
        if df.loc[i,'drinkornot'] not in [1,2,3,4,5] and df.loc[i,'drinkornot']+1==True:
            df.loc[i,'drinkornot']='Z'

    #psick09 to category
    for i in range(len(df)):
        if df.loc[i,'psick09'] not in [0,1] and df.loc[i,'psick09']+1==True:
            df.loc[i,'psick09']='Z'

    #psick10 to category
    for i in range(len(df)):
        if df.loc[i,'psick10'] not in [0,1] and df.loc[i,'psick10']+1==True:
            df.loc[i,'psick10']='Z'

    #psick11 to category
    for i in range(len(df)):
        if df.loc[i,'psick11'] not in [0,1] and df.loc[i,'psick11']+1==True:
            df.loc[i,'psick11']='Z'

    #mdrug07 to category
    for i in range(len(df)):
        if df.loc[i,'mdrug07'] not in [0,1] and df.loc[i,'mdrug07']+1==True:
            df.loc[i,'mdrug07']='Z'

    df=df[['pid','yr','age','gender','g_hei','g_wei','g_bmi','g_ssr','drinkornot','psick09','psick10','psick11','mdrug07']]
    
    return df


# In[32]:


def read_me(path,filename,df):
    Info="""
    {filename} is cleaned on {time}, by cleaning_mjdb_v1.py\n
    The data was downloaded from meijao database, including {rows} samples(rows).\n
    {columns} variants(columns) had been selected and cleaned.\n
    
    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n
    
    All null values were kept null.\n
    For numeric data, values out of selected range were set to -999.\n
    For categorical data, values out of selected categories were labeled as Z.\n
    
    "pid" representing "patient id" was kept.\n
    "yr" representing "year" was kept.\n
    "age" representing "patient age" was treated as numeric data, 0 < age <= 100.\n
    "gender" representing "patient gender" was treated as categorical data, (1): male, (2): female.\n
    "g_hei" representing "patient height" was treated as numeric data, 0 < g_hei <= 200.\n
    "g_wei" representing "patient weight" was treated as numeric data, 0 < g_wei <= 150.\n
    "g_bmi" representing "patient bmi" was treated as numeric data, 0 < g_bmi <= 50.\n
    "g_ssr" representing "right hand systolic blood pressure" was treated as numeric data, 60 < g_ssr <= 300.\n
    
    "drinkornot_96" representing "How often do you drink?" was treated as categorical data, (1): never or almost never, (2): has quit alcohol now, (3)sometimes, (4) often, (5) everyday.\n
    "drinkornot_97", "drinkornot_98", "drinkornot_17" all representing "How often do you drink weekly?" were treated as categorical data, (1): never or less than 1, (2): has quit alcohol now, (3)once or twice, (4) 3-4 times, (5) everyday.\n
    The 4 mentioned above were combined to one category "drinkornot" since most of them have similar standard.\n
    
    "psick09" representing "Have you been diagnosed with high blood pressure" was treated as categorical data, (0): no, (1): yes.\n
    "psick10" representing "Have you been diagnosed with diabetes?" was treated as categorical data, (0): no, (1): yes.\n
    "psick11" representing "Have you been diagnosed with stroke?" was treated as categorical data, (0): no, (1): yes.\n
    
    "mdrug07" representing "Have you been taking hyperlipidemia drugs" was treated as categorical data, (0): no, (1): yes.\n
    This column was selected to indicate whether the patient is diagnosed with hyperlipidemia, since the exact question  only exists in the 2017 version.\n
    """.format(filename=filename, time=time.asctime(time.localtime()), rows=len(df), columns=len(df.columns))
    f=open(path+"readme.txt", "w")
    f.write(Info)
    f.close()


# In[33]:


def main(path:str,rawfile:str):
    df=pd.read_csv(path+rawfile,index_col=0)
    df=cleaning(df)
    filename=rawfile[:-8]+'_cleaned.csv'
    df.to_csv(path+filename)
    read_me(path,filename,df)


# In[34]:


path='c:/Users/s9304/downloads/'
rawfile='mjdb_14000_data_raw.csv'


# In[35]:


main(path,rawfile)


# In[ ]:





# In[ ]:





# In[ ]:




