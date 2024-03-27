import pandas as pd
from os import listdir
from json import load

files = listdir('episodes_json')
full_frame = dict(id=[], name=[], air_date=[], episode=[], url=[], created=[])
for file in files:
    with open(f'episodes_json/{file}') as f:
        frame = load(f)
    results = frame["results"]
    for result in results:
        for key in full_frame.keys():
            full_frame[key].append(result[key])

df = pd.DataFrame(full_frame)
df.to_csv(f'csv_tables/episodes.csv', index=False)
df.to_excel(f'excel_tables/episodes.xlsx', index=False)