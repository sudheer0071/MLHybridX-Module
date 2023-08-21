import numpy as np

def split_data(data, target):
        if target == "": 
            x = data.iloc[:,:-1].values.astype(np.float64)
            y = data.iloc[:,-1].values.astype(np.float64)
        else:
            print("by user")
            x = data.drop(target,axis=1).values.astype(np.float64)
            y = data[target].values.astype(np.float64)

        
        return x,y
