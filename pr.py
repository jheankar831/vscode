import numpy as np
import pandas as pd

# Data for steps walked
steps_walked = [6012, 4079, 6386, 5230, 4598, 5564, 6971, 7763, 8032, 8569]

# Create a 10x2 array with day number and steps walked
data = np.array(list(enumerate(steps_walked, start=1)))

# Add 2000 steps to each day's count
data[:, 1] += 2000

# Create a pandas DataFrame for easier manipulation
df = pd.DataFrame(data, columns=['Day', 'Steps'])

# Sort the DataFrame by steps in descending order
df_sorted = df.sort_values(by='Steps', ascending=False)

# Find days with more than 7000 steps
days_over_7000 = df[df['Steps'] > 7000]['Day'].tolist()

print("Steps walked in sorted order:")
print(df_sorted)

print("\nDays with more than 7000 steps:", days_over_7000)
