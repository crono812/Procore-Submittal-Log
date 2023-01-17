#!/usr/bin/env python
# coding: utf-8

# In[1]:

def metrics(df, location):
    import pandas as pd
    import numpy as np
    import procore_functions as procore


    closeout = ['As-Built',
               'Attic Stock',
               'Certificate of Substantial Completion',
               'Certificate of Final Completion',
               'Closeouts',
               'O&M Manual',
               'Product Manual',
               'Record Documents',
               'Spare Parts List',
               'Training Material',
               'Warranty / Guarantee']

    types = df['Description'].unique()
    not_closeout = [x for x in types if x not in closeout]
    df['Type'] = df['Description']
    df['Location'] = df['Phase']

    keys = ['open',
           'closeout',
           'pending',
           'revised',
           'leed',
           'closed']

    metrics = dict(zip(keys, [None] * len(keys)))

    # In[22]:


    metrics['open'] = procore.open_submittals(df, location, not_closeout)
    metrics['closeout'] = procore.open_submittals(df, location, closeout)
    metrics['pending'] = procore.design_team(df, location, 'all')
    metrics['revised'] = procore.revise_resubmit(df, location, 'all')
    metrics['leed'] = [0, 0]
    metrics['closed'] = procore.closed_submittals(df, location, 'all')

    return metrics
    
    # In[ ]:





    # In[ ]:




