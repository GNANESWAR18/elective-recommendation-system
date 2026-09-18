import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/elective_recommendation_students.csv")

# Basic information
print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical summary
print("\n" + "=" * 60)
print("STATISTICAL SUMMARY")
print("=" * 60)

print(df.describe())

# Elective distribution
print("\n" + "=" * 60)
print("ELECTIVE DISTRIBUTION")
print("=" * 60)

print(df["preferred_elective"].value_counts())

# Plot 1: Elective distribution
plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    y="preferred_elective",
    order=df["preferred_elective"].value_counts().index
)

plt.title("Preferred Elective Distribution")
plt.xlabel("Number of Students")
plt.ylabel("Elective")
plt.tight_layout()
plt.savefig("elective_distribution.png", dpi=300)
plt.close()

# Plot 2: Academic score distributions
score_columns = [
    "programming_score",
    "mathematics_score",
    "database_score",
    "ai_score",
    "ml_score",
    "web_score",
    "data_science_score"
]

df[score_columns].hist(
    figsize=(12, 9),
    bins=20
)

plt.suptitle("Distribution of Academic Scores")
plt.tight_layout()
plt.savefig("academic_scores.png", dpi=300)
plt.close()

# Plot 3: Correlation matrix
plt.figure(figsize=(10, 8))

correlation = df[score_columns].corr()

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Academic Score Correlation Matrix")
plt.tight_layout()
plt.savefig("score_correlation.png", dpi=300)
plt.close()

print("\nEDA completed successfully.")