import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visuals(self, y_pred, y_actual, plot_type:str, title:str, xlabel: str, ylabel:str):
    
    title = f'{plot_type} Chart' 
    xlabel = f'{xlabel}'
    ylabel = f'{ylabel}'
    if plot_type == 'plot':
        sns.lineplot(x=y_actual, y=y_pred, color='blue', label='Line 1')
        sns.lineplot(x=y_actual, y=y_pred, color='red', label='Line 2')
        plt.legend()     
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.show()


    if plot_type == 'scatter':
        sns.scatterplot(x=y_actual, y=y_pred, color='blue', label='Line 1')
        sns.lineplot(x=y_actual, y=y_pred, color='red', label='Line 2')
        plt.legend()     
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.show()


def main():
    visuals([1,2,3,4,5],[2,5,8,8,5],'plot')

main()