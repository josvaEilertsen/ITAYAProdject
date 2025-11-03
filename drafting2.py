# %% [markdown]
# You’ve been hired by a nonprofit called ConnectSA, which provides digital literacy and streaming
# services to underserved communities in South Africa.They have collected customer data from outreach efforts in Cape Town, Durban, and Soweto.Your job is to clean, explore, and visualize this data to help them understand who their customers
# are and how engagement has grown over time.Use the dataset titled customers.csv containing 100 customer records from a nonprofit streaming
# initiative.

# %%
#1a
# Import
from IPython.display import display, HTML
import pandas as pd
import numpy as np

# Helper function to display styled headers
def print_header(title):
    """Displays a formatted and styled header."""
    display(HTML(f'<div style="background-color:#4A90E2; color:white; padding:10px; border-radius:5px; text-align:center; margin-top:20px; margin-bottom:10px;"><h2>{title}</h2></div>'))

# Helper function for styled metric display
def display_metric(label, value):
    """Displays a single metric with styling."""
    display(HTML(f'<p style="font-size:16px; margin-left:10px;"><b>{label}:</b> <span style="color:#4A90E2;">{value}</span></p>'))

#Load the dataset
df = pd.read_csv('customers.csv')

#Display first 5 rows of the DataFrame
print_header("First 5 Rows of the DataFrame")
display(df.head())

print_header("DataFrame Info")
df.info()

print_header("Descriptive Statistics")
display(df.describe())

# %%
# --- Solution for 1b ---
print_header("Question 1b: Age Statistics")

# Calculate the mean and standard deviation of the 'age' column using NumPy
# CORRECTED: Changed 'df_customers' to 'df' for consistency
mean_age = np.mean(df['age'])
std_dev_age = np.std(df['age'])

display_metric("Mean Age", f"{mean_age:.2f}")
display_metric("Standard Deviation of Age", f"{std_dev_age:.2f}")

# Create a boolean array to identify customers under 25
# This will be a Series of True/False values
is_under_25 = df['age'] < 25
display(HTML('<p style="font-size:16px; margin-left:10px;">Boolean array for the first 5 customers under 25:</p>'))
display(is_under_25.head())


# --- Solution for 1c ---
print_header("Question 1c: Filtering for Customers Under 25")

# Use the boolean array 'is_under_25' to filter the DataFrame
# This selects only the rows where the 'is_under_25' value is True
customers_under_25 = df[is_under_25]

# Display the resulting DataFrame
display(HTML('<p style="font-size:16px; margin-left:10px;">Displaying all customers under the age of 25 (age column highlighted):</p>'))
styled_customers_under_25 = customers_under_25.style.background_gradient(
    cmap='coolwarm_r', subset=['age']
).set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
display(styled_customers_under_25)


# --- Solution for 1d ---
print_header("Question 1d: Creating the 'age_group' Column")

# Define the conditions (bins) and the corresponding labels for our groups
# [cite_start]Bins: 0-24 (Youth), 25-59 (Adult), 60+ (Senior) [cite: 68, 69, 70]
bins = [0, 24, 59, float('inf')]
labels = ['Youth', 'Adult', 'Senior']

# Define a styling function to color rows based on 'age_group'
def color_age_group(row):
    if row.age_group == 'Youth':
        return ['background-color: #D4EDDA'] * len(row) # Light Green
    elif row.age_group == 'Adult':
        return ['background-color: #FFF3CD'] * len(row) # Light Yellow
    elif row.age_group == 'Senior':
        return ['background-color: #D1ECF1'] * len(row) # Light Blue
    return [''] * len(row)

# Create the new 'age_group' column using the pandas.cut() function
# This function segments the data into the bins we defined
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=True)

# Display the first 10 rows of the DataFrame to show the new column
display(HTML('<p style="font-size:16px; margin-left:10px;">DataFrame with the new \'age_group\' column (rows colored by group):</p>'))
styled_df_head = df.head(10).style.apply(color_age_group, axis=1).set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
display(styled_df_head)
