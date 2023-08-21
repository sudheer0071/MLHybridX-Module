from sklearn.model_selection import train_test_split 

def train_data(x,y,size):
     x_train, x_test, y_train, y_test = train_test_split(x, y,test_size= size, random_state=2)
     return x_train, x_test, y_train, y_test