#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime


# In[707]:


df = pd.read_csv(r'C:\Users\Parth\Desktop\downloaded files\may\fo27MAY2020bhav.csv')
df['EXPIRY_DT'] = df['EXPIRY_DT'].astype('datetime64[ns]')


# In[708]:


clean = df.loc[(df['INSTRUMENT'] == 'OPTIDX') & (df['SYMBOL'] == 'BANKNIFTY') & (df['EXPIRY_DT'] == df.EXPIRY_DT.min())]


# In[709]:


main = pd.DataFrame(clean)


# In[710]:


print(main)


# In[711]:


ce = main.loc[(main['OPTION_TYP'] == 'CE')]


# In[712]:


print(ce)


# In[713]:


strike_ce = pd.DataFrame(ce)
print(ce)


# In[714]:


value = 60
index = abs(strike_ce['OPEN'] - value).idxmin()
print(index)
c1 = strike_ce.loc[index]
print(c1)


# In[715]:


value = 50
index2 = abs(strike_ce['OPEN'] - value).idxmin()
print(index2)
c2 = strike_ce.loc[index2]
print(c2)


# In[716]:


value = 40
index3 = abs(strike_ce['OPEN'] - value).idxmin()
print(index3)
c3 = strike_ce.loc[index3]
print(c3)


# In[717]:


value = 30
index4 = abs(strike_ce['OPEN'] - value).idxmin()
print(index4)
c4 = strike_ce.loc[index4]
print(c4)


# In[718]:


value = 20
index5 = abs(strike_ce['OPEN'] - value).idxmin()
print(index5)
c5 = strike_ce.loc[index5]
print(c5)


# In[719]:


value = 10
index6 = abs(strike_ce['OPEN'] - value).idxmin()
print(index6)
c6 = strike_ce.loc[index6]
print(c6)


# In[720]:


pe = main.loc[(main['OPTION_TYP'] == 'PE')]
print(pe)


# In[721]:


strike_pe = pd.DataFrame(pe)


# In[722]:


value = 60
index7 = abs(strike_pe['OPEN'] - value).idxmin()
print(index7)
p1 = strike_pe.loc[index7]
print(p1)


# In[723]:


value = 50
index8 = abs(strike_pe['OPEN'] - value).idxmin()
print(index8)
p2 = strike_pe.loc[index8]
print(p2)


# In[724]:


value = 40
index9 = abs(strike_pe['OPEN'] - value).idxmin()
print(index9)
p3 = strike_pe.loc[index9]
print(p3)


# In[725]:


value = 30
index10 = abs(strike_pe['OPEN'] - value).idxmin()
print(index10)
p4 = strike_pe.loc[index10]
print(p4)


# In[726]:


value = 20
index11 = abs(strike_pe['OPEN'] - value).idxmin
print(index11)
p5 = strike_pe.loc[index11]
print(p5)


# In[727]:


value = 10
index11 = abs(strike_pe['OPEN'] - value).idxmin()
print(index11)
p6 = strike_pe.loc[index11]
print(p6)


# In[728]:


data_ce = []
data_ce.append(c1)
data_ce.append(c2)
data_ce.append(c3)
data_ce.append(c4)
data_ce.append(c5)
data_ce.append(c6)


# In[729]:


print(data_ce)


# In[730]:


data_pe = []
data_pe.append(p1)
data_pe.append(p2)
data_pe.append(p3)
data_pe.append(p4)
data_pe.append(p5)
data_pe.append(p6)


# In[731]:


print(data_pe)


# In[732]:


ce_final = pd.DataFrame(data_ce)


# In[733]:


pe_final = pd.DataFrame(data_pe)


# In[734]:


print(ce_final)


# In[74]:


print(pe_final)


# In[75]:


frames = [ce_final,pe_final]
final = pd.concat(frames)


# In[76]:


print(final)


# In[77]:


final.to_csv(r'C:\Users\Parth\Desktop\strike files\may strike\new_method27may.csv')


# In[78]:


data = pd.read_csv(r'C:\Users\Parth\Desktop\strike files\may strike\new_method27may.csv')


# In[79]:


data['PROFIT'] = data['OPEN'] - data['CLOSE']


# In[80]:


print(data)


# In[90]:


per = data['PROFIT'].sum()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




