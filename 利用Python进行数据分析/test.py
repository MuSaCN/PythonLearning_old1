# Author:Zhang Yuan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import statsmodels as sm
import MyPackage
__mypath__=MyPackage.MyClass_Path.MyClass_Path("\\利用Python进行数据分析") #路径类
myfile=MyPackage.MyClass_File.MyClass_File()            #文件操作类
myplt=MyPackage.MyClass_Plot.MyClass_Plot()             #直接绘图类(单个图窗)
myfig=MyPackage.MyClass_Plot.MyClass_Figure()           #对象式绘图类(可多个图窗)
myfigpro=MyPackage.MyClass_PlotPro.MyClass_FigurePro()  #高级对象式绘图类
mynp=MyPackage.MyClass_Array.MyClass_NumPy()            #多维数组类(整合Numpy)
mypd=MyPackage.MyClass_Array.MyClass_Pandas()           #矩阵数组类(整合Pandas)
mypdpro=MyPackage.MyClass_ArrayPro.MyClass_PandasPro()  #高级矩阵数组类
mytime=MyPackage.MyClass_Time.MyClass_Time()            #时间类
#---------------------------------------------------------
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\"




data = pd.DataFrame({
    'x0': [1, 2, 3, 4, 5],
    'x1': [0.01, -0.01, 0.25, -4.1, 0.],
    'y': [-1.5, 0., 3.6, 1.3, -2.]})
data
import patsy
y, X = patsy.dmatrices('y ~ x0 + x1+1', data)
#%%
y
X
#%%
np.asarray(y)
np.asarray(X)
#%%
patsy.dmatrices('y ~ x0 + x1 + 0', data)[1]
#%%
coef, resid, _, _ = np.linalg.lstsq(X, y)
#%%
coef
coef = pd.Series(coef.squeeze(), index=X.design_info.column_names)
coef
#%% md
### Data Transformations in Patsy Formulas
#%%
y, X = patsy.dmatrices('y ~ x0 + np.log(np.abs(x1) + 1)', data)
X
#%%
y, X = patsy.dmatrices('y ~ standardize(x0) + center(x1)', data)
X
#%%
new_data = pd.DataFrame({
    'x0': [6, 7, 8, 9],
    'x1': [3.1, -0.5, 0, 2.3],
    'y': [1, 2, 3, 4]})
new_X = patsy.build_design_matrices([X.design_info], new_data)
new_X
#%%
y, X = patsy.dmatrices('y ~ I(x0 + x1)', data)
X
#%% md
### Categorical Data and Patsy
#%%
data = pd.DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a', 'b', 'a', 'b'],
    'key2': [0, 1, 0, 1, 0, 1, 0, 0],
    'v1': [1, 2, 3, 4, 5, 6, 7, 8],
    'v2': [-1, 0, 2.5, -0.5, 4.0, -1.2, 0.2, -1.7]
})
y, X = patsy.dmatrices('v2 ~ key1', data)
X
#%%
y, X = patsy.dmatrices('v2 ~ key1 + 0', data)
X
#%%
y, X = patsy.dmatrices('v2 ~ C(key2)', data)
X
#%%
data['key2'] = data['key2'].map({0: 'zero', 1: 'one'})
data
y, X = patsy.dmatrices('v2 ~ key1 + key2', data)
X
y, X = patsy.dmatrices('v2 ~ key1 + key2 + key1:key2', data)
X
#%% md
## Introduction to statsmodels
#%% md
### Estimating Linear Models
#%%
import statsmodels.api as sm
import statsmodels.formula.api as smf
#%%
def dnorm(mean, variance, size=1):
    if isinstance(size, int):
        size = size,
    return mean + np.sqrt(variance) * np.random.randn(*size)

# For reproducibility
np.random.seed(12345)

N = 100
X = np.c_[dnorm(0, 0.4, size=N),
          dnorm(0, 0.6, size=N),
          dnorm(0, 0.2, size=N)]
eps = dnorm(0, 0.1, size=N)
beta = [0.1, 0.3, 0.5]

y = np.dot(X, beta) + eps
#%%
X[:5]
y[:5]
#%%
X_model = sm.add_constant(X)
X_model[:5]
#%%
model = sm.OLS(y, X)
#%%
results = model.fit()
results.params
#%%
print(results.summary())
#%%
data = pd.DataFrame(X, columns=['col0', 'col1', 'col2'])
data['y'] = y
data[:5]
#%%
results = smf.ols('y ~ col0 + col1 + col2', data=data).fit()
results.params
results.tvalues
#%%
results.predict(data[:5])
#%% md
### Estimating Time Series Processes
#%%
init_x = 4

import random
values = [init_x, init_x]
N = 1000

b0 = 0.8
b1 = -0.4
noise = dnorm(0, 0.1, N)
for i in range(N):
    new_x = values[-1] * b0 + values[-2] * b1 + noise[i]
    values.append(new_x)
#%%
MAXLAGS = 5
model = sm.tsa.AR(values)
results = model.fit(MAXLAGS)
#%%
results.params
#%% md
## Introduction to scikit-learn
#%%
train = pd.read_csv('datasets/titanic/train.csv')
test = pd.read_csv('datasets/titanic/test.csv')
train[:4]
#%%
train.isnull().sum()
test.isnull().sum()
#%%
impute_value = train['Age'].median()
train['Age'] = train['Age'].fillna(impute_value)
test['Age'] = test['Age'].fillna(impute_value)
#%%
train['IsFemale'] = (train['Sex'] == 'female').astype(int)
test['IsFemale'] = (test['Sex'] == 'female').astype(int)
#%%
predictors = ['Pclass', 'IsFemale', 'Age']
X_train = train[predictors].values
X_test = test[predictors].values
y_train = train['Survived'].values
X_train[:5]
y_train[:5]
#%%
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
#%%
model.fit(X_train, y_train)
#%%
y_predict = model.predict(X_test)
y_predict[:10]
#%% md
(y_true == y_predict).mean()
#%%
from sklearn.linear_model import LogisticRegressionCV
model_cv = LogisticRegressionCV(10)
model_cv.fit(X_train, y_train)
#%%
from sklearn.model_selection import cross_val_score
model = LogisticRegression(C=10)
scores = cross_val_score(model, X_train, y_train, cv=4)
scores



