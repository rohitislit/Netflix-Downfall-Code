import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px

# Load data (assumes files are in same directory as script)
cases = pd.read_csv('WHO-COVID-19-global-data.csv')
stock = pd.read_csv('HistoricalData_1659131156425.csv')
vacc = pd.read_csv('owid-covid-data.csv')

# Preprocess Cases Data
cases = cases[cases['Country'] == 'United States of America']
cases['Date_reported'] = pd.to_datetime(cases['Date_reported'])
cases.reset_index(drop=True, inplace=True)

# Preprocess Stock Data
stock['Date'] = pd.to_datetime(stock['Date'])
stock = stock.sort_values(by='Date')

df = pd.DataFrame(stock, columns=['Close/Last', 'Open', 'High', 'Low'])
for col in df.columns:
    df[col] = df[col].str.replace('$', '').astype(float)
stock.update(df)

# Preprocess Vaccination Data
vacc['date'] = pd.to_datetime(vacc['date'])
vacc = vacc[vacc['location'] == 'United States']
vacc = vacc[['new_vaccinations', 'continent', 'location', 'date']].dropna().reset_index(drop=True)

# Merge Datasets
stock_with_cases = pd.merge(stock, cases, left_on="Date", right_on="Date_reported")
stock_with_vaccinations = pd.merge(stock, vacc, left_on="Date", right_on="date")
stock_vacc_cases = pd.merge(stock_with_vaccinations, cases, left_on="Date", right_on="Date_reported")
stock_vacc_cases = stock_vacc_cases[['New_cases', 'new_vaccinations', 'Close/Last', 'Open', 'Date']]
stock_vacc_cases.dropna(subset=['new_vaccinations'], inplace=True)

# Split for potential model use
train_data = stock_vacc_cases.head(350)
test_data = stock_vacc_cases.tail(50)

# Simple Linear Regression
X = stock_vacc_cases[['new_vaccinations']]
y = stock_vacc_cases[['Close/Last']]
model = linear_model.LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Plot Regression
plt.figure()
plt.plot(X, y_pred, color='red')
plt.scatter(X, y)
plt.xlabel('Vaccinations')
plt.ylabel('Close/Last')
plt.title('Vaccinations vs Stock Price')
plt.show()

# 3D Scatter with Matplotlib
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(stock_vacc_cases['New_cases'], stock_vacc_cases['new_vaccinations'], stock_vacc_cases['Close/Last'], c='r')
ax.set_xlabel('New Cases')
ax.set_ylabel('New Vaccinations')
ax.set_zlabel('Close/Last')
ax.set_title('3D Scatter Plot')
plt.show()

# 3D Plot with Plotly
fig = px.scatter_3d(stock_vacc_cases, x='New_cases', y='new_vaccinations', z='Close/Last')
fig.show()
