import matplotlib.pyplot as plt
import numpy as np

from dataHandler import *

states = (read_file('../state_list.txt')[0].split(','))
parties = (read_file('../party_list.txt')[0].split(','))

# initialize
data = []

# Get pre-processed Data
path = '../../pre_proc_data/'

vote_data = []
f_nom_data = []

# Build up array data which contain the percentage of vote getting 
# and the female rate of the nomination of every party
for party_id in range(len(parties)):

    filename = path+parties[party_id]+'_vote_perc.csv' # get percentage of vote getting
    lines = read_file(filename)
    tmp = []
    
    for line in lines[1:]:
        data = [float(n) for n in (line.split(','))[1:]] # store vote_percentage data
        tmp.extend(data)
    vote_data.append(tmp)

    filename = path+parties[party_id]+'_nom_gender.csv' # get the gender of the nomination
    lines = read_file(filename)
    tmp = []
    for line in lines[1:]:
        data = (line.split(','))[1:]
     
        male = float(data[0])  # get the number of male nomination
        female = float(data[1])  # get the number of female nomination
        female_rate = float(female/(male+female))*100 # calculate the percentage of female nomination
        tmp.append(female_rate)
    f_nom_data.append(tmp)


# display the graph for hypothese
output_path = '../../result/hyp1/'
for party_id in range(len(parties)):
    x_axis = range(len(states))
    plt.plot(x_axis, vote_data[party_id], 'b-',label = "vote") 
    plt.plot(x_axis, f_nom_data[party_id], 'g--',label = "female nomination")
    plt.legend(loc="upper left")
    plt.xticks(x_axis, states)
    plt.title('Vote and female candidate Realationship for '+parties[party_id])
    plt.xlabel('State')
    plt.ylabel('Percentage')
    plt.savefig(output_path+parties[party_id]+'.png')
    plt.clf()
