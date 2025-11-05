# %% [markdown]
# ** Question 1 **

# %%
#1a
# Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load the dataset
df = pd.read_csv('customers.csv')

#Display first 5 rows of DataFrame
print("--- First 5 Rows of the DataFrame ---")
print(df.head())
print("\n" + "-"*40 + "\n") #Adding separator

print("--- DataFrame Info ---")
df.info()
print("\n" + "-"*40 + "\n") #Adding separator

print("--- Descriptive Statistics ---")
print(df.describe())

# %%
#1b
print("--- Question 1b: Age Statistics ---")

#Calculate the mean and standard deviation of age column 
mean_age = np.mean(df['age'])
std_dev_age = np.std(df['age'])

print(f"Mean Age: {mean_age:.2f}")
print(f"Standard Deviation of Age: {std_dev_age:.2f}\n")

#Create boolean array to identify customers under 25
is_under_25 = df['age'] < 25
print("Boolean array for the first 5 customers under 25:")
print(is_under_25.head())
print("-" * 30)

# %%
#1c
print("\n--- Question 1c: Filtering for Customers Under 25 ---")

# Use the boolean array 'is_under_25' to filter the DataFrame
# This selects only the rows where the 'is_under_25' value is True
customers_under_25 = df[is_under_25]

# Display the resulting DataFrame
print("Displaying all customers under the age of 25:")
print(customers_under_25)
print("-" * 30)

# %%
#1d
print("\n--- Question 1d: Creating the 'age_group' Column ---")

#Define the bins and corresponding labels for groups
bins = [0, 24, 59, float('inf')]
labels = ['Youth', 'Adult', 'Senior']

#Create age_group column
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=True)

#Display
print("DataFrame with the new 'age_group' column:")
print(df.head(10))
print("-" * 30)

# %% [markdown]
# ** Question 2 **

# %%
#2a
print("\n--- Question 2a: Working with Dates ---")

#Convert subscription_date to datetime
df['subscription_date'] = pd.to_datetime(df['subscription_date'])

#Extract columns
df['year_joined'] = df['subscription_date'].dt.year
df['month_joined'] = df['subscription_date'].dt.month
df['quarter_joined'] = df['subscription_date'].dt.quarter

print("DataFrame with new date columns:")
print(df[['subscription_date', 'year_joined', 'month_joined', 'quarter_joined']].head())
print("-" * 30)

# %%
#2b
print("\n--- Question 2b: GroupBy Age Group ---")

#Calculate average age and subscription year per age_group
age_group_stats = df.groupby('age_group')[['age', 'year_joined']].mean()

print("Average age and join year by age group:")
print(age_group_stats)
print("-" * 30)

# %%
#2c
print("\n--- Question 2c: Bar Chart (Sign-ups per Year) ---")

#Get counts for each year and sort by year
signups_per_year = df['year_joined'].value_counts().sort_index()

#Creating the graph
plt.figure(figsize=(10, 6)) 
signups_per_year.plot(kind='bar', color='skyblue')
plt.title('Number of Sign-ups Per Year') 
plt.xlabel('Year') 
plt.ylabel('Number of Sign-ups') 
plt.xticks(rotation=0) 
plt.grid(axis='y', linestyle='--', alpha=0.7)
print("Displaying bar chart...")

plt.show()

# %%
#2d
print("\n--- Question 2d: Pie Chart (Distribution by Age Group) ---")

#Get counts for each age group
age_group_distribution = df['age_group'].value_counts()

plt.figure(figsize=(8, 8))
age_group_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold', 'lightgreen', 'lightcoral'])
plt.title('Distribution of Customers by Age Group')
plt.ylabel('') 
print("Displaying pie chart...")

plt.show()

# %%
#2e
print("\n--- Question 2e: Saving the Cleaned Dataset ---")

#Save the DataFrame to CSV
#index=False stops the pandas index from beig saved
df.to_csv('community_customers_cleaned.csv', index=False)

print("Cleaned dataset saved as 'community_customers_cleaned.csv'")
print("-" * 30)

# %% [markdown]
# ** Question 3 *

# %%
print("\n" + "="*50 + "\n")
print("--- Starting Question 3: Health Data Analysis ---")
print("="*50 + "\n")

#3a
print("\n--- Question 3a: Load and Explore health_data.csv ---")

#Load dataset
df_health = pd.read_csv('health_data.csv')

#Explore
print("--- First 5 Rows ---")
print(df_health.head())
print("\n--- DataFrame Info ---")
df_health.info()

#Identify missing
print("\n--- Missing Values ---")
print(df_health.isnull().sum())

#Identify duplicates
print("\n--- Duplicate Rows ---")
print(f"Number of duplicate rows: {df_health.duplicated().sum()}")

#Explore numerical data
print("\n--- Descriptive Statistics ---")
print(df_health.describe())
print("-" * 30)

# %%
#3b
print("\n--- Question 3b: Clean blood_pressure Column ---")

#extract first number and convert to float
#cleans data like 120/80 by extracting 120
df_health['blood_pressure_cleaned'] = df_health['blood_pressure'].astype(str).str.extract(r'(\d+)').astype(float)

print("Blood pressure column cleaned (showing first 5):")
print(df_health[['blood_pressure', 'blood_pressure_cleaned']].head())
print("-" * 30)

# %%
#3c
print("\n--- Question 3c: Create risk_level Column ---")

#Define function
def classify_risk(row):
    if (row['BMI'] > 30) and (row['disease_score'] > 80):
        return 'High'
    elif (row['BMI'] > 25) and (row['disease_score'] > 60):
        return 'Medium'
    else:
        return 'Low'

#Apply the function
df_health['risk_level'] = df_health.apply(classify_risk, axis=1)

print("DataFrame with new 'risk_level' column:")
print(df_health[['BMI', 'disease_score', 'risk_level']].head(10))
print("-" * 30)

# %%
#3d
print("\n--- Question 3d: GroupBy risk_level ---")

#Calculate average BMI and disease score per risk_level
risk_group_stats = df_health.groupby('risk_level')[['BMI', 'disease_score']].mean()

print("Average BMI and Disease Score by Risk Level:")
print(risk_group_stats)
print("-" * 30)

# %%
#3e
print("\n--- Question 3e: Box Plot and Histogram ---")

#Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

#Plot 1
risk_order = ['Low', 'Medium', 'High']
bmi_data_by_risk = [df_health['BMI'][df_health['risk_level'] == level] for level in risk_order]

ax1.boxplot(bmi_data_by_risk, labels=risk_order)
ax1.set_title('BMI Distribution by Risk Level')
ax1.set_xlabel('Risk Level')
ax1.set_ylabel('BMI')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

#Plot 2
ax2.hist(df_health['age'], bins=15, color='teal', edgecolor='black')
ax2.set_title('Age Distribution of Patients')
ax2.set_xlabel('Age')
ax2.set_ylabel('Frequency')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
print("Displaying box plot and histogram...")

plt.show()

# %% [markdown]
# ** Question 4 **


