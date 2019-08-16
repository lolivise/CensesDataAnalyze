import matplotlib.pyplot as plt
import numpy as np

from dataHandler import *

states = (read_file('../state_list.txt')[0].split(','))
parties = (read_file('../party_list.txt')[0].split(','))
sex_list = ['Males','Females']

source_path = '../../database/'
fileName = source_path+'HouseNominationsByGenderDownload-20499.csv'

req_data = []

col_chk_ind = [0]
req_col_list = []
for state in states:
    for sex in sex_list:
        req_col_list.append(sex+state)

#print(req_col_list)
for party in parties:
    tmp_nom_state = []
    tmp_ser = []
    tmp_ser.append(party)
    col_chk_list =[]
    col_chk_list.append(tmp_ser)
    lines = getData(fileName,          # file name
                    req_col_list,      # required column name
                    col_chk_list,      # set value of row checking
                    col_chk_ind)       # set index of row checking

    for item_id in range(0,len(lines[0]),2):
        tmp = []
        state_name = states[int(item_id/2)]
        tmp.append(state_name)
        tmp.append(lines[0][item_id])
        tmp.append(lines[0][item_id+1])
        tmp_nom_state.append(tmp)
    req_data.append(tmp_nom_state)

# write to csv
output_path = '../../pre_proc_data/'
label = ['state']
label.extend(sex_list)
for party_id in range(len(parties)):
    fileName = output_path+parties[party_id]+'_nom_gender.csv'
    req_data[party_id].insert(0,label)
    write_to_csv(req_data[party_id],fileName)
