import pandas as pd

# Create a 10x2 array
data = [[1, 6012], [2, 4079], [3, 6386], [4, 5230], [5, 4598], [6, 5564], [7, 6971], [8, 7763], [9, 8032], [10, 8569]]
df = pd.DataFrame(data, columns=['Day', 'Steps'])

# Add 2000 steps to each day's steps walked
df['Steps'] += 2000

# Add 1000 steps to all the observations
df['Steps'] += 1000

# Print the array containing steps walked in sorted order
print(df.sort_values(by='Steps')[['Day', 'Steps']])

# Find out the days on which he walked more than 7000 steps
print(df[df['Steps'] > 7000][['Day', 'Steps']])