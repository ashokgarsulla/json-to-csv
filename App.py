import pandas as pd
import json

with open('MOCK_DATA.json') as json_file:
    data = json.loads(json_file.read())
data = pd.json_normalize(data)
print(type(data))
print(data.to_csv())
data.to_csv("stackoverflow.csv")