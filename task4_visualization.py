import pandas as pd
import matplotlib.pyplot as plt
import os

# Creating one dir to save the plots 
os.makedirs("plots", exist_ok = True)
# Read the csv file to the DataFrame
df = pd.read_csv("data/cleaned.csv")

# Bar chart - Avg score per category
avgerage_score = df.groupby("category")["score"].mean()

plt.figure()
avgerage_score.plot(kind="bar")
plt.title("Average Score by Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.xticks(rotation=90)
plt.tight_layout()

# Saving the plot in .png format
barchart_path = f"plots/average_score_per_category.png"
plt.savefig(barchart_path, dpi = 300)
plt.close()
#plt.show()
print(f"Bar Chart saved: {barchart_path}")

# Histogram - Score distribution
plt.figure()
df["score"].plot(kind="hist", bins=20)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()

# Saving the plot in .png format
histogram_path = f"plots/score_distribution.png"
plt.savefig(histogram_path, dpi = 300)
plt.close()
#plt.show()
print(f"Histogram Chart saved: {histogram_path}")

# Pie chart - Category distribution
plt.figure()
df["category"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Distribution")
plt.ylabel("")
plt.legend(df["category"].value_counts().index, loc = "upper right")


# Saving the plot in .png format
piechart_path = f"plots/category_distribution.png"
plt.savefig(piechart_path, dpi = 300)
plt.close()
#plt.show()
print(f"Pie Chart saved: {piechart_path}")

# Scatter plot - score vs no.of comments
plt.figure()
plt.scatter(df["score"], df["comments"], alpha= 0.7)
plt.title("Score vs No. of Comments")
plt.xlabel("Score")
plt.ylabel("No. of comments")
plt.tight_layout()

# Saving the plot in .png format
scatterplot_path = f"plots/score_vs_no_of_comments.png"
plt.savefig(scatterplot_path, dpi = 300)
plt.close()
#plt.show()
print(f"Scatter Plot saved: {scatterplot_path}")


print("All plots were saved in the 'plots/' directory.")
