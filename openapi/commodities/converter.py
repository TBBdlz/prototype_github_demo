import pandas as pd
import json

# Load JSON data
with open('data.json') as file:
    json_data = json.load(file)

# Extract the 'items' list from the JSON data
items = json_data['data']['items']

# Convert to DataFrame
df = pd.DataFrame(items)

# Save to CSV
df.to_csv('data.csv', index=False)
