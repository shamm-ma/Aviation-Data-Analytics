import pandas as pd 

#store monthly csvs in list 
bts_csv= ["data/raw/flightdata/bts_jan.csv",
          "data/raw/flightdata/bts_feb.csv",
          "data/raw/flightdata/bts_mar.csv",
          "data/raw/flightdata/bts_apr.csv"]  

reference_column = None # reference column for first file 
dataframes = [] # empty list to store each monthly column

#loop through each file 
for file in bts_csv:
    df=pd.read_csv(file)

    #get column names & shape of each file 

    current_columns = list(df.columns)#get column names of current file
    
    print (file)
    print (df.shape) 
    print(current_columns)

    #use first files columns as reference 
    if reference_column is None: 
        reference_column = current_columns
        print ("reference column saved")

    else: 
        #compare current file columns to reference columns 
        if current_columns == reference_column: 
            print ("columns match")

        else: 
           print("columns do not match")

    dataframes.append(df) #append each monthly dataframe to list
print()

combined_df = pd.concat(dataframes, ignore_index=True) #combine all monthly dataframes into one dataframe
print("Combined DataFrame shape:", combined_df.shape)

print(combined_df.head()) 

combined_df.to_csv("data/raw/flightdata/flights_2025_jan_apr.csv", index=False)
print("Combined CSV saved.")