import pandas as pd
salariesData = pd.read_csv('Salary_Data.csv')
A = salariesData.iloc[:, :-1].values
B = salariesData.iloc[:, 1].values
from sklearn.model_selection import train_test_split
A_train, A_test, B_train, B_test = train_test_split(A, B, test_size = 1/3, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(A_train, B_train)
pred = clf.predict(A_test)
from sklearn.metrics import mean_squared_error
mse2=mean_squared_error(A_test,pred)
print(mse2)
mse1 = mean_squared_error(B_test, pred)
print(mse1)
import matplotlib.pyplot as plt
plt.scatter(A_train, B_train, colour = 'Green')
plt.scatter(A_test, B_test, colour = 'Orange')
plt.title('Salary Data')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.show()