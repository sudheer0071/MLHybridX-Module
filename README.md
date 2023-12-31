#  ML Module that makes learning process smooth

### Project Overview
This project focuses on the implementation of fundamental machine learning algorithms from scratch. The primary goal is to gain a deep understanding of how these algorithms work by coding them manually. By implementing algorithms like linear regression and logistic regression, we can explore their inner workings, mathematical foundations, and practical applications.

### Algorithms Used
#### Linear regression 
It is a basic algorithm for predicting a continuous target variable based on one or more input features. It involves fitting a linear relationship between the inputs and the target variable.

we will more algorithms soon.


## Installation

You can simply Install this Module just like another Module

Firstly, make sure you have installed these libraries : [ numpy, pandas, scikit-learn, seaborn ]

if you don't have these models no need to worry you can simply install it by :: pip install <<module name>Module name>



```bash
  pip install mlhybridx 
```
Here we go !. Now you can use it in your systems.

## Usage/Examples

```python
import hybrid
from hybrid import EasyRegressor

"""
If you have no idea about what can you do with dataset
and how can you apply train_test_split, fitting in models etc for that you 
can pass default parameter inside EasyRegressor on 
running that you will get the whole idea about any model.
"""
# just run this and you get the whole idea about all processes
EasyRegressor('default')
# this takes random dataset from seaborn and tells about every process
#                              output

"""
inside default
*///////////////////////////////////////// ●▬▬▬▬◤ Dataset ◢▬▬▬▬● ///////////////////////////////////////////


            Date  Extent
0     1980-01-01  14.200
1     1980-01-03  14.302
2     1980-01-05  14.414
3     1980-01-07  14.518
4     1980-01-09  14.594
...          ...     ...
13170 2019-12-27  12.721
13171 2019-12-28  12.712
13172 2019-12-29  12.780
13173 2019-12-30  12.858
13174 2019-12-31  12.889

[13175 rows x 2 columns]








//////////////////////////////// ●▬▬▬▬◤ split data ◢▬▬▬▬● //////////////////////////////////////


//////////////// ●▬▬▬▬◤ Input data (X) ◢▬▬▬▬● //////////////////
 [[3.1553280e+17]
 [3.1570560e+17]
 [3.1587840e+17]
 ...
 [1.5775776e+18]
 [1.5776640e+18]
 [1.5777504e+18]]

////////////// ●▬▬▬▬◤ Output data (Y) ◢▬▬▬▬● ////////////////
 [14.2   14.302 14.414 ... 12.78  12.858 12.889]











//////////////////////////////////// ●▬▬▬▬◤ trained data ◢▬▬▬▬● ///////////////////////////////


 //////////////////////////////// ●▬▬▬▬◤ x_train ◢▬▬▬▬● //////////////////////////////

[[5.588352e+17]
 [4.779648e+17]
 [7.509024e+17]
 ...
 [7.919424e+17]
 [6.342624e+17]
 [6.913728e+17]]

shape of x_train = (10540, 1)


///////////////////////////////// ●▬▬▬▬◤ y_train ◢▬▬▬▬● /////////////////////////////

[ 7.223 15.447  8.939 ... 15.259 15.277 11.725]

shape of y_train = (10540,)


 ///////////////////////////////// ●▬▬▬▬◤ x_test ◢▬▬▬▬● //////////////////////////////

[[1.5468192e+18]
 [7.9747200e+17]
 [7.4908800e+17]
 ...
 [1.5539040e+18]
 [4.7243520e+17]
 [8.6624640e+17]]

shape of x_test = (2635, 1)


 ///////////////////////////////// ●▬▬▬▬◤ y_test ◢▬▬▬▬● //////////////////////////////

[13.282 14.686  6.9   ... 14.096 13.202 11.968]

shape of y_test = (2635,)





///////////////////////////////////////// ●▬▬▬▬◤ fitting into Liner Regression Models ◢▬▬▬▬● ////////////////////////////////////////



////////////////////////////////////////////////// ●▬▬▬▬◤ By ols ◢▬▬▬▬● /////////////////////////////////////////////////

m = [-1.92604083e-18]
b = [13.19621591] 
 Predicted value = [[10.21697898]
 [11.66025228]
 [11.75344184]
 ...
 [10.20333336]
 [12.28628643]
 [11.52778998]]



//////////////////////////////////////////// ●▬▬▬▬◤ By Multiple Regression ◢▬▬▬▬● ///////////////////////////////////////

intercept_ = 13.196215914838561
coef_ = [-1.92604083e-18]
 Predicted value = [[10.21697898]
 [11.66025228]
 [11.75344184]
 ...
 [10.20333336]
 [12.28628643]
 [11.52778998]]



///////////////////////////////////// ●▬▬▬▬◤ By Gradient Descent Regression ◢▬▬▬▬● //////////////////////////////////////




 For lr = 0.001 and epochs = 50


intercept = 11.263270304178373
coefficient = [-0.64567608]
 Predicted value = [[10.21697898]
 [11.66025228]
 [11.75344184]
 ...
 [10.20333336]
 [12.28628643]
 [11.52778998]]

"""
# making an object
# new = Hybrid('<name of your dataset in csv formate>')
# suppose we have a dataset of wine.csv

new = EasyRegressor('wine.csv')

# To see dataset in dataframe
new.df()
# output show below in image
```
![Alt text](image.png)

```python
# if you want to give target column for which values you want to predict pass the target parameter inside split() method
# new.split(target = 'pH')

new.split()
# by default it takes last column as a target column

#                   output

"""//////////////// ●▬▬▬▬◤ Input data (X) ◢▬▬▬▬● //////////////////
 [[ 7.4    0.7    0.    ...  3.51   0.56   9.4  ]
 [ 7.8    0.88   0.    ...  3.2    0.68   9.8  ]
 [ 7.8    0.76   0.04  ...  3.26   0.65   9.8  ]
 ...
 [ 6.3    0.51   0.13  ...  3.42   0.75  11.   ]
 [ 5.9    0.645  0.12  ...  3.57   0.71  10.2  ]
 [ 6.     0.31   0.47  ...  3.39   0.66  11.   ]]

////////////// ●▬▬▬▬◤ Output data (Y) ◢▬▬▬▬● ////////////////
 [5. 5. 5. ... 6. 5. 6.]
"""

# after splitting the data next part is the training part 
# before that we have to split train data and test data
new.train(test_size = 0.3) # you can also pass test_size  and target in train , by default it runs on 0.2
#                        output 
""" 
 //////////////////////////////// ●▬▬▬▬◤ x_train ◢▬▬▬▬● //////////////////////////////

[[ 7.3   0.39  0.31 ...  3.41  0.54  9.4 ]
 [ 6.7   0.46  0.24 ...  3.39  0.6  10.6 ]
 [ 7.5   0.57  0.02 ...  3.36  0.62 10.8 ]
 ...
 [ 8.9   0.84  0.34 ...  3.12  0.48  9.1 ]
 [12.8   0.3   0.74 ...  3.2   0.77 10.8 ]
 [ 6.9   0.51  0.23 ...  3.4   0.84 11.2 ]]

shape of x_train = (1119, 11)


///////////////////////////////// ●▬▬▬▬◤ y_train ◢▬▬▬▬● /////////////////////////////

[6. 6. 6. ... 6. 7. 6.]

shape of y_train = (1119,)


 ///////////////////////////////// ●▬▬▬▬◤ x_test ◢▬▬▬▬● //////////////////////////////

[[ 7.2   0.63  0.   ...  3.37  0.58  9.  ]
 [11.6   0.47  0.44 ...  3.38  0.86  9.9 ]
 [ 7.7   0.96  0.2  ...  3.36  0.44 10.9 ]
 ...
 [ 7.9   0.18  0.4  ...  3.33  0.93 11.3 ]
 [ 9.9   0.53  0.57 ...  3.19  0.76 11.6 ]
 [ 6.8   0.49  0.22 ...  3.41  0.83 11.3 ]]

shape of x_test = (480, 11)


 ///////////////////////////////// ●▬▬▬▬◤ y_test ◢▬▬▬▬● //////////////////////////////

[6. 4. 5. ... 5. 7. 6.]

shape of y_test = (480,)
"""

# Now Applying Model
# we have three models in Linear Regression you can choose one of them according to your data set , i go for Multiple Linear Regression Model --> *** model_mlr ***

new.model_mlr()

#                                  output
"""
intercept = 25.141588069949456
coefficient = [ 3.16451741e-02 -1.13297028e+00 -1.29162767e-01  2.98498912e-02
 -1.94941142e+00  2.85043937e-03 -2.85137633e-03 -2.10144417e+01
 -3.77024485e-01  9.04017724e-01  2.53185189e-01]
 """

# Next is to find the predicted values
# predict method contains 2 params first is model and second is any value on which more values will be predicted second parameter is optional

new.predict('mlr') # you can also pass second parameter 
# here prediction is on the basis of multple linear Regression model called ---> mlr
#                                  output
"""  
Predicted values = [[ 1.81051079e+02  1.47062302e+01 -1.29162767e-01 ...  8.43501273e+01
   1.54861388e+01  2.26527478e+02]
 [ 2.91674067e+02  1.06835761e+01  1.09331360e+01 ...  8.46015432e+01
   2.25257835e+01  2.49154907e+02]
 [ 1.93621873e+02  2.30029543e+01  4.89915485e+00 ...  8.40987114e+01
   1.19663165e+01  2.74296495e+02]
 ...
 [ 1.81051079e+02  1.14378238e+01  4.39632309e+00 ...  8.81213655e+01
   1.90059611e+01  2.41612431e+02]
 [ 1.93621873e+02  1.77232208e+01  6.65906601e+00 ...  8.10817209e+01
   1.22177324e+01  2.34069954e+02]
 [ 1.93621873e+02  1.65918493e+01  2.38499604e+00 ...  8.48529591e+01
   1.32233959e+01  2.44126589e+02]]
"""

# Next part is to find the score for that we have score method which takes 2 params first is which type of score you want to find and second is model name

new.score('RMSE', 'mlr') 
#                                  output
"""
R2 Score = 0.3787468740719061
'MSE = 0.6349626010421263'
"""

# If you have no idea about what can you do with dataset and how can you apply train, models etc for that you can pass default parameter inside EasyRegressor on running that you will get the whole idea about any model.
```


## License

This project is licensed under the MIT License - see the <u>[LISCENCE</u>](Liscence.txt) file for details.

## 🔗 Links

Documentation : [
MLHybridX · PyPi
](https://pypi.org/project/mlhybridx/)

Github Repo: [MLHybridX-Module](https://github.com/sudheer0071/MLHybridX)

### Now terminal version is also available !! 
#### check it out
Github Repo: [mlhybridx-terminal-version](https://github.com/sudheer0071/mlhybridx-terminal-version/tree/main)

## Contributor
![](https://skillicons.dev/icons?i=github)

[Deepak Yadav](https://github.com/nero58)  and [Sudheer](https://github.com/sudheer0071)


## Languages used 
![My Skills](https://skillicons.dev/icons?i=py,git)