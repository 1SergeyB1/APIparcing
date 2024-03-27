import pandas as pd
from os import listdir
from json import load

files = listdir('locations_json')
full_frame = dict(id=[], name=[], type=[], dimension=[], url=[], created=[])
for file in files:
    with open(f'locations_json/{file}') as f:
        frame = load(f)
    results = frame["results"]
    for result in results:
        for key in full_frame.keys():
            full_frame[key].append(result[key])

df = pd.DataFrame(full_frame)
df.to_csv(f'csv_tables/locations.csv', index=False)
df.to_excel(f'excel_tables/locations.xlsx', index=False)