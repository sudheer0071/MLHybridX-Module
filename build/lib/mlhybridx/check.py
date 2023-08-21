# import sys
# import pandas as pd 
# from check_ext.check_extention import check_file
# from algos.algorithm import ols, multiple, GDR
# from scores.scores import SE
# from split.split import split_data
# from predict.predict import predict_olr, perdict_multiple, predict_gdr
# # from default import multiple_data
# from train.train import train_data
# # from main_class import Hybrid
# from default import By_default
# import time

import sys
import pandas as pd 
from .hub import check_file,ols,multiple,GDR,SE,split_data,train_data,predict_gdr,predict_olr,perdict_multiple,multiple_data
import time

class EasyRegressor:
    def __init__ (self, file_name = 'default'):

        if file_name == 'default':
            print("inside default")
            self.default()
            
            
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
        
    def splitt(self, target=""):
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
        data = multiple_data()
        print("*///////////////////////////////////////// ●▬▬▬▬◤ Dataset ◢▬▬▬▬● ///////////////////////////////////////////\n\n")
        print(data)

        target=""

        print("\n\n\n\n\n\n\n\n//////////////////////////////// ●▬▬▬▬◤ split data ◢▬▬▬▬● //////////////////////////////////////\n\n")
        x,y = split_data(data, target)
        print(f"X: {x}\n\n\n y: {y}")

        print("\n\n\n\n\n\n\n\n\n//////////////////////////////////// ●▬▬▬▬◤ trained data ◢▬▬▬▬● ///////////////////////////////\n\n")
        x,  y = split_data(data, target)
        size = 0.2
        x_train, x_test, y_train, y_test = train_data( x,  y, size)
        print(f"X_train: {x_train}\n\n\n y_train: {y_train}\n\n\nX_test: {x_test}\n\n\n y_test: {y_test}")

        print("\n\n\n\n\n///////////////////////////////////////// ●▬▬▬▬◤ fitting into Liner Regression Models ◢▬▬▬▬● ////////////////////////////////////////")
        

        print("\n\n\n////////////////////////////////////////////////// ●▬▬▬▬◤ By ols ◢▬▬▬▬● /////////////////////////////////////////////////\n")
        x_train,  x_test,  y_train,  y_test = train_data( x,  y , size)
        m,b = ols( x_train,  y_train)
        print(f"m = {m}\nb = {b} ")
        pred = predict_gdr(x_test,m,b)
        print(f" Predicted value = {pred}")

        
        print("\n\n\n//////////////////////////////////////////// ●▬▬▬▬◤ By Multiple Regression ◢▬▬▬▬● ///////////////////////////////////////\n")
        x_train,  x_test,  y_train,  y_test = train_data( x,  y , size)
        intercept_, coef_ = multiple( x_train,  y_train)
        print(f"intercept_ = {intercept_}\ncoef_ = {coef_}")
        pred = predict_gdr(x_test,m,b)
        print(f" Predicted value = {pred}")


        print("\n\n\n///////////////////////////////////// ●▬▬▬▬◤ By Gradient Descent Regression ◢▬▬▬▬● //////////////////////////////////////\n")
        print("\n\n\n For lr = 0.001 and epochs = 50\n\n")
        x_train,  x_test,  y_train,  y_test = train_data( x,  y , size)
        intercept_, coef_= GDR(x_train, y_train, lr=0.001, epochs=50)
        print(f"intercept = {intercept_}\ncoefficient = {coef_}")
        pred = predict_gdr(x_test,m,b)
        
        print(f" Predicted value = {pred}")

        return None
        

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
            m,b = GDR(x_train, y_train, lr=0.001, epochs=50)
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
            # print(m)
            # print(b)
            n = predict_olr(x_test,m,b)
            # print(n)
            print(n.shape)
            return SE(y_test, n, score)
            return True
        if model == "mlr":
            m,b = multiple(x_train,y_train)
            # print(m)
            # print(b)
            y_pred = perdict_multiple(x_test,m,b)
            return SE(y_test, y_pred, score)
            return True
        if model == "gdr":
            m,b = GDR(x_train,y_train,lr=0.01,epochs= 50)
            # print(m)
            # print(b)
            y_pred = predict_gdr(x_test,m,b)
            return SE(y_test, y_pred, score)
            return None
