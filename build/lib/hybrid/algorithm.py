import numpy as np

def ols(x_train,y_train):
  
        n=0
        x_bar = x_train.mean()
        y_bar = y_train.mean() 
        nr = 0
        dr = 0
        
        for i in range(len(x_train)):
            nr += ((y_train[i] - y_bar)*(x_train[i] - x_bar))
            dr += (x_train[i] - x_bar)**2
        m = nr/dr
        b = y_bar - m*x_bar 

        return m,b

def multiple(x_train, y_train):
        x_train = np.insert(x_train,0,1,axis=1)
        
        # calcuate the coeffs
        betas = np.linalg.inv(np.dot(x_train.T,x_train)).dot(x_train.T).dot(y_train)
        intercept_ = betas[0]
        coef_ = betas[1:]
    
        return intercept_, coef_

def GDR(X_trained, y_train,lr,epochs):
        # m = 100
        # b = -120  
        # x_train = x_train[:, 0]
        # for i in range(epochs):
        #     loss_slope_b = -2 * np.sum(y_train - m*x_train.ravel() - b)
        #     loss_slope_m = -2 * np.sum((y_train - m*x_train.ravel() - b)*x_train.ravel())
            
        #     b = b - (lr * loss_slope_b)
        #     m = m - (lr * loss_slope_m)
        # print(f"For lr = {lr} and epochs = {epochs}")
        # return m,b

        intercept_ = 0
        coef_ = np.ones(X_trained.shape[1])
        
        X_train =(X_trained - np.mean(X_trained, axis = 0))/np.std(X_trained, axis= 0) 

        for i in range(epochs):
            for i in range(X_train.shape[0]):
                idx = np.random.randint(0,X_train.shape[0])
                
                y_hat = np.dot(X_train[idx],coef_) + intercept_
                
                intercept_der = -2 * (y_train[idx] - y_hat)
                intercept_ = intercept_ - (lr * intercept_der)
                
                coef_der = -2 * np.dot((y_train[idx] - y_hat), X_train[idx])
                coef_ = coef_ - (lr * coef_der) 
        return intercept_ , coef_