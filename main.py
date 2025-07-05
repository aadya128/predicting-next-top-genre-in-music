import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
# Corrected path
df = pd.read_csv("/bin/best_of_2020-2025__greatest_hits_20202025.csv")
df.head()

# Convert 'Release Date' to datetime and extract year
df['year'] = pd.to_datetime(df['Release Date']).dt.year

# Drop missing or weird years
df = df[df['year'].between(1921, 2020)]

# Drop rows with missing genres
df = df.dropna(subset=['Genres'])

# View top genres
df['Genres'].value_counts().head(15)

# Group by year and genre
genre_counts = df.groupby(['year', 'Genres']).size().reset_index(name='count')

# Get top genres overall
top_genres = genre_counts.groupby('Genres')['count'].sum().sort_values(ascending=False).head(10).index

# Filter data for top genres
filtered = genre_counts[genre_counts['Genres'].isin(top_genres)]

# Plot
plt.figure(figsize=(18,8)) # Increased figure size
sns.lineplot(data=filtered, x='year', y='count', hue='Genres')
plt.title("Top 10 Genres Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Songs")
plt.xticks(rotation=45)
plt.grid(True)

# Set x-axis ticks to be the unique years in the filtered data
plt.xticks(filtered['year'].unique())

plt.tight_layout()
plt.show()
