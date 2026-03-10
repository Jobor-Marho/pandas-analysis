# Analyzing Salaries By College Major with Python (Pandas)

# ----------------------------------------------------
# 1. Import Libraries
# ----------------------------------------------------
import pandas as pd

# Format floats for readability
pd.options.display.float_format = '{:,.2f}'.format

# ----------------------------------------------------
# 2. Load Dataset
# ----------------------------------------------------
df = pd.read_csv('data/salaries_by_college_major.csv')

# ----------------------------------------------------
# 3. Create a Working Copy
# ----------------------------------------------------
df_copy = df.copy()

# ----------------------------------------------------
# 4. Explore the Dataset
# ----------------------------------------------------
print("Dataset Shape:", df_copy.shape)
print("\nColumns:", df_copy.columns.tolist())
print("\nFirst 5 rows:\n", df_copy.head())
print("\nLast 5 rows:\n", df_copy.tail())
print("\nMissing values in each column:\n", df_copy.isna().sum())

# ----------------------------------------------------
# 5. Data Cleaning
# ----------------------------------------------------
cleaned_df = df_copy.dropna()
print("\nCleaned dataset preview:\n", cleaned_df.head())

# ----------------------------------------------------
# 6. Starting Salary Analysis
# ----------------------------------------------------
starting_salary = cleaned_df['Starting Median Salary']
highest_start_idx = starting_salary.idxmax()
major_highest_start = cleaned_df.loc[highest_start_idx, 'Undergraduate Major']
highest_start_salary = cleaned_df.loc[highest_start_idx, 'Starting Median Salary']
print(f"\nHighest starting salary: {highest_start_salary} (Major: {major_highest_start})")

lowest_start_idx = starting_salary.idxmin()
major_lowest_start = cleaned_df.loc[lowest_start_idx, 'Undergraduate Major']
lowest_start_salary = cleaned_df.loc[lowest_start_idx, 'Starting Median Salary']
print(f"Lowest starting salary: {lowest_start_salary} (Major: {major_lowest_start})")

# ----------------------------------------------------
# 7. Mid-Career Salary Analysis
# ----------------------------------------------------
midcareer_salary = cleaned_df['Mid-Career Median Salary']
highest_mid_idx = midcareer_salary.idxmax()
major_highest_midcareer = cleaned_df.loc[highest_mid_idx, 'Undergraduate Major']
highest_midcareer_salary = cleaned_df.loc[highest_mid_idx, 'Mid-Career Median Salary']
print(f"\nHighest mid-career salary: {highest_midcareer_salary} (Major: {major_highest_midcareer})")

lowest_mid_idx = midcareer_salary.idxmin()
lowest_midcareer_row = cleaned_df.loc[lowest_mid_idx]
major_lowest_midcareer = lowest_midcareer_row['Undergraduate Major']
lowest_midcareer_salary = lowest_midcareer_row['Mid-Career Median Salary']
print(f"Lowest mid-career salary: {lowest_midcareer_salary} (Major: {major_lowest_midcareer})")

# ----------------------------------------------------
# 8. Salary Spread
# ----------------------------------------------------
spread = cleaned_df['Mid-Career 90th Percentile Salary'] - cleaned_df['Mid-Career 10th Percentile Salary']
cleaned_df.insert(1, 'Spread', spread)
top_spread_idx = cleaned_df['Spread'].idxmax()
print(f"\nMajor with largest salary spread: {cleaned_df.loc[top_spread_idx, 'Undergraduate Major']} (Spread: {cleaned_df.loc[top_spread_idx, 'Spread']})")

# ----------------------------------------------------
# 9. Top Salaries (90th Percentile)
# ----------------------------------------------------
top_90th = cleaned_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print("\nTop 5 majors by 90th percentile salary:\n", top_90th[['Undergraduate Major','Mid-Career 90th Percentile Salary']].head())

# ----------------------------------------------------
# 10. Top Median Mid-Career Salaries
# ----------------------------------------------------
top_midcareer = cleaned_df.sort_values('Mid-Career Median Salary', ascending=False)
print("\nTop 5 majors by mid-career median salary:\n", top_midcareer[['Undergraduate Major','Mid-Career Median Salary']].head())

# ----------------------------------------------------
# 11. Group Analysis
# ----------------------------------------------------
major_groups = cleaned_df.groupby('Group')
print("\nNumber of majors per group:\n", major_groups.size())

avg_salaries = major_groups[
    ['Starting Median Salary','Spread','Mid-Career Median Salary','Mid-Career 10th Percentile Salary','Mid-Career 90th Percentile Salary']
].mean().round(2)
print("\nAverage salary metrics per group:\n", avg_salaries)