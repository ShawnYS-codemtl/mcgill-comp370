import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("rats_complaints_locs_conditions.csv")

# Use the drop_duplicates() method to remove duplicates based on all columns
df_no_duplicates = df.drop_duplicates()

# Save the DataFrame with duplicates removed to a new CSV file
df_no_duplicates.to_csv("rats_complaints_locs_conditions_nodup.csv", index=False)