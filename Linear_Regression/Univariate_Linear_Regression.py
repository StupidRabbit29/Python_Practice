from numpy import *

def Compute_Cost_Function(m, b, dataSet):
    error = 0
    number = len(dataSet)
    for data in dataSet:
        error += (1/(2*number))*(m*data[0] + b - data[1])
    return error

def Gradient_Descent_Runner(initial_m, initial_b, learning_rate, dataSet, iteration_times):
    m = initial_m
    b = initial_b
    for i in range(1, iteration_times):
        m, b = Gradient_Descent(m, b, learning_rate, dataSet)
        print("m = {0}, b = {1}, error = {2}".format(m, b, Compute_Cost_Function(m, b, dataSet)))
    return m, b

def Gradient_Descent(m, b, learning_rate, dataSet):
    mstep = 0
    bstep = 0
    number = len(dataSet)
    for data in dataSet:
        mstep += (1/number)*(m*data[0] + b - data[1])
        bstep += (1/number)*(m*data[0] + b - data[1])*data[0]
    return m - learning_rate*mstep, b - learning_rate*bstep

def loadData(filename):
    dataSet = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])
        #数据的X，Y信息
    return dataMat

def run():
    dataSet = genfromtxt("data.csv", delimiter=',')
    learning_rate = 0.001
    initial_m = 0
    initial_b = 0
    iteration_times = 2000
    print("Start gradient descent at m = {0}, b = {1}, error = {2}".format(initial_m, initial_b, Compute_Cost_Function(initial_m, initial_b, dataSet)))
    print("Running...")
    m, b = Gradient_Descent_Runner(initial_m, initial_b, learning_rate, dataSet, iteration_times)
    print("Gradient descent is over after {0} iterations with m = {1}, b = {2}, error = {3}".format(iteration_times, m, b, Compute_Cost_Function(m, b, dataSet)))

if __name__ is '__main__':
    run()