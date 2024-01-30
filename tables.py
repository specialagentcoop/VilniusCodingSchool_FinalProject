import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

# # Number 1: Linear Regression
#
# df = pd.read_csv('csv_files/SkyScanner_Vilnius_Tokyo.csv')
#
# # Create a new dataframe, showing the average price for each flight date
# mean_price_df = df.groupby('Outbound Flight Date')['Price, €'].mean().reset_index()
# mean_price_df['Outbound Flight Date'] = pd.to_datetime(mean_price_df['Outbound Flight Date'])
#
# # Create a new column, representing the date number since the beginning
# mean_price_df['Date Number'] = range(1, len(mean_price_df)+1)
# print(mean_price_df)
#
# # Indicate numbers of dates in the dataframe
# future_date_number = 4
# last_date_number = max(mean_price_df['Date Number'])
#
# # Dataframe with future months
# future_date_df = pd.DataFrame({'Date Number': np.arange(last_date_number+1, last_date_number+1+future_date_number)})
# start_date = pd.to_datetime('2024-05-31')
# future_date_df['Outbound Flight Date'] = pd.to_datetime(pd.date_range(start=start_date, periods=4, freq='7D'))
# print(future_date_df)
#
# # Concatenate two dataframes
# extended_df = pd.concat([mean_price_df, future_date_df], ignore_index=True)
# print(extended_df)
#
# # Split the data into features (X) and target variable (y)
# X = mean_price_df[['Date Number']] # Using double brackets to keep X as a DataFrame
# y = mean_price_df['Price, €']
#
# # Using extended dataframe to create a future prediction
# X_extended = extended_df[['Date Number']]
#
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
#
# # Create and train the model
# model = LinearRegression()
# model.fit(X_train, y_train)
#
# # Make predictions on the test set
# y_pred = model.predict(X_test)
#
# # Make predictions on the extended set
# y_future_pred = model.predict(X_extended)
#
# # Calculate Mean Squared Error to evaluate the model performance
# mse = mean_squared_error(y_test, y_pred) # Compares real and predicted numbers and indicates the mean error
# print(f'Mean Squared Error: {mse}')
#
# plt.figure(figsize=(12,8))
#
# plt.plot(mean_price_df['Outbound Flight Date'], mean_price_df['Price, €'], label='Mean Flight Price for May')
# plt.plot(future_date_df['Outbound Flight Date'], y_future_pred[future_date_number:], linestyle='dashed', label='Predicted Mean Flight Price for Next Four Weeks)')
#
# plt.xlabel('Date')
# plt.ylabel('Mean Price, €')
# plt.title('Prediction of Vilnius-Tokyo Flight Price for June 2024')
# plt.legend()
# plt.show()

# Number 2: Vilnius - Tokyo Flight Price vs Time and Predicted Flight Prices

# df = pd.read_csv('csv_files/SkyScanner_Vilnius_Tokyo.csv')
# df['Overall Time'] = df['Outbound Flight Duration, min']+df['Return Flight Duration, min']
# print(df)
#
# X = df[['Overall Time']]
# y = df['Price, €']
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# model = LinearRegression()
# model.fit(X_train, y_train)
# X_range = pd.DataFrame({'Overall Time': range(int(min(X['Overall Time'])), int(max(X['Overall Time']))+1)})
# y_predicted = model.predict(X_range)
#
# plt.figure(figsize=(10, 6))
# plt.scatter(df['Overall Time'], df['Price, €'], color="darkseagreen", label="Actual Data")
# plt.plot(X_range, y_predicted, color="crimson", label="Predicted Prices")
# plt.xlabel("Flight Time in Minutes")
# plt.ylabel("Flight Price in Euros")
# plt.title("Vilnius - Tokyo Flight Price vs Time and Predicted Flight Prices")
# plt.legend()
# plt.show()

# Number 3: Price per Airlines

# df = pd.read_csv('csv_files/SkyScanner_Vilnius_Tokyo.csv')
# filtered_df = df[df['Outbound Flight Airlines'] == df['Return Flight Airlines']]
# mean_price_df = filtered_df.groupby('Outbound Flight Airlines')['Price, €'].mean().reset_index()
# sorted_mean_price_df = mean_price_df.sort_values('Price, €', ascending=False)
# plt.figure(figsize=(14, 10))
# sns.barplot(data=sorted_mean_price_df, x='Outbound Flight Airlines', y='Price, €', palette='viridis')
# plt.title('Average Price by Airlines', fontsize=16)
# plt.ylabel('Average Price, €')
# plt.xticks(rotation=30)
# plt.grid(True)
# plt.show()

# Number 4: Average Price by Date

# df = pd.read_csv('csv_files/SkyScanner_Vilnius_Tokyo.csv')
# df['Flight Dates'] = 'May '+df['Outbound Flight Date'].str[-2:]+'-'+df['Return Flight Date'].str[-2:]
# mean_price_df = df.groupby('Flight Dates')['Price, €'].mean()
# mean_price_df.plot(kind='bar', color='skyblue')
# plt.title('Average Vilnius - Tokyo Flight Price by Date', fontsize=16)
# plt.xlabel('Flight Date')
# plt.ylabel('Average Price, €')
# plt.xticks(rotation=0)
# plt.show()

# Number 5: Correlation Between Price and Departure Time

# df = pd.read_csv('csv_files/SkyScanner_Vilnius_Tokyo.csv')
# sorted_df = df.sort_values('Outbound Flight Departure Time', ascending=True)
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='Outbound Flight Departure Time', y='Price, €', data=sorted_df)
# plt.title('Correlation Between Price and Departure Time')
# plt.xlabel('Departure Time')
# plt.ylabel('Price, €')
# plt.xticks(rotation=30)
# plt.grid(True)
# plt.show()


