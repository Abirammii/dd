# Step 3: Function to fetch data from World Bank API
import requests

def fetch_worldbank_data(indicator, start_year=2015, end_year=2022):
    url = f"http://api.worldbank.org/v2/country/all/indicator/{indicator}?date={start_year}:{end_year}&format=json&per_page=20000"
    response = requests.get(url)
    data = response.json()
    df = pd.json_normalize(data[1])
    df = df[["country.value", "countryiso3code", "date", "value"]]
    df.rename(columns={
        "country.value": "country",
        "countryiso3code": "iso3",
        "date": "year",
        "value": indicator
    }, inplace=True)
    return df

# Fetch data for all indicators
all_data = None
for code in indicators.keys():
    df = fetch_worldbank_data(code)
    if all_data is None:
        all_data = df
    else:
        all_data = pd.merge(all_data, df, on=["country", "iso3", "year"], how="outer")

print("✅ Data collected! Shape:", all_data.shape)
all_data.head()
