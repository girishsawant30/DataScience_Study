import numpy as np
def gradient_descent(x,y):
      m = c = 0
      LR = 0.001
      iteration = 5000
      n = len(x)
      for i in range (iteration):
          y_pred = m * x + c
          cost_func = (1/n) * sum([val**2 for val in (y-y_pred)])
          part_deriv_M = -(2/n) * sum(x*(y-y_pred))
          part_deriv_C = -(2/n) * sum(y-y_pred)
          m = m - LR * part_deriv_M
          c = c - LR * part_deriv_C          
          print("Cost Function: {}, M: {}, C: {}".format(cost_func, m, c))
          


X = np.array([2,4,6,8,10,12,14,16,18,20])
Y = np.array([10,20,30,40,50,60,70,80,90,100])
gradient_descent(X,Y)
