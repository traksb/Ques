import pandas as pd

data = [
    {"role": "assistant", "content": "What are your preferred brands of cat food? 🐱"},
    {"role": "user", "content": "Only whiskas to be honest  Only whiskas to be honest"},
    {"role": "assistant", "content": "What are your initial reactions to the new cat food concept? 🐱🍲"},
    {"role": "user", "content": "My initial reactions are very positive  My initial reactions are very positive  The benefits via nutrition  The benefits via nutrition"},
    # ... add the rest of your data here
]

# Split the data into chunks of 4 (1 pair of assistant and user interaction)
chunks = [data[i:i+4] for i in range(0, len(data), 4)]

# Create a DataFrame for each chunk and concatenate them horizontally
df = pd.concat([pd.DataFrame(chunk) for chunk in chunks], axis=1)

# Print the DataFrame
print(df)