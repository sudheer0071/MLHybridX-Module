import seaborn as sns
import random
from .algorithm import ols, multiple, GDR
from .scores import SE
from .split import split_data
from .predict import predict_olr, perdict_multiple, predict_gdr
from .train import train_data

def datasets():
        flight = sns.load_dataset('flights').replace({'Jan': 1, 'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}) 
        anscombe = sns.load_dataset('anscombe').replace({'I':1,'II':2,'III':3,'IV':4})
        car_crash = sns.load_dataset('car_crashes').drop(['abbrev'], axis=1)
        dowjones = sns.load_dataset('dowjones')
        seaice = sns.load_dataset('seaice')
        # datasets = [flight, anscombe, car_crash, dowjones, seaice]
        dataset = {'Flight': flight, 'Anscombe':anscombe, 'Car Crash':car_crash,'Dowjones': dowjones, 'seaice': seaice,}

        name, data = random.choice(list(dataset.items()))
        
        return name, data


def By_default():

        name, data = datasets()
        print(f"*///////////////////////////////////////// ●▬▬▬▬◤ {name} Dataset ◢▬▬▬▬● ///////////////////////////////////////////\n\n")
        
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
        pred = predict_olr(x_test,m,b)
        print(f" Predicted value = {pred}")

        
        print("\n\n\n//////////////////////////////////////////// ●▬▬▬▬◤ By Multiple Regression ◢▬▬▬▬● ///////////////////////////////////////\n")
        x_train,  x_test,  y_train,  y_test = train_data( x,  y , size)
        intercept_, coef_ = multiple( x_train,  y_train)
        print(f"intercept_ = {intercept_}\ncoef_ = {coef_}")
        pred = perdict_multiple(x_test,m,b)
        print(f" Predicted value = {pred}")


        print("\n\n\n///////////////////////////////////// ●▬▬▬▬◤ By Gradient Descent Regression ◢▬▬▬▬● //////////////////////////////////////\n")
        print("\n\n\n For lr = 0.001 and epochs = 50\n\n")
        x_train,  x_test,  y_train,  y_test = train_data( x,  y , size)
        intercept_, coef_= GDR(x_train, y_train, lr=0.001, epochs=50)
        print(f"intercept = {intercept_}\ncoefficient = {coef_}")
        pred = predict_gdr(x_test,m,b)
        
        print(f" Predicted value = {pred}")
        

        


