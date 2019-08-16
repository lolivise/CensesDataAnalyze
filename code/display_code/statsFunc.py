import math

# function for calculating the mean of a array
def mean(data):
    return float(sum(data))/max(len(data),1)

# function for calculating standard deviation
def cal_SD (data):
    mean_val = mean(data)
    
    sum_val = 0.0
    for item in data:
        val = float(math.pow((item-mean_val),2))
        sum_val = sum_val + val

    sd = math.sqrt((float(sum_val)/float(len(data))))

    return sd

# function for calculating skewness value
def skewness(data):
    mean_val = mean(data)
    sd = cal_SD(data)
    mole_val = 0
    for item in data:
        val = float(math.pow((item-mean_val),3))
        #print(val)
        mole_val = mole_val + val
    
    skew_val = mole_val/math.pow(sd,3)
    #print(skew_val)
    return skew_val
