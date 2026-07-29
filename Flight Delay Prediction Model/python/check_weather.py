import pandas as pd 

airportweather_csv = [
    "data/raw/weatherdata/DFW_72259003927.csv",
    "data/raw/weatherdata/DEN_72565003017.csv",
    "data/raw/weatherdata/ATL_72219013874.csv",
    "data/raw/weatherdata/ORD_72530094846.csv",
    "data/raw/weatherdata/PHX_72278023183.csv",
    "data/raw/weatherdata/CLT_72314013881.csv",
    "data/raw/weatherdata/LAS_72386023169.csv",
    "data/raw/weatherdata/LAX_72295023174.csv",
    "data/raw/weatherdata/MCO_72205012815.csv",
    "data/raw/weatherdata/SEA_72793024233.csv",
    "data/raw/weatherdata/DCA_72405013743.csv",
    "data/raw/weatherdata/BOS_72509014739.csv",
    "data/raw/weatherdata/SFO_72494023234.csv",
    "data/raw/weatherdata/LGA_72503014732.csv",
    "data/raw/weatherdata/MIA_72202012839.csv",
    "data/raw/weatherdata/EWR_72502014734.csv",
    "data/raw/weatherdata/DTW_72537094847.csv",
    "data/raw/weatherdata/SLC_72572024127.csv",
    "data/raw/weatherdata/IAH_72243012960.csv",
    "data/raw/weatherdata/MSP_72658014922.csv",
]
#loop through each file 
for file in airportweather_csv:
    df= pd.read_csv(file) 
    

    print(file) #healthcheck 
    print(df.shape)
    print(df.head())
    print(list(df.columns))

    df["DATE"] = pd.to_datetime(df["DATE"]) #get max/min dates 
    print("Max Date:", max(df['DATE']))
    print("Min Date:", min(df['DATE']))
    print()
