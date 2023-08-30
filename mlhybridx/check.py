
import sys
import pandas as pd 
from .hub import check_file,ols,multiple,GDR,SE,split_data,train_data,predict_gdr,predict_olr,perdict_multiple, By_default
import time

class EasyRegressor:
    def __init__ (self, file_name = 'default'):

        if file_name == 'default':
            print("inside default")
            self.default()
            return None
            
            
        self.file_name = file_name 
        self.m = None
        self.b = None
        self.coef_ = None 
        self.intercept_ = None 
        self.data = None 
        self.target = ""
        self.test_size = 0.2
    def typer(self, output, delay = 0.001):
        for char in output:
                print(char, end="", flush= True)
                time.sleep(delay)
        print()
        return None
    def df(self):
        read_data = check_file(self.file_name)
        if read_data != False:
              self.data = pd.DataFrame(read_data)
              return self.data
        else:
            print('file not found') 
            sys.exit("File not found")
        # print(df)
         
    def split(self, target=""):
        self.target = target
        self.df()
        self.x, self.y = split_data(self.data, self.target)  

        print(f"//////////////// ●▬▬▬▬◤ Input data (X) ◢▬▬▬▬● //////////////////\n {self.x}\n\n////////////// ●▬▬▬▬◤ Output data (Y) ◢▬▬▬▬● ////////////////\n {self.y}\n\n")
        # return self.type(output, 0.000001)
        return None
    def train(self, test_size = 0.2):
        self.df() 
        self.test_size = test_size
        self.x, self.y  = split_data(self.data,self.target)
        self.x_train, self.x_test, self.y_train, self.y_test = train_data(self.x, self.y, self.test_size)
        
        print(f" //////////////////////////////// ●▬▬▬▬◤ x_train ◢▬▬▬▬● //////////////////////////////\n\n{self.x_train}\n\nshape of x_train = {self.x_train.shape}\n\n\n///////////////////////////////// ●▬▬▬▬◤ y_train ◢▬▬▬▬● /////////////////////////////\n\n{self.y_train}\n\nshape of y_train = {self.y_train.shape}\n\n\n ///////////////////////////////// ●▬▬▬▬◤ x_test ◢▬▬▬▬● //////////////////////////////\n\n{self.x_test}\n\nshape of x_test = {self.x_test.shape}\n\n\n ///////////////////////////////// ●▬▬▬▬◤ y_test ◢▬▬▬▬● //////////////////////////////\n\n{self.y_test}\n\nshape of y_test = {self.y_test.shape}")
        # return self.type(output, 0.000000001)
        return None
          
    def default(self):
        By_default()
        return ""

    def model_ols(self):
        self.df()
        x, y  = split_data(self.data, self.target)
        x_train, x_test, y_train, y_test = train_data(x, y, self.test_size)
        m,b =  ols(x_train, y_train)
        output = f"m = {m}\nb = {b}"
        return self.typer(output)


    def model_mlr(self):
        self.df()
        x, y  = split_data(self.data, self.target)
        x_train, x_test, y_train, y_test = train_data(x, y, self.test_size)
        intercept_, coef_ = multiple(x_train, y_train)
        output = f"intercept = {intercept_}\ncoefficient = {coef_}"
        return self.typer(output)
    

    def model_gdr(self, lr=0.0001, epochs=50):
        self.df()
        x, y  = split_data(self.data, self.target)
        x_train, x_test, y_train, y_test = train_data(x, y, self.test_size)
        intercept_, coef_= GDR(x_train, y_train, lr, epochs)
        output = f"intercept = {intercept_}\ncoefficient = {coef_}"
        return self.typer(output)
    


    def predict(self, model, val=None):  
      self.df()
      x, y  = split_data(self.data, self.target)
      x_train, x_test, y_train, y_test = train_data(x, y, self.test_size)
      m,b =  ols(x_train, y_train)   
      try:
        if model == 'ols':
            m,b = ols(x_train, y_train)
            if val is not None:
                 pred = predict_olr(float(val),m,b)
                 output = f"Predicted Values = {pred}"
                 return self.typer(output)
            pred = predict_olr(x_test, m, b)
            output = f"Predicted values = {pred}"
            return self.typer(output)
        
        if model == 'mlr':
            m,b = multiple(x_train, y_train)
            if val is not None:
                 pred = perdict_multiple(float(val),m,b)
                 output = f"Predicted Values = {pred}"
                 return self.typer(output)
            pred = predict_olr(x_test, m, b)
            output = f"Predicted values = {pred}"
            return self.typer(output)

        if model == 'gdr':
            m,b = GDR(x_train,  y_train, lr=0.001, epochs=50)
            if val is not None:
                 pred = predict_gdr(x_test, m, b)
                 output = f"Predicted values = {pred}"
                 return self.typer(output)
            pred = predict_gdr(x_test, m, b)
            output = f"Predicted values = {pred}"
            return self.typer(output)
      except ValueError:
          print("Inalid params")  
          
        


    def score(self, score, model):
        self.df()
        x, y  = split_data(self.data, self.target)
        x_train, x_test, y_train, y_test = train_data(x, y, self.test_size) 
        if model == "ols":
            m,b = ols(x_train,y_train) 
            n = predict_olr(x_test,m,b) 
            print(n.shape)
            return SE(y_test, n, score) 
        if model == "mlr":
            m,b = multiple(x_train,y_train)
            y_pred = perdict_multiple(x_test,m,b)
            return SE(y_test, y_pred, score) 
        if model == "gdr":
            m,b = GDR(x_train,y_train,lr=0.01,epochs= 50) 
            y_pred = predict_gdr(x_test,m,b)
            return SE(y_test, y_pred, score) 
