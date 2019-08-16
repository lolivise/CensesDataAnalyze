import matplotlib.pyplot as plt
import numpy as np

from dataHandler import *

states = (read_file('../state_list.txt')[0].split(','))
file_type = 'STE'
cat_list = ['43A','43B']
sex_list = ['M_','F_']

# get file name
file_list = []
for state in states:
    file_list.append(getFileList(state,file_type,cat_list))
#print(file_list)

# init data
req_col_list = []
sex_tot_LF = []
sex_tot_pop = []
tot_LF = []
tot_pop = []

# set up required column
for sex in sex_list:
    tmp = []
    tmp.append(sex+'Tot_LF_Tot')
    tmp.append(sex+'Tot_Tot')
    req_col_list.append(tmp)

# generate Data
for state_id in range(len(states)):
    tmp_LF = []
    tmp_pop = []
    for sex_id in range(len(sex_list)):
        tmp = []
        for cat_id in range(len(cat_list)):
            pattern = getData(file_list[state_id][cat_id], # file name
                              req_col_list[sex_id],        # required column name
                              None,                        # no row check value
                              None)                        # no row check index

            tmp.extend(pattern[0])
        tmp_LF.append(tmp[0])
        tmp_pop.append(tmp[1])

    sex_tot_LF.append(tmp_LF)
    sex_tot_pop.append(tmp_pop)

# Sum up
for state_id in range(len(states)):
    tmp_tot_LF = []
    tmp_tot_pop = []
    lf = 0
    pop = 0
    for sex_id in range(len(sex_list)):
        lf = lf + int(sex_tot_LF[state_id][sex_id])
        pop = pop + int(sex_tot_pop[state_id][sex_id])
    tmp_tot_LF.append(lf)
    tmp_tot_pop.append(pop)

    tmp_tot_LF.insert(0,states[state_id])
    tmp_tot_pop.insert(0,states[state_id])

    tot_LF.append(tmp_tot_LF)
    tot_pop.append(tmp_tot_pop)

# write into csv file
label = ['State','M','F']
label_for_total = ['State','ToTal']
path = '../../pre_proc_data/'

fileName = path+'STATES_sex_POP.csv'
for state_id in range(len(states)):
    sex_tot_pop[state_id].insert(0,states[state_id])
sex_tot_pop.insert(0,label)
write_to_csv(sex_tot_pop,fileName)

fileName = path+'STATES_LF.csv'
tot_LF.insert(0,label_for_total)
write_to_csv(tot_LF,fileName)

fileName = path+'STATES_POP.csv'
tot_pop.insert(0,label_for_total)
write_to_csv(tot_pop,fileName)
