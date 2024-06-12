import pandas as pd

# Replace 'quoridor_data.csv' with the path to your CSV file if it's not in the same directory.
df = pd.read_csv('quoridor_data.csv')
# To display the first few rows of the DataFrame to ensure it's loaded correctly, use:
print(df.head(10000)) 