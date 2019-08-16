import matplotlib.pyplot as plt
import numpy as np
import math
from dataHandler import *
from statsFunc import *
import statistics

# get the data of states and return the skewness of data of states 
def convert_list(data):
    return_states_skew = []
    for line in data:
        tmp = []
        items = (line.split(','))[1:] # get data without first column
        for item in items:
            tmp.append(int(item))
        skew_val = skewness(tmp) # calculate the skewness value of a data array
        
        return_states_skew.append(skew_val)
    return return_states_skew

# Get the state list
states = (read_file('../state_list.txt')[0].split(','))

# Built the required data
path = '../../pre_proc_data/'
file_inc = path+'STATES_income_by_tot.csv'
file_edu = path+'STATES_edu_by_tot.csv'
file_LF = path+'STATES_LF.csv'
file_POP = path+'STATES_POP.csv'

# built income data exclude the first column
inc_col = ((read_file(file_inc)[0]).split(','))[1:] # collect the name of each column
for i in range(len(inc_col)): 
    inc_col[i] = inc_col[i][:-4]                    # collect income data
state_inc = convert_list((read_file(file_inc))[1:]) # calculate the skewness value of income in a state

edu_col = ((read_file(file_edu)[0]).split(','))[1:] # collect the name of each column
for i in range(len(edu_col)):
    edu_col[i] = edu_col[i][:-4]                    # collect education data
state_edu = convert_list((read_file(file_edu))[1:]) # calculate the skewness value of education in a state


state_LF = [int((n.split(',')[1])) for n in (read_file(file_LF))[1:]]   # get data of labuor force
state_POP = [int((n.split(',')[1])) for n in (read_file(file_POP))[1:]] # get data of population
state_LF_rate = []
for state_id in range(len(states)):
    lf_rate = float(state_LF[state_id]/state_POP[state_id])*100   # calculate the labour percentage in each state
    state_LF_rate.append(lf_rate)

# Display data for hypothese 2
output_path = '../../result/hyp2/'

# Display relationship between labour force and income data
x_axis = np.arange(len(states))
plt.plot(x_axis, state_LF_rate,'r--', label='Labour Force')
plt.plot(x_axis, state_inc, 'b-', label='Income')
plt.legend(loc = 'upper right')
plt.title('Labour-income info')
plt.xlabel('state')
plt.xticks(x_axis, states)
plt.savefig(output_path+'labour_income.png')
plt.clf()


# Display relationship between education data and income data
plt.plot(x_axis, state_edu, 'y-.',label = 'Education')
plt.plot(x_axis, state_inc, 'b-', label ='Income')
plt.legend(loc = 'upper right')
plt.title('education - income info')
plt.xlabel('state')
plt.xticks(x_axis, states)
plt.savefig(output_path+'edu_income.png')
plt.clf()


# Display relationship between educatino data and Labour Force Data
plt.plot(x_axis, state_edu, 'y-.', label = 'Education')
plt.plot(x_axis, state_LF_rate, 'r--', label = 'Labour Force')
plt.legend(loc = 'upper right')
plt.title('Education - Labour Force info')
plt.xlabel('State')
plt.ylabel('Skewness')
plt.xticks(x_axis, states)
plt.savefig(output_path+'edu_Labour.png')
plt.clf()
