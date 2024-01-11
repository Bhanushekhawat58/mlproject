import pandas as pd 
data = pd.read_csv('./Salary_Data.csv')
# print(data)
x=data.loc[:,'YearsExperience'].values.reshape(-1, 1)

y= data.loc[:,'Salary'].values



from sklearn.model_selection import train_test_split
x_train, x_test ,y_train , y_test = train_test_split(x, y, test_size=1/3, random_state=0)

from sklearn.linear_model import LinearRegression 
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test) 



""" lr = LinearRegression()
lr.fit(x.reshape(-1, 1), y)

print(lr.predict([[2.4]])) """
print(y_pred) 
print(regressor.predict([[2.4]]))

import matplotlib.pyplot as plt

plt.scatter(x_train,y_train ,color='red')
plt.plot(x_test,y_pred )
plt.show()









