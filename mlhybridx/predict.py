import numpy as np

def predict_olr(x_test,m,b):
        n = m * x_test + b  
        return n 

def perdict_multiple(x_test,intercept_,coef_):
        y_pred = np.dot(x_test,coef_) + intercept_
        return y_pred
    
def predict_gdr(x_test,m,b):
           return m * x_test + b