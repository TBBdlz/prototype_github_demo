import pandas as pd

# Load the CSV file and parse 'date' as datetime
daily = pd.read_csv("daily.csv", parse_dates=["date"])

# Set the 'date' column as the index of the DataFrame
daily.set_index('date', inplace=True)

# Resample to weekly and calculate the mean
weekly_df = daily.resample('W').mean()

# Select the first 144 weeks
first_145_weeks = weekly_df.head(145)

# Display or save the result
print(first_145_weeks)

# Optionally save to a new CSV file
first_145_weeks.to_csv("first_145_weeks.csv")
