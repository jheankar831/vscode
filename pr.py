import pandas as pd

def create_dataframe(data):
    """Create a DataFrame from the input data."""
    return pd.DataFrame(data, columns=['Day', 'Steps'])

def add_steps(df, steps):
    """Add a certain number of steps to each day in the DataFrame."""
    df['Steps'] += steps
    return df

def sort_by_steps(df):
    """Sort the DataFrame by the number of steps."""
    return df.sort_values(by='Steps')[['Day', 'Steps']]

def find_days_with_more_than_n_steps(df, n):
    """Find the days on which more than n steps were walked."""
    return df[df['Steps'] > n][['Day', 'Steps']]

# Create the input data
data = [[1, 6012], [2, 4079], [3, 6386], [4, 5230], [5, 4598], [6, 5564], [7, 6971], [8, 7763], [9, 8032], [10, 8569]]

# Create a DataFrame
df = create_dataframe(data)

# Add 2000 steps to each day
df = add_steps(df, 2000)

# Add 1000 steps to each day
df = add_steps(df, 1000)

# Print the DataFrame sorted by steps
print(sort_by_steps(df))

# Find the days on which more than 7000 steps were walked
print(find_days_with_more_than_n_steps(df, 7000))