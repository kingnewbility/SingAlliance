
import pandas as pd
import numpy as np
import datetime
import requests

# Address class to store HTTP address
class Address:
    contract_address="https://api.hbdm.com"
    Kline_http="/market/history/kline"

# error handling method
def ErrorHandling(resp):
    error_code=resp.json()['err-code']
    error_msg=resp.json()['err-msg']
    print(" \nThere is an error when getting data from the server \n erroe code: %s   erroe message: %s\n"%(error_code,error_msg))

# connect server and get row data
def Kline(symbol,period,size=150):
    get_msg=Address.contract_address+Address.Kline_http+"?"+"symbol=%s&period=%s&size=%s"%(symbol,period,size)
    resp=requests.get(get_msg)
    if resp.json()['status']=="ok":
        return resp
    else:
        ErrorHandling(resp)

# select json format data in the given time periods
def Kline_json(symbol,period,begin_time,end_time):
    resp=Kline(symbol,period,2000)
    begin_time=datetime.datetime.timestamp(begin_time)
    end_time=datetime.datetime.timestamp(end_time)
    json_data=resp.json()
    data=[i for i in json_data['data'] if (i['id']>=begin_time)&(i['id']<=end_time)]
    json_data['data']=data
    return json_data

# get the DataFrame format data
def Kline_dataframe(symbol,period,begin_time,end_time):
    json_data=Kline_json(symbol,period,begin_time,end_time)
    df=pd.DataFrame(json_data['data'])
    df['date']=df['id'].apply(lambda x: datetime.datetime.fromtimestamp(x))
    return df

# calculate the weight of given data to get the minimum volatility
def minimum_volatility(dataframe):
    dataframe_cov=dataframe.cov()
    dataframe_cov_inv=np.linalg.inv(dataframe_cov)
    return dict(zip(dataframe.columns,dataframe_cov_inv.sum(axis=1)/dataframe_cov_inv.sum(axis=1).sum()))

# calculate the coefficient of efficient frontier function
# sigma^2=a*mu^2+b*mu+c 
# out put are a, b, c
def EfficientFrontier(dataframe):
    df_cov_inv=np.linalg.inv(dataframe.cov())
    df_return=np.mean(dataframe)
    a=df_cov_inv.sum()
    b=(df_cov_inv@df_return).sum()
    c=(df_return.T@df_cov_inv@df_return).sum()
    delta=a*c-b*b
    return a/delta, b/delta, c/delta,



