import pandas as pd

# Specify the extracted data file name
file = "data/trends_20260409.json"

print("Loading file: ", file)

# Loading the DataFrame using read JSON format.
df = pd.read_json(file)

# Remove duplicates
df.drop_duplicates(subset="post_id", inplace= True)

# Missing Data points
df["author"] = df["author"].fillna("unknown")
df["score"] = df["score"].fillna(0)
df["comments"] = df["comments"].fillna(0)

# Convert data types
df["score"] = df["score"].astype(int)
df["comments"] = df["comments"].astype(int)

# Store the data in csv
clean_file = "data/cleaned.csv"
df.to_csv(clean_file, index = False)


print("Cleaned data stored to ", clean_file)
print("Total rows = ", len(df))
