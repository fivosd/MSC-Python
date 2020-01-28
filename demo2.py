#!/usr/bin/env python
# coding: utf-8

# In[86]:


import requests
import pandas as pd
import io
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#import numpy as np


# In[87]:





# In[13]:


# the time series function call (EXPAND)
# function access can be granted via menu 
def alpha_vantage(symb,API_KEY):
    link = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=full&apikey={}&datatype=csv'.format(symb,API_KEY)
    rq = requests.get(link)
    urlData = rq.content
    rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    # returns encoded utf-8 CSV format but in a Pandas DataFrame
    return rawData


# In[88]:


def show_plot(ticker,API_KEY):
    data = alpha_vantage(ticker,API_KEY)
    data = data.sort_values(by='timestamp',ascending=True)
    
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data.set_index('timestamp')
    
    plt.plot(data['close'])
    plt.xlabel('Years')
    plt.ylabel('Price ($)')
    plt.title("Stock Price over Time for: "+ticker)
    plt.show()
    
    return 'complete'


# In[92]:


def alpha_query(query,API_KEY):
    link = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={}&apikey={}&datatype=csv'.format(query,API_KEY)
    rq = requests.get(link)
    urlData = rq.content
    rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    # returns encoded utf-8 CSV format but in a Pandas DataFrame
    return rawData


# In[103]:


def query(query,API_KEY):
    query = alpha_query(query,API_KEY).loc[0]
    return query[0]


# In[109]:


def main():
    # calling the Alpha Vantage Key Through the File
    API_KEY = open('API_KEY.txt','r').read()
    #print(API_KEY)
    input_str = input('Input the stock name we want:')
    show_plot(query(input_str,API_KEY),API_KEY)


# In[111]:


main()

