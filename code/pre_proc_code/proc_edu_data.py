import matplotlib.pyplot as plt
import numpy as np

from dataHandler import *

###### init data #####
states = (read_file('../state_list.txt')[0].split(','))
list_type = 'STE'
cat_list = ['16A','16B']
sex_list = ['M_','F_']

req_data = []
data_sex_sum = []

# get files name
file_list = []
for state in states:
    file_list.append(getFileList(state,list_type,cat_list))

# setup required columns name
req_col_list = []
part_name = ['Y12e_Tot','Y11e_Tot','Y10e_Tot','Y9e_Tot','Y8b_Tot','DNGTS_Tot']

for sex in sex_list:
    tmp = []
    for name in part_name:
        tmp.append(sex+name)
    req_col_list.append(tmp)

# get required data from database
for state_id in range(len(states)):
    tmp_sex = []
    for sex_id in range(len(sex_list)):
        tmp = []
        for cat_id in range(len(cat_list)):
            pattern = getData(file_list[state_id][cat_id], # file name
                              req_col_list[sex_id],        # list of require column name
                              None,                        # no row check value
                              None)                        # no row check index
            tmp.extend(pattern[0])
        tmp_sex.append(tmp)
    req_data.append(tmp_sex)



# pre-proccess the data of education
for state_id in range(len(req_data)):
    tmp_tot_per_col = []
    tmp_tot_per_col.append(states[state_id])
    for col in range(len(req_data[state_id][0])):
        tot_in_col = 0
        for sex_id in range(len(req_data[state_id])):
            num = int(req_data[state_id][sex_id][col]) # get the value of current column
            tot_in_col = tot_in_col + num              # sum up the total
        tmp_tot_per_col.append(tot_in_col)
    data_sex_sum.append(tmp_tot_per_col)


# write to csv file
fileName = ''
path = '../../pre_proc_data/'
fileName = path+'STATES_edu_by_tot.csv'
part_name.insert(0, 'state')
data_sex_sum.insert(0,part_name)
write_to_csv(data_sex_sum,fileName)

