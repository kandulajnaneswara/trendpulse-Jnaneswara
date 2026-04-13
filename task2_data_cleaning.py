import pandas as pd
import numpy as np

# -----------------------------------------------------------
# Step 1: Load the JSON File
# -----------------------------------------------------------
# Specify the extracted data file name
file = "data/trends_20260413.json"

print("Loading file: ", file)

# Loading the DataFrame using read JSON format.
df = pd.read_json(file)
print(f"Loaded {len(df)} stroies from {file}")

# -----------------------------------------------------------
# Step 2: Clean the Data
# -----------------------------------------------------------
# Remove duplicates
df_duplicates = df.drop_duplicates(subset="post_id", inplace= True)
print(f"After removing duplicates: {len(df)}")

# Missing Data points
# Handle missing values
df.dropna(subset=["post_id", "title", "score"], inplace=True)
print(f"After removing nulls: {len(df)}")

#Strip white space from titles
df["title"] = df["title"].str.strip()

# Convert data types
df["score"] = pd.to_numeric(df["score"],errors="coerce").astype(int)
df["num_comments"] = pd.to_numeric(df["num_comments"],errors="coerce").fillna(0).astype(int)


# Remove low scores
df = df[df["score"]>=5]
print(f"After removing low scores: {len(df)}")


# -----------------------------------------------------------
# Step 3: Save as csv
# -----------------------------------------------------------
# Store the data in csv
clean_file = "data/trends_clean.csv"
df.to_csv(clean_file, index = False)


print("Cleaned data stored to ", clean_file)
print(f"Saved {len(df)} rows to {clean_file}")

print(f"Stories per category: \n{df["category"].value_counts()}")
