    #!/usr/bin/env python
    # coding: utf-8
def generate_worksheet(df, engineer, sub, workbook, worksheet):

    import xlsxwriter as xl
    import pandas as pd
    import numpy as np
    import os
    from datetime import datetime
    import procore_formatter


    # In[7]:


    raw = pd.read_csv('submittal_logs.csv')
    df = procore_formatter.formatter(raw)


    # In[4]:


    today = datetime.today()


    # In[ ]:


    text_format = workbook.add_format({
        'font_name' : 'Calibri', 
        'font_size' : 12,
        'align' : 'center',
        'valign' : 'vcenter', 
        'text_wrap' : True
    })

    date_format = workbook.add_format({
        'font_name' : 'Calibri', 
        'font_size' : 12,
        'align' : 'center',
        'valign' : 'vcenter', 
        'text_wrap' : True,
        'num_format' : 'mm/dd/yyyy'
    })

    format_title = workbook.add_format({
        'bold' : True,
        'font_color' : 'white', 
        'bg_color' : '333F4F', 
        'font_name' : 'Calibri',
        'font_size' : 14,
        'border' : 1, 
        'align' : 'center',
        'valign' : 'vcenter',
        'text_wrap' : True
    })


    # In[ ]:


    delta_title = 'Delta at Laguardia\nConcourse F\nTAA# 2732.46\n\nContract Items List'


    delta_format = workbook.add_format({
        'bold' : True,
        'font_color' : 'black', 
        'bg_color' : 'FFCCCC', 
        'font_name' : 'Calibri',
        'font_size' : 16,
        'border' : 2, 
        'align' : 'center',
        'valign' : 'vcenter',
        'text_wrap' : True   
    })


    # In[ ]:


    worksheet.merge_range(0, 0, 7, 5, delta_title, delta_format)


    dated_columns = [7, 8, 9, 10, 11, 12, 15, 16]


    # In[ ]:


    worksheet.set_column(0, 20, None, text_format)
    for i in range(len(dated_columns)):
        worksheet.set_column(i, i, None, date_format) 


    # In[ ]:
    date_format = workbook.add_format({
        'font_color' : 'black', 
        'font_name' : 'Calibri',
        'font_size' : 11,
        'border' : 1, 
        'align' : 'center',
        'valign' : 'vcenter',
        'text_wrap' : True,
         'num_format': 'mm/dd/yyyy'
    })
    
    text_format = workbook.add_format({
    'font_color' : 'black', 
    'font_name' : 'Calibri',
    'font_size' : 11,
    'border' : 1, 
    'align' : 'center',
    'valign' : 'vcenter',
    'text_wrap' : True,
     'num_format': '0.00'
    })

    titles = [['Phase', 7, text_format],
              ['Responsible Subcontractor', 15, text_format],
              ['Spec Section', 12, text_format],
              ['Submittal Number', 13, text_format],
              ['Rev.', 6, text_format], 
              ['PC', 5, text_format], 
              ['Submittal Title', 75, text_format],
              ['Description', 15, text_format],
              ['Ball In Court', 15, text_format],
              ['Received Date', 12.5, date_format],
              ['Submitted Date', 12.5, date_format],
              ['Returned Date', 12.5, date_format], 
              ['Approved Date', 12.5, date_format],
              ['Resubmit Date', 12.5, date_format],
              ['Resubmit Approved Date', 12.5, date_format],
              ['Status', 11, text_format],
              ['Lead Time', 11, text_format],
              ['ROJ Date', 12, date_format], 
              ['Submit By Date', 12.5, date_format],
              ['Response', 20, text_format],
              ['LEED', 11, text_format],
              ['Notes', 30, text_format]]


    # In[ ]:


    worksheet.set_row(8, 56.25)
    for i in range(len(titles)):
        worksheet.write(8, i, titles[i][0], format_title)
        worksheet.set_column(i,i, titles[i][1], titles[i][2])
        
    sub_format = workbook.add_format({
        'bold' : True,
        'font_color' : 'black', 
        'bg_color' : 'D9E1F2', 
        'font_name' : 'Calibri',
        'font_size' : 16,
        'border' : 2, 
        'align' : 'center',
        'valign' : 'vcenter',
        'text_wrap' : True})


    # In[ ]:


    #sub_info = f'{division}{sub}\nCMT Engineer - {engineer}'
    sub_info = f'{sub}\n{engineer}'


    # In[17]:


    worksheet.merge_range(0, 6, 7, 6, sub_info, sub_format)


    # In[18]:


    worksheet.freeze_panes(9, 0)


    # In[19]:


    format1 = workbook.add_format({'bg_color': '#FFC7CE',
                               'font_color': '#9C0006',
                                  'num_format' : 'mm/dd/yyyy'})

    worksheet.conditional_format('S10:S4000', {'type' : 'date',
                                                'criteria' : '<=',
                                                'value' : today,
                                                'format' : format1})

    worksheet.set_column('N:N', None, None, {'hidden': True})
    worksheet.set_column('O:O', None, None, {'hidden': True})
    worksheet.set_column('U:U', None, None, {'hidden': True})

