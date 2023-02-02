import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv')
data.head()
data.describe()
data.fillna(data.mean(), inplace=True)
print(data)
data[['Calories', 'Max_pulse']].agg(['min','max','count','mean'])
data[(data['Calories'] >= 500) & (data['Calories'] <= 1000)]
data[(data['Calories'] > 500) & (data['Max_pulse'] < 100)]
data = data.drop('Max_pulse', axis=1)
print(data)
data['Calories'] = data['Calories'].astype(int)
plt.scatter(data['Duration'], data['Calories'])
plt.xlabel("Duration")
plt.ylabel("Calories")
plt.show()