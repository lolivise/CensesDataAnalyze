import matplotlib.pyplot as plt
import numpy as np
import csv

# built the list of name of required file
def getFileList(state,data_type,cat_list):
    file_list = []
    source_path = '../../database/'
    for cat in cat_list:
        name = source_path+'2016Census_G'+cat+'_'+state+'_'+data_type+'.csv'
        file_list.append(name)
    return file_list

# read file and return the content excluding the first line
def read_file(fileName):
    fileobj = open(fileName, 'r')
    lines = fileobj.readlines()
    fileobj.close()
    
    for i in range(len(lines)):
        lines[i] = (lines[i])[:-1]

    return lines

# determine whether need to get data base on checking row 
def getData(fileName, req_col_list, row_chk_list, row_chk_ind):
    lines = read_file(fileName)
    
    if(row_chk_list is None): # if the row checking is not set
        return ignoreCol(lines, req_col_list)
    else: # if row checking is set
        return searchByCol(lines, req_col_list, row_chk_list, row_chk_ind)

# get the required column data from every row
def ignoreCol(lines, req_col_list):

    col_name_str = lines[0]
    all_col_name = col_name_str.split(',') # get all the column of the base data
    req_data = []
    
    for line in lines[1:]:
        value = line.split(',') # get values from each column
        tmp = []

        for req_col_name in req_col_list: # go through all the column name of required data
            if(req_col_name in all_col_name): # check whether it is in the current file
                index = all_col_name.index(req_col_name) # get the index of the column when match
                tmp.append(value[index]) # store the required data
                                
        req_data.append(tmp)

    return req_data

# get the required column data base on the reqiured row
def searchByCol(lines, req_col_list, row_chk_list, row_chk_ind):
    
    col_name_str = lines[0]
    col_name_str = col_name_str[:-1] # get all the column name from the current file
    all_col_name = col_name_str.split(',')
    
    req_data = []

    for line in lines:
        value = line.split(',') # get the entire value of current row
        
        pass_test = True # set a checker

        for i in range(len(row_chk_ind)):
            if value[row_chk_ind[i]] not in row_chk_list[i]: # check the value of in the current position match 
                pass_test = False

        if(pass_test): # if current row pass all the test get the required data from the row
            tmp = []
            for col_name in req_col_list:
                if col_name in all_col_name:
                    index = all_col_name.index(col_name)
                    tmp.append(value[index])
            
            req_data.append(tmp)

    return req_data

# write the value into a CSV file
def write_to_csv(data, fileName):
    
    with open(fileName, 'w') as outFile:
        wr = csv.writer(outFile, dialect='excel')
        for row in data:
            wr.writerow(row)
        outFile.close()
