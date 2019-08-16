import matplotlib.pyplot as plt
import numpy as np

from dataHandler import *
from statsFunc import *

states = (read_file('../state_list.txt')[0].split(',')) # get the list of state
parties = ['ALP','LP']

# Built required Data
path = '../../pre_proc_data/'

vote_data = []
for party_id in range(len(parties)):
    filename = path+parties[party_id]+'_vote_perc.csv' 
    lines = read_file(filename)
    tmp = []
    for line in lines[1:]:
        data = [float(n) for n in (line.split(','))[1:]] # get the percentage of vote getting from the party
        tmp.extend(data)
    vote_data.append(tmp)

file_LF = path+'STATES_LF.csv'
file_POP = path+'STATES_POP.csv'
lf_per_state = []
lf_data = (read_file(file_LF))[1:]  # get the labour force data
pop_data =(read_file(file_POP))[1:] # get population data
for ind in range(len(lf_data)):
    lf = float((lf_data[ind].split(','))[1])   
    tot = float((pop_data[ind].split(','))[1]) 
    lf_rate = (lf/tot)*100      # calculate the percentage of the labour force in a state
    lf_per_state.append(lf_rate)

file_age = path+'STATES_age.csv'
age_per_state = []
age_data = (read_file(file_age))[1:] # get the age data
for ages in age_data:
    age_list = [int(n) for n in (ages.split(','))[1:]]
    skew_val = skewness(age_list)  # calculate the skewness value of age in a state
    age_per_state.append(skew_val)

# display relationship between labour force and vote percentage for parties
output_path = '../../result/hyp3/'
x_axis = range(len(states))
for party_id in range(len(parties)):
    plt.plot(x_axis, vote_data[party_id], 'b--', label = 'vote')
    plt.plot(x_axis, lf_per_state, 'r-', label = 'labour force')
    plt.legend(loc = 'upper right')
    plt.xticks(x_axis,states)
    plt.title(parties[party_id]+'_Vote - Labour_Force')
    plt.xlabel('State')
    plt.ylabel('Percentage')
    plt.savefig(output_path+parties[party_id]+'_vot_LF.png')
    plt.clf()

# display relationship between age and vote percentage for parties
    plt.plot(x_axis, vote_data[party_id], 'b--', label = 'vote')
    plt.plot(x_axis, age_per_state, 'g-', label = 'skew val of age')
    plt.legend(loc = 'upper right')
    plt.xticks(x_axis, states)
    plt.title(parties[party_id]+'_Vote - Age_Skewness')
    plt.xlabel('State')
    plt.savefig(output_path+parties[party_id]+'_vot_age.png')
    plt.clf()

