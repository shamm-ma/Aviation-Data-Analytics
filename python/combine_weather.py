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

reference_column= None # reference column for first file
weather_df= [] # empty list to store each airport data 

#loop through each file 
for file in airportweather_csv:
    df= pd.read_csv(file) 

    current_columns = list(df.columns)#get column names of current file

    airport= file.split("/")[-1].split("_")[0] #get airport code from file name
    df["AIRPORT"] = airport #add airport code as new column

    df["DATE"] = pd.to_datetime(df["DATE"]) #convert DATE column to datetime format
    start_date= "2025-01-01" #set start date for filtering
    end_date= "2025-04-30" #set end date for filtering 
    df= df[(df["DATE"] >= start_date) & (df["DATE"] <= end_date)] #filter df for timeline 

    if reference_column is None:
        reference_column = current_columns
        print ("reference column saved")
    else:
        if current_columns == reference_column:
            print ("columns match")
        else:
            print("columns do not match")

    weather_df.append(df) #append each airport dataframe to list
    print()

combined_weather_df= pd.concat(weather_df, ignore_index=True) #combine all airport dataframes into one dataframe
print(
    "Combined Weather DataFrame shape:", combined_weather_df.shape,
    "Combined Weather DataFrame head:\n", combined_weather_df.head())

    
combined_weather_df.to_csv("data/raw/weatherdata/weather_2025_jan_apr.csv", index=False)
print("Combined Weather CSV saved.")
    
