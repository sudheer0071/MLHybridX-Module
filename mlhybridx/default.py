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


        


