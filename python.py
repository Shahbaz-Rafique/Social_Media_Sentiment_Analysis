import pandas as pd

csv_path = 'sentimentdataset.csv'
df = pd.read_csv(csv_path)

json_data = df.to_json(orient="records")

with open("data.json", "w") as json_file:
    json_file.write(json_data)
