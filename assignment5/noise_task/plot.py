import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("dataset.csv")

# Extract issue names and monthly values
issues = df["Issue"]
months = df.columns[1:]
data = df.iloc[:, 1:]

# Convert the data to a list of lists
data = data.values.tolist()

# Create a list of colors for the bars
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.7', '0.5']

# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 6))

for i, (issue, color) in enumerate(zip(issues, colors)):
    ax.bar(months, data[i], label=issue, color=color)

#ax.set_xlabel('Months')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Noise Issues Across 2020 in Residential Areas ')
ax.legend()

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the plot or save it to a file
plt.show()
