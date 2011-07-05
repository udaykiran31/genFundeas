import datetime
import random
from decimal import *
from math import sqrt
def main():

    list_pop=[]
    dict_stdDev = {}
    getcontext().prec=5
    for j in range(0,10000):
        list_pop.append(j)
# population parameters
    population_mean=getMean(list_pop)
    population_stdDev=getStdDev(getStdDevNum(list_pop,population_mean),len(list_pop))
# sample parameters
    list_stdDevNum=[]    
    dict_stdDev={}
    #creates 50 random samples ...
    for b in range(0,100):
        list_sample = []
        # creating the random sample
        for i  in range(0,80):
            list_sample.append(random.randrange(0,10000))
        mean = getMean(list_sample)
        list_stdDevNum.append(getStdDevNum(list_sample,mean))
    for i in range(70,81):
        list_stdDev=[]
        for j in list_stdDevNum:
            list_stdDev.append(getStdDev(j,i))
        dict_stdDev[i]=list_stdDev
    for key in dict_stdDev.keys():
        mean_ofStdDev = getMean(dict_stdDev[key])
        dict_stdDev[key]=getMod(mean_ofStdDev,population_stdDev)
    print dict_stdDev    
        
    

## std functions
def getMean(list_sample):
    sum1 =0
    for i in list_sample:
        sum1 = sum1 + i
    return Decimal(str(sum1))/Decimal(len(list_sample))
def getStdDevNum(list_sample,mean):
    diff=0
    for i in list_sample:
        i = str(i)
        i = Decimal(i)
        diff = diff+ pow((i-mean),2)
    return diff
def getStdDev(num,sample_size):
    num = str(num)
    var = Decimal(num)/Decimal(sample_size)    
    return sqrt(var)
def getMod(var1,var2):
    var = var1-Decimal(str(var2))
    if var>=0:
        return var
    else: return var*-1

        
    

if __name__ == '__main__':
    main()
    
