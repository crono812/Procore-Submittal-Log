#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime
import os


# In[ ]:


df = pd.read_csv('submittal_logs.csv')
df.columns
df['Location'].unique()


# In[5]:


def phase(location):

    location_north = ['Concourse F North Building', 
                      'Temporary Connector',
                       'Temporary Connector>Temporary Corridor',
                       'Concourse F North Building>Temp connector',
                       'Superstructure>Termporary Conn.']

    location_south = ['Concourse F South Building']

    if location in location_north:
        return 'N'
    elif location in location_south:
        return 'S'
    else:
        return 'N/S'


# In[6]:


def pc(spec):
    if 'TC' in spec:
        return 'TC'
    elif 'PT' in spec:
        return 'PT'
    elif 'AS' in spec:
        return 'AS'
    elif 'PFSS' in spec:
        return 'PFSS'
    else:
        return 'CSFO'


# In[7]:


def dis_date(date):
    if len(date) > 4:
        return date[:10]
    else:
        return np.nan


# In[8]:


def clean_date(date):
    if '\n' in date:
        return max(date.split('\n'))

    elif '<br />' in date:
        return max(date.split('<br />'))

    else:
        return date


# In[9]:

def formatter(df):
    
    import pandas as pd
    import numpy as np
    from datetime import datetime
    import os

    dropped_columns = ['Package #', 'Description', 'Cost Code', 'Received From', 'Created At', 'Updated At', 'Final Due Date', 
                      'Issue Date', 'Planned Return Date', 'Design Team Review Time', 'Planned Internal Review Completed Date',
                      'Internal Review Time', 'Anticipated Delivery Date', 'Confirmed Delivery Date', 'Actual Delivery Date',
                      'Planned Submit By Date', 'Approvers', 'Sent Date', 'Reference Drawing:', 'Unnamed: 36', 'Due Date']

    df = df.drop(labels = dropped_columns, axis = 1)


    # In[12]:


    df['PC'] = df['#'].apply(pc)
    df['Phase'] = df['Location'].apply(phase)
    df['Specification'] = df['Spec Section'].astype('str')
    df['Specification'] = df['Specification'].apply(lambda spec: spec[:8])
    df['Submittal Number'] = df['#'].apply(lambda num: num.split('-')[-1])
    df['Distributed Date'] = df['Distributed Date'].astype('str')
    df['Approved Date'] = df['Distributed Date'].apply(dis_date)
    df['Submitted Date'] = 'NaN'
    df['Resubmit Date'] = 'NaN'
    df['Resubmit Approved Date'] = 'NaN'


    # In[14]:


    dates = ['Received Date', 'Required On Site Date', 'Submit By', 'Returned Date']

    for i in range(len(dates)):
        df[dates[i]] = df[dates[i]].astype('str')
        df[dates[i]] = df[dates[i]].apply(clean_date)


    # In[15]:


    rename = {
        'Title' : 'Submittal Title',
        'Type' : 'Description', 
        'Required On Site Date' : 'ROJ Date',
        'Submit By' : 'Submit By Date'
    }

    df = df.rename(columns = rename)


    # In[16]:


    df = df.replace('NaN', np.nan)
    df = df.replace('nan', np.nan)


    # In[19]:


    df.columns


    # In[24]:


    dates = ['Submit By Date', 'Received Date',
             'ROJ Date', 'Returned Date', 'Distributed Date', 
             'Approved Date', 'Submitted Date', 'Resubmit Date', 'Resubmit Approved Date']

    for i in range(len(dates)):
        try:
            df[dates[i]] = pd.to_datetime(df[dates[i]])
        except:
            print(f'Error in {dates[i]}')
    
    
        reorder = [
        'Phase',
        'Responsible Contractor',
        'Specification',
        'Submittal Number',
        'Rev.',
        'PC',
        'Submittal Title',
        'Description',
        'Ball In Court',
        'Received Date',
        'Submitted Date',
        'Returned Date',
        'Approved Date',
        'Resubmit Date',
        'Resubmit Approved Date',
        'Status',
        'Lead Time',
        'ROJ Date',
        'Submit By Date',
        'Response'
    ]
    
    df_reorder = df[reorder]
    
    
    return df_reorder


    # In[ ]:




