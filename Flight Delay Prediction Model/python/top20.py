import pandas as pd 
#find top 20 Airports by no. flights for NOAA weather data comparison
df= pd.read_csv("data/raw/flightdata/flights_2025_jan_apr.csv", usecols=["ORIGIN"])

print(df["ORIGIN"].value_counts().head(20))
print(df["ORIGIN"].nunique())
