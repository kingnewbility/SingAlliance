# SingAlliance

The purpose of this repo is to encapsulate the API of Huobi and do a simple mean-variance optimization of three contracts: BTC 1227, XRP 1227, LTC 1227.

The SingAlliance.py in SingAlliance folder is the encapsulated module, and it can connect with Huobi server and download, parses, and processes relative data.

The main.py is the entrance of the project and where we import and use the SingAlliance module, the minimum variance weight vector of the given data is {'BTC_CQ': 0.7480248696535629, 'XRP_CQ': 0.38514762842752326, 'LTC_CQ': -0.1331724980810862}

The Efficient Frontier is a parabola of portfolio's return and volatility, and for the given data: sigma^2=a*mu^2+b*mu+c 
where a=239.5, b=-0.07, c=3.9e-5

Since limited time, the code and fig are just for illustration purpose, and the real code and document should be more user-friendly.

