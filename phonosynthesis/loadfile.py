import pandas as pd
url = 'https://raw.githubusercontent.com/shraddhabarke/Phonosynthesis/master/datasets/Dutch_Roca_17.csv'
df = pd.read_csv(url, error_bad_lines=False)
print(df)