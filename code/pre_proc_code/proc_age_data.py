import matplotlib.pyplot as plt
import numpy as np

from dataHandler import *


# init data 
states = (read_file('../state_list.txt')[0].split(','))
list_type = 'STE'
cat_list = ['04A','04B']

req_data = []

# get file name
file_list = []
for state in states:
    file_list.append(getFileList(state,list_type,cat_list))


# get required columns name
req_col_list = []
for age in range(18,80,1):
    col_name = 'Age_yr_'+str(age)+'_P'
    req_col_list.append(col_name)

for state_id in range(len(states)):
    tmp = []
    tmp.append(states[state_id])
    for cat_id in range(len(cat_list)):
        pattern = getData(file_list[state_id][cat_id], # file name
                          req_col_list,                # required column list
                          None,                        # no row check value
                          None)                        # no row check index
        tmp.extend(pattern[0])
    req_data.append(tmp)


# write to csv file
path = '../../pre_proc_data/'
fileName = path+'STATES_age.csv'

req_col_list.insert(0,'state')
req_data.insert(0,req_col_list)

write_to_csv(req_data,fileName)

