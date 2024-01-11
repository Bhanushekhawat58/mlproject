import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score



data = pd.read_csv("suv_data.csv")
print(data.head(10))
print(data)


print("Number of customers: ", len(data))


print(data.info())
X = data.drop(['Purchased','Gender'], axis = 1)
y = data['Purchased']
# print(X)
# print(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_test)
print(X_train)


import pandas as pd 
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

data = pd.read_csv("suv_data.csv")
print(data.head(10))
print(data)