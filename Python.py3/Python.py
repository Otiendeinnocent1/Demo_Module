Python.py
# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Load the dataset
# Assuming the data is in a CSV file called 'data.csv'
df = pd.read_csv('data.csv')

# Step 3: Data Exploration
# Show the first few rows of the data
print("First few rows of the dataset:")
df.head()

# Get basic information about the data
print("Basic Information:")
df.info()

# Step 4: Basic Data Analysis
# Calculate summary statistics for numeric columns
print("Summary Statistics:")
df.describe()

# Filter data based on a condition (e.g., Age > 30)
filtered_data = df[df['Age'] > 30]
print(f"Data with Age > 30:\n{filtered_data}")

# Step 5: Data Visualization
# Simple Line Plot: Age vs Name
plt.plot(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Name vs Age')
plt.show()

# Bar Plot: Average Age by City
df.groupby('City')['Age'].mean().plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Average Age')
plt.title('Average Age by City')
plt.show()

# Histogram: Age Distribution
df['Age'].plot(kind='hist', bins=10, color='purple')
plt.xlabel('Age')
plt.title('Age Distribution')
plt.show()

# Scatter Plot: Age vs City
df.plot(kind='scatter', x='City', y='Age')
plt.title('City vs Age')
plt.show()

# Step 6: Observations
# Provide findings or observations based on analysis
# Example observation:
print("Observation: The average age by city shows that 'New York' has the highest average age.")

# Step 7: Saving the results (Optional)
df.to_csv('processed_data.csv')
