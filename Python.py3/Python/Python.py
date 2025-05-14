# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Task 1: Load and Explore Dataset
# ------------------------------

# Load the sample Iris dataset from seaborn
df = sns.load_dataset("iris")

# Display first few rows
print("📊 Dataset Preview:")
print(df.head())

# Check data types
print("\n📘 Data Types:")
print(df.dtypes)

# Check for missing values
print("\n❓ Missing Values:")
print(df.isnull().sum())

# Drop missing values (if any)
df = df.dropna()

# ------------------------------
# Task 2: Basic Data Analysis
# ------------------------------

# Descriptive statistics
print("\n📈 Descriptive Statistics:")
print(df.describe())

# Group by species and compute the mean of numeric columns
grouped_means = df.groupby("species").mean()
print("\n📊 Mean Values Grouped by Species:")
print(grouped_means)

# ------------------------------
# Task 3: Data Visualization
# ------------------------------

# 1. Line Plot: Sepal Length of First 10 Samples
plt.figure(figsize=(8, 4))
plt.plot(df['sepal_length'][:10], marker='o', linestyle='-')
plt.title('Line Chart: Sepal Length (First 10 Samples)')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart: Average Petal Length per Species
plt.figure(figsize=(6, 4))
grouped_means['petal_length'].plot(kind='bar', color='skyblue')
plt.title('Average Petal Length per Species')
plt.ylabel('Petal Length')
plt.xlabel('Species')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of Sepal Width
plt.figure(figsize=(6, 4))
plt.hist(df['sepal_width'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df, palette='deep')
plt.title('Scatter Plot: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.tight_layout()
plt.show()


