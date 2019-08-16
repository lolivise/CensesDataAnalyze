import matplotlib.pyplot as plt
import numpy as np

from dataHandler import *

states = (read_file('../state_list.txt')[0].split(','))
file_type = 'STE'
cat_list = ['17A','17B','17C']
sex_list = ['M_','F_']

file_list = []
for state in states:
    file_list.append(getFileList(state,file_type,cat_list))
#print(file_list)

'''
Built personal weekly income data 
'''

# init data
req_col_list = []
req_data = []
income_struc = []

income_ran = [1,150,300,400,500,650,
                800,1000,1250,1500,1750,
                2000,3000]

# set up required columns name list
for sex in sex_list:
    tmp = [sex+'Neg_Nil_income_Tot']
    for ind in range(len(income_ran)):
        if(ind < len(income_ran)-1):
            col_name = sex+str(income_ran[ind])+'_'+str(income_ran[ind+1]-1)+'_Tot'
            tmp.append(col_name)
        else:
            tmp.append(sex+str(income_ran[ind])+'_more_Tot')
    req_col_list.append(tmp)

# Get data by built column name list
for state_id in range(len(states)):
    tmp_sex = []
    for sex_id in range(len(sex_list)):
        tmp = []
        for cat_id in range(len(cat_list)):
            pattern = getData(file_list[state_id][cat_id], # file name  
                                 req_col_list[sex_id],     # required column name
                                 None,                     # no row check value
                                 None)                     # no row check index
            tmp.extend(pattern[0])
        tmp_sex.append(tmp)
    req_data.append(tmp_sex)
      

# Sum up the total people in every income range
for state_id in range(len(states)):
    tmp_tot_per_col = []
    tmp_tot_per_col.append(states[state_id])
    for col in range(len(req_col_list[0])):
        total = 0
        for sex_id in range(len(sex_list)):
            num = int(req_data[state_id][sex_id][col])
            total = total + num
        tmp_tot_per_col.append(total)
    income_struc.append(tmp_tot_per_col)


# write in csv file
label = []
for item in req_col_list[0]:
    label.append(item[2:])

path = '../../pre_proc_data/'
fileName = path+'STATES_income_by_tot.csv'
label.insert(0,'state')
income_struc.insert(0,label)
write_to_csv(income_struc,fileName)
