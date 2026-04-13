import pandas as pd
import numpy as np
from pathlib import Path

#---------------------------------------------------------------
# Step 1: Load and Explore the data
#---------------------------------------------------------------
# Specify the extracted data file name
file = "data/trends_clean.csv"

# write an exception if the file doesn't exists in the path.
if not Path(file).exists():
    raise FileNotFoundError(f"{file} not found. Please return to task2_data_cleaning.py first")

# Read the csv file to DataFrames
df = pd.read_csv("data/cleaned.csv")

# Remove any accidental leading/trailing spaces
df.columns = df.columns.str.strip()
print("Available columns:", df.columns.tolist())

if "num_comments" not in df.columns:
    if "descendants" in df.columns:
        # Rename if original API field name if exists
        df.rename(columns={"descendants": "num_comments"}, inplace=True)
        print("Renamed 'descendants' to 'num_comments'.")
    else:
        # Create the column with default value 0
        df["num_comments"] = 0
        print("Column 'num_comments' not found. Created with default value 0.")

# Ensure numeric data types
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
df["num_comments"] = (
    pd.to_numeric(df["num_comments"], errors="coerce")
    .fillna(0)
    .astype(int)
)

# Explore Data
print(f"Loaded data: {df.shape}\n")

print("First 5 rows: ")
print(df.head(), "\n")

# Calculate averages using pandas DataFrame
average_score = df["score"].mean()
average_comments = df["num_comments"].mean()

print(f"Average Score: {average_score:,.0f}")
print(f"Average comments: {average_comments:,.0f}")

# -----------------------------------------------------------
# Step 2: Basic Analysis with NumPy
# -----------------------------------------------------------
# Load the df to numpy variables
scores = df["score"].to_numpy()
comments = df["num_comments"].to_numpy()

# Calculation all the mean, median, standard deviation, min & max values using NumPy
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

print("\n-----  NumPy Stats  -----")
print(f"Mean score: {mean_score:,.0f}")
print(f"Median score: {median_score:,.0f}")
print(f"Std deviation: {std_score:,.0f}")
print(f"Max score: {max_score:,.0f}")
print(f"Min score: {min_score:,.0f}")

# Calculating category with most stories
category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_category_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_category_count} stories)")

# Calculating the story that has most comments and its title & comments count
most_commented_row = df.loc[df["num_comments"].idxmax()]
most_commented_title = most_commented_row["title"]
comment_count = int(most_commented_row["num_comments"])

print(f"\nMost commented story: '{most_commented_title}' - {comment_count:,} comments")


# -----------------------------------------------------------
# Step 3: Add new columns
# -----------------------------------------------------------
# Engagement: discussion per upvote
df["engagement"] = df["num_comments"] / (df["score"]+1)

# is_popular: True if score greater than average
df["is_popular"] = df["score"] > average_score

# -----------------------------------------------------------
# Step 4: Save the Result
# -----------------------------------------------------------
analyse_file = "data/trends_analysed.csv"
df.to_csv(analyse_file, index=False)

print(f"\nSaved to {analyse_file}")
