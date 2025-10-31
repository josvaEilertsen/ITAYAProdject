
# --- Solution for 1b ---
print("--- Question 1b: Age Statistics ---")

# Calculate the mean and standard deviation of the 'age' column using NumPy
mean_age = np.mean(df['age'])
std_dev_age = np.std(df['age'])

print(f"Mean Age: {mean_age:.2f}")
print(f"Standard Deviation of Age: {std_dev_age:.2f}\n")

# Create a boolean array to identify customers under 25
# This will be a Series of True/False values
is_under_25 = df['age'] < 25
print("Boolean array for the first 5 customers under 25:")
print(is_under_25.head())
print("-" * 30)


# --- Solution for 1c ---
print("\n--- Question 1c: Filtering for Customers Under 25 ---")

# Use the boolean array 'is_under_25' to filter the DataFrame
# This selects only the rows where the 'is_under_25' value is True
customers_under_25 = df[is_under_25]

# Display the resulting DataFrame
print("Displaying all customers under the age of 25:")
print(customers_under_25)
print("-" * 30)


# --- Solution for 1d ---
print("\n--- Question 1d: Creating the 'age_group' Column ---")

# Define the conditions (bins) and the corresponding labels for our groups
# Bins: 0-24 (Youth), 25-59 (Adult), 60+ (Senior)
bins = [0, 24, 59, float('inf')]
labels = ['Youth', 'Adult', 'Senior']

# Create the new 'age_group' column using the pandas.cut() function
# This function segments the data into the bins we defined
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=True)

# Display the first 10 rows of the DataFrame to show the new column
print("DataFrame with the new 'age_group' column:")
print(df.head(10))
print("-" * 30)