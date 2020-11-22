import pandas as pd


df = pd.read_json('final_data.json', orient='records')

print(df)