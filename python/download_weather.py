from pathlib import Path
import pandas as pd 

#airport code mapping to NOAA station ID 
airport_stations= {
    "DFW": "72259003927",
    "DEN": "72565003017",
    "ATL": "72219013874",
    "ORD": "72530094846",
    "PHX": "72278023183",
    "CLT": "72314013881",
    "LAS": "72386023169",
    "LAX": "72295023174",
    "MCO": "72205012815",
    "SEA": "72793024233",
    "DCA": "72405013743",
    "BOS": "72509014739",
    "SFO": "72494023234",
    "LGA": "72503014732",
    "MIA": "72202012839",
    "EWR": "72502014734",
    "DTW": "72537094847",
    "SLC": "72572024127",
    "IAH": "72243012960",
    "MSP": "72658014922",
}

output_folder= Path("data/raw/weatherdata")
output_folder.mkdir(parents=True, exist_ok=True)

base_url = "https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2025"

for airport, station_id in airport_stations.items(): 
    url= f"{base_url}/{station_id}.csv"
    output_file= output_folder / f"{airport}_{station_id}.csv"

    print (f"Downloading {airport}")

    df= pd.read_csv(url) 
    df.to_csv(output_file, index=False) 

    print (f"saved {output_file}") 
