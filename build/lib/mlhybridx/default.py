import seaborn as sns
import random
from .algorithm import ols, multiple, GDR
from .scores import SE
from .split import split_data
from .predict import predict_olr, perdict_multiple, predict_gdr
from .train import train_data


def multiple_data():
   flight = sns.load_dataset('flights').replace({'Jan': 1, 'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}) 
  
   tips = sns.load_dataset('tips')
   car_crash = sns.load_dataset('car_crashes').drop(['abbrev'], axis=1)
   datasets = [flight, car_crash, tips]
   data = random.choice(datasets)
   return data


        


