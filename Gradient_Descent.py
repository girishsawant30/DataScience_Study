import numpy as np
def gradient_descent(x,y):
    m=c= 0
    rate = 0.001
    iteration = 100
    n = len(x)
    for i in range (iteration):
        y_predicted = m * x + c
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        mp = -(2/n)*sum(x*(y-y_predicted))
        cp = -(2/n)*sum(y-y_predicted)
        m = m - rate * mp
        c = c - rate * cp
        print("Cost Function: {}, M: {}, C: {}".format(cost, m, c))

X = np.array([2,4,6,8,10,12,14,16,18,20])
Y = np.array([10,20,30,40,50,60,70,80,90,100])
gradient_descent(X,Y)