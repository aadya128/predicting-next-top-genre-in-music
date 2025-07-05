import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("/bin/best_of_2020-2025__greatest_hits_20202025.csv")
df.head()

df['year'] = pd.to_datetime(df['Release Date']).dt.year

df = df[df['year'].between(1921, 2020)]

df = df.dropna(subset=['Genres'])

df['Genres'].value_counts().head(15)

genre_counts = df.groupby(['year', 'Genres']).size().reset_index(name='count')

top_genres = genre_counts.groupby('Genres')['count'].sum().sort_values(ascending=False).head(10).index

filtered = genre_counts[genre_counts['Genres'].isin(top_genres)]

# Plot
plt.figure(figsize=(18,8)) 
sns.lineplot(data=filtered, x='year', y='count', hue='Genres')
plt.title("Top 10 Genres Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Songs")
plt.xticks(rotation=45)
plt.grid(True)

plt.xticks(filtered['year'].unique())

plt.tight_layout()
plt.show()
