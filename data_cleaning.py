import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

# Function to convert time to minutes for further calculations
def hours_to_min(time):
    time_in_minutes = 0
    for value in time:
        time_element = time.split(' ')

        if len(time_element) == 1:
            time_in_minutes = int(time_element[0].replace('h', '')) * 60
        elif len(time_element) == 2:
            time_in_minutes = (int(time_element[0].replace('h', '')) * 60) + int(time_element[1])

    return int(time_in_minutes)


# Concatenate scraped files into one database
df1 = pd.read_csv('csv_files/240503-240510_SkyScanner_Vilnius_Tokyo.csv')
df2 = pd.read_csv('csv_files/240510-240517_SkyScanner_Vilnius_Tokyo.csv')
df3 = pd.read_csv('csv_files/240517-240524_SkyScanner_Vilnius_Tokyo.csv')
df4 = pd.read_csv('csv_files/240524-240531_SkyScanner_Vilnius_Tokyo.csv')
df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Clean concatenated data
df['Outbound Flight Date'] = pd.to_datetime(df['Outbound Flight Date'])
df['Return Flight Date'] = pd.to_datetime(df['Return Flight Date'])
df['Outbound Flight Duration, min'] = df['Outbound Flight Duration'].apply(hours_to_min)
df['Return Flight Duration, min'] = df['Return Flight Duration'].apply(hours_to_min)
df['Price'] = pd.to_numeric(df['Price'].str.replace(',', '').str.replace(' €', ''))
df['Outbound Flight Departure Time'] = df['Outbound Flight Departure Time'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Arrival Time'] = df['Outbound Flight Arrival Time'].str.replace("['", "").str.replace("']", "")
df['Return Flight Departure Time'] = df['Outbound Flight Departure Time'].str.replace("['", "").str.replace("']", "")
df['Return Flight Arrival Time'] = df['Outbound Flight Arrival Time'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Stops'] = pd.to_numeric(df['Outbound Flight Stops'].str.replace(' stops', '').str.replace(' stop', ''))
df['Return Flight Stops'] = pd.to_numeric(df['Return Flight Stops'].str.replace(' stops', '').str.replace(' stop', ''))
df['Outbound Flight Connecting Airports'] = df['Outbound Flight Connecting Airports'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Departure Airport'] = df['Outbound Flight Departure Airport'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Arrival Airport'] = df['Outbound Flight Arrival Airport'].str.replace("['", "").str.replace("']", "")
df['Return Flight Connecting Airports'] = df['Return Flight Connecting Airports'].str.replace("['", "").str.replace("']", "")
df['Return Flight Departure Airport'] = df['Return Flight Departure Airport'].str.replace("['", "").str.replace("']", "")
df['Return Flight Arrival Airport'] = df['Return Flight Arrival Airport'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Arrival + Days'] = pd.to_numeric(df['Outbound Flight Arrival + Days'])
df['Return Flight Arrival + Days'] = pd.to_numeric(df['Return Flight Arrival + Days'])
df.rename(columns={'Price': 'Price, €'}, inplace=True)
df.dropna()
df.drop_duplicates()

# Convert clean data to CSV file
df.to_csv('csv_files/SkyScanner_Vilnius_Tokyo.csv', index=True)

