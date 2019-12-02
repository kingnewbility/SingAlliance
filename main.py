import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import os
import sys
sys.path.append(os.getcwd()+"/SingAlliance")
import SingAlliance

# initialization
begin_time=datetime.datetime(2019,11,1,5,0)
end_time=datetime.datetime(2019,11,15,23,0)
period="60min"

# get Kline data from server
BTC_CQ=SingAlliance.Kline_dataframe("BTC_CQ",period,begin_time,end_time)
XRP_CQ=SingAlliance.Kline_dataframe("XRP_CQ",period,begin_time,end_time)
LTC_CQ=SingAlliance.Kline_dataframe("LTC_CQ",period,begin_time,end_time)

# use close price as the price of every minute
df=pd.concat([BTC_CQ['close'],XRP_CQ['close'],LTC_CQ['close']],axis=1)
df.columns=['BTC_CQ','XRP_CQ','LTC_CQ']

# get the weight dict for these three contracts
minimum_variance_weight=SingAlliance.minimum_volatility(df.pct_change())
print("The minimum variance weight vector is: %s"%minimum_variance_weight)

# get the coefficient of efficient frontier function
a,b,c=SingAlliance.EfficientFrontier(df.pct_change())

# plot the efficient frontier
mu_1=np.arange(-0.002,0.005,0.000001)
sigma_2_1=a*mu_1**2+b*mu_1+c
plt.figure(figsize=(10,7))
plt.plot(sigma_2_1,mu_1,color='r')
plt.legend(labelspacing=0.8)
plt.xlabel('hourly volatility (sigma^2)')
plt.ylabel('hourly returns (mu)')
plt.title("Efficient Frontier sigma^2=a*mu^2+b*mu+c")
plt.show()


# example for handling error http msg
BTC_CQ=SingAlliance.Kline_dataframe("BTC_CQ",'0.5min',begin_time,end_time)
