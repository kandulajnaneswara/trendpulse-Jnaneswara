import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

# -----------------------------------------------------------
# Step 1: Setup
# -----------------------------------------------------------
# Creating output directory to save the plots if not exists
os.makedirs("outputs", exist_ok = True)

# Load the trends_analyse.csv file to the DataFrame
file = "data/trends_analysed.csv"
# write an exception if the file doesn't exists in the path.
if not Path(file).exists():
    raise FileNotFoundError(f"{file} not found. Please return to task3_analysis.py first")

df = pd.read_csv(file)

# Clean title column 
df["title"] = df["title"].fillna("Untitled").astype(str).str.strip()
# Ensure score is numeric
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0)

# Function to shorten the long titles
def shorten_title(title, max_length = 50):
    # Trim titles longer than max_length 
    if len(title) <= max_length:
        return title
    else:
        return title[:max_length] + "..."

# -----------------------------------------------------------
# Step 2: Chart 1 - Top 10 stories by score
# -----------------------------------------------------------
# Creating horizontal bar chart with Top 10 stories by score
top_10 = df.sort_values(by="score", ascending= False).head(10).copy()
# Shortening the titles for Top 10 stories
top_10["short_title"] = top_10["title"].apply(shorten_title)

# Plotting horizontal bar chart
plt.figure(figsize= (10, 6))
plt.barh(top_10["short_title"], top_10["score"])
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")
# To keep the highest score on top
plt.gca().invert_yaxis()
plt.tight_layout()
# Saving the plot in .png format
plt.savefig("outputs/chart1_top_stories.png", dpi = 300)
plt.show()


# -----------------------------------------------------------
# Step 3: Chart 2 - Stories per Category
# -----------------------------------------------------------
# Creating bar chart showing how many stories came from each category
category_counts = df["category"].value_counts()
# Defining a list of different colors for each category
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown", "tab:pink", "tab:gray", "tab:olive", "tab:cyan"]

# Ensure the no. of colors matches the no.of categories
bar_colors = colors[:len(category_counts)]

# Plotting bar chart 
plt.figure(figsize= (8, 6))
plt.bar(category_counts.index, category_counts.values, color = bar_colors)
plt.title("No. of Stories per each category")
plt.xlabel("Category")
plt.ylabel("No. of Stories")
plt.xticks(rotation = 90)
plt.tight_layout()
# Saving the plot in .png format
plt.savefig("outputs/chart2_categories.png", dpi = 300)
plt.show()

# -----------------------------------------------------------
# Step 4: Chart 3 - Scores vs Comments 
# -----------------------------------------------------------
# Creating Scatter plot - score vs no.of comments
plt.figure(figsize= (8, 6))

# Separate popular and non-popular stories
popular = df[df["is_popular"] == True]
non_popular = df[df["is_popular"] == False]

# Plotting scatter plots
plt.scatter(non_popular["score"], non_popular["num_comments"], label = "Non-Popular", alpha = 0.6, color = "tab:blue")
plt.scatter(popular["score"], popular["num_comments"], label = "Popular", alpha = 0.8, color="tab:red")

plt.title("Score vs No. of Comments")
plt.xlabel("Score")
plt.ylabel("No. of comments")
plt.legend()
plt.tight_layout()

# Saving the plot in .png format
plt.savefig("outputs/chart3_scatter.png", dpi = 300)
plt.show()


# -----------------------------------------------------------
# Dashboard: Combining all 3 charts into one figure
# -----------------------------------------------------------
# Using plt.subplots(1, 3)
fig, axes = plt.subplots(1,3, figsize= (18,5))
fig.suptitle("TrendPulse Dashboard", fontsize= 16)

# ----- Dashboard Chart 1: Top 10 Stories -----
axes[0].barh(top_10["short_title"], top_10["score"])
axes[0].set_title("Top 10 Stories")
axes[0].set_xlabel("Score")
axes[0].invert_yaxis()

# ----- Dashboard Chart 2: Stories per Category -----
axes[1].bar(category_counts.index, category_counts.values, color = bar_colors)
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis = 'x', rotation = 90)

# ----- Dashboard Chart 3: Scatter Plot -----
axes[2].scatter(non_popular["score"], non_popular["num_comments"], label = "Non-Popular", alpha = 0.6, color = "tab:blue")
axes[2].scatter(popular["score"], popular["num_comments"], label = "Popular", alpha = 0.8, color = "tab:red")
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")
axes[2].legend()

plt.tight_layout(rect= [0, 0, 1, 0.95])
# Saving the plot in .png format
plt.savefig("outputs/dashboard.png", dpi = 300)
plt.show()

print("All charts saved successfully in the 'outputs/' directory.")
