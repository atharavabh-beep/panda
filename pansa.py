id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'age': [25, 32, np.nan, 45, 29, 32, 29],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR', 'Marketing', 'HR'],
    'salary': [50000, 80000, 60000, 90000, 52000, np.nan, 52000],
    'joining_date': ['2020-01-15', '2019-03-20', '2021-07-10', '2018-11-25', '2020-06-05', '2021-01-12', '2020-06-05']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display basic information
print("Initial DataFrame:")
print(df, "
")

# Cleaning and preprocessing
df['age'] = df['age'].fillna(df['age'].mean())     # Fill missing age with mean
df['salary'] = df['salary'].fillna(df['salary'].median())  # Fill missing salary with median
df.drop_duplicates(inplace=True)                   # Remove duplicates
df['name'] = df['name'].str.strip()               # Strip whitespace

print("Cleaned DataFrame:")
print(df, "
")

# Filtering data: Employees older than 30
older_than_30 = df[df['age'] > 30]
print("Employees older than 30:")
print(older_than_30, "
")

# Aggregation: Average salary by department
avg_salary_department = df.groupby('department')['salary'].mean()
print("Average salary by department:")
print(avg_salary_department, "
")

# Sorting: By salary descending
sorted_by_salary = df.sort_values(by='salary', ascending=False)
print("Data sorted by salary (desc):")
print(sorted_by_salary, "
")

# Using NumPy for numerical operations
ages = df['age'].to_numpy()
salaries = df['salary'].to_numpy()

print("Statistics using NumPy:")
print(f"Mean Age: {np.mean(ages):.2f}")
print(f"Total Salary: {np.sum(salaries)}")
print(f"Salary after 10% increment for everyone: {salaries * 1.1}
")

# Reshaping example: Pivot table
pivot_table = df.pivot_table(index='department', columns='age', values='salary', aggfunc='mean', fill_value=0)
print("Pivot Table (Salary mean by Department and Age):")
print(pivot_table)