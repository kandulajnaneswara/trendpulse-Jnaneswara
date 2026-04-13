import pandas as pd

# Read the csv file to DataFrames
df = pd.read_csv("data/cleaned.csv")

# Printing the basic info
df.info()

# Calculating average score per category
average_score = df.groupby("category")["score"].mean()
print(f"\nAverage Score per Category: {average_score}")

# Top 5 authors by no. of Posts
top_five_authors = df["author"].value_counts().head(5)
print(f"\nTop five Authors: {top_five_authors}")

# Top commented post
top_commented_post = df.sort_values("comments", ascending = False).head(5)
#print(f"\nTop Commented Post: \n{top_commented_post.to_string(index = False, justify= "left")}") 
#pd.set_option('display.max_colwidth', None)   # Don't cut or wrap title
#pd.set_option('display.width', 1000)          # Increase total width
#pd.set_option('display.colheader_justify', 'left')  # Left align headers
print(f"\nTop Commented Post: \n{top_commented_post[["title", "comments"]].to_string(justify="left")}")