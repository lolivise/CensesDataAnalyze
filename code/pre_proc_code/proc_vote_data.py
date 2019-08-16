import matplotlib.pyplot as plt
import numpy as np

from dataHandler import *

# get the list of states and parties
states = (read_file('../state_list.txt')[0].split(','))
parties = (read_file('../party_list.txt')[0].split(','))

source_path = '../../database/'
fileName = source_path+'HouseFirstPrefsByStateByPartyDownload-20499.csv'

# get data from the base data
data = []
col_chk_ind = [1,0]
req_col_list = ['TotalPercentage']
for party in parties:
    tmp_data = []
    for state in states:
        tmp = []
        tmp_ser = []
        tmp_ser.append(party)
        tmp_ser2 = []
        tmp_ser2.append(state)
        col_chk_list = []
        col_chk_list.append(tmp_ser)
        col_chk_list.append(tmp_ser2)
        
        lines = getData(fileName,
                        req_col_list,
                        col_chk_list,
                        col_chk_ind)
    
        for line in lines:
            tmp.extend(line)
           
        tmp_data.append(tmp)
    
    data.append(tmp_data)

# write data to csv file
path = '../../pre_proc_data/'
req_col_list.insert(0,'state')
for ind in range(len(parties)):
    fileName = path+parties[ind]+'_vote_perc.csv'
    form = []
    form.append(req_col_list)
    for state_id in range(len(states)):
        data[ind][state_id].insert(0,states[state_id])
        form.append(data[ind][state_id])
    write_to_csv(form,fileName)
