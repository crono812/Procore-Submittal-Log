#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import datetime as datetime


# In[7]:


def open_submittals(df, location, description):
    status = ['Open', 'Draft', 'Pending']
    
    open_df = df[df['Rev.'] == 0]
    open_df = open_df[open_df['Status'].isin(status) &
                  open_df['Location'].isin(location) &
                  ~open_df['Ball In Court'].str.contains('P022', na = False)]
    
    if description != 'all':
        open_df = open_df[open_df['Type'].isin(description)]
    
    return [open_df, open_df['Status'].count()]


# In[8]:


def closed_submittals(df, location, description):
    status = ['Closed', 'Void', 'Superseded']
    
    close_df = df[df['Status'].isin(status) &
                  df['Location'].isin(location)]
        
    if description != 'all':
        close_df = close_df[close_df['Type'].isin(description)]

    return [close_df, close_df['Status'].count()]   


# In[9]:


def design_team(df, location, description):
    
    dt_df = df[df['Ball In Court'].str.contains('P022', na = False) &
                     df['Response'].str.contains('Pending') &
                     df['Location'].isin(location)]
    
    if description != 'all':
        
        dt_df = dt_df[dt_df['Type'].isin(description)]
        
    return [dt_df, dt_df['Status'].count()]


# In[10]:


def revise_resubmit(df, location, description):
    
    status = ['Open', 'Draft', 'Pending']
    
    open_df = df[df['Rev.'] != 0]
    open_df = open_df[open_df['Status'].isin(status) &
                  open_df['Location'].isin(location) &
                  ~open_df['Ball In Court'].str.contains('P022', na = False)]
    
    if description != 'all':
        open_df = open_df[open_df['Type'].isin(description)]
    
    return [open_df, open_df['Status'].count()]


# df = pd.read_csv('submittal_logs.csv')

# locations = df['Location'].unique()
# location_south = ['Concourse F South Building']
# location_north = np.delete(locations, np.where(locations == location_south))
# print(locations)

# closed = closed_submittals(df, locations, 'all')
# closed[1]

# types = df['Type'].unique()
# 
# closeout = ['As-Built',
#            'Attic Stock',
#            'Certificate of Substantial Completion',
#            'Certificate of Final Completion',
#            'Closeouts',
#            'O&M Manual',
#            'Product Manual',
#            'Record Documents',
#            'Spare Parts List',
#            'Training Material',
#            'Warranty / Guarantee']
# 
# not_closeout = [x for x in types if x not in closeout]
# 

# num_open = open_submittals(df, location_north, not_closeout)
# num_open[1]

# closeout = open_submittals(df, location_north, closeout)
# closeout[1]

# num_open_south = open_submittals(df, location_south, 'all')
# num_open_south[1]

# test = {'open' : ['N/A',1] ,
#        'closed' : 'N/A'}

# test['open'][0] = 1

# test
