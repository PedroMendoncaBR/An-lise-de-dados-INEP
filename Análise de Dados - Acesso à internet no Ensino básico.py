#!/usr/bin/env python
# coding: utf-8

# # Análise das escolas sem internet no Brasil

# In[33]:


import pandas as pd
import matplotlib.pyplot as plt


# ### Arquivos extraídos para análise

# In[34]:


df_2014 = pd.read_csv ('ESCOLAS-2014.CSV',delimiter = '|', encoding = 'iso-8859-1', usecols = ['ID_INTERNET'])
df_2015 = pd.read_csv ('ESCOLAS-2015.CSV',delimiter = '|', encoding = 'iso-8859-1', usecols = ['IN_INTERNET'])
df_2016 = pd.read_csv ('ESCOLAS-2016.CSV',delimiter = '|', encoding = 'iso-8859-1', usecols = ['IN_INTERNET'])
df_2017 = pd.read_csv ('ESCOLAS-2017.CSV',delimiter = '|', encoding = 'iso-8859-1', usecols = ['IN_INTERNET'])
df_2018 = pd.read_csv ('ESCOLAS-2018.CSV',delimiter = '|', encoding = 'iso-8859-1', usecols = ['IN_INTERNET'])


# In[35]:


internet_2014 = (df_2014.query('ID_INTERNET == 0')['ID_INTERNET'].count())
internet_2015 = (df_2015.query('IN_INTERNET == 0')['IN_INTERNET'].count())
internet_2016 = (df_2016.query('IN_INTERNET == 0')['IN_INTERNET'].count())
internet_2017 = (df_2017.query('IN_INTERNET == 0')['IN_INTERNET'].count())
internet_2018 = (df_2018.query('IN_INTERNET == 0')['IN_INTERNET'].count())


# In[36]:


print(f'Em 2014, {internet_2014} escolas não tinham acesso à internet.')
print(f'Em 2015, {internet_2015} escolas não tinham acesso à internet.')
print(f'Em 2016, {internet_2016} escolas não tinham acesso à internet.')
print(f'Em 2017, {internet_2017} escolas não tinham acesso à internet.')
print(f'Em 2018, {internet_2018} escolas não tinham acesso à internet.')


# ### Variáveis

# In[43]:


x = [2014, 2015, 2016, 2017, 2018]
y = [(internet_2014), (internet_2015), (internet_2016), (internet_2017), (internet_2018)]
a = [2014, 2015, 2016, 2017, 2018]
b = [(internet_2014), (internet_2015), (internet_2016), (internet_2017), (internet_2018)]

plt.title('ESCOLAS SEM ACESSO À INTERNET')
plt.xlabel('ANO')
plt.ylabel('ESCOLAS')
plt.plot(a, b)
plt.bar(x, y, color = 'k')
plt.show()


# In[ ]:




