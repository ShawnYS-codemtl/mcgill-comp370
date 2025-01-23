import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("buildings_frequency.csv")
df = df.astype({"building_type": str, "frequency": int})

df = df.sort_values(by='frequency', ascending=False)

# Extract building types and frequencies
building_types = df['building_type']
frequencies = df['frequency']

# Create a bar plot
fig = plt.figure(figsize = (10, 6))
plt.bar(building_types, frequencies, 
        width = 0.4)

plt.ylabel('Frequency')
plt.title('City Structures Where Conditions Attracting Rats are Present  ')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

# Show the plot
plt.show()
