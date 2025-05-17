import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('GooglePlaystore.xlsx')
# print(df.head())

# =========== Preprocessing ============
# 3-1-1
filter1_1 = (df['Reviews'] != '3.0M')
df = df[filter1_1]

# 3-1-2
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].replace("Varies with device", np.nan)
df = df.dropna()

# 3-1-3
def change_ver(val):
    if isinstance(val, str):
        val = val.split(" ")[0]
        if '-' in val:
            val = val.split('-')[0]
        parts = val.split('.')
        return '.'.join(parts[:2]) if len(parts) >= 2 else parts[0]
    return np.nan

df['Android Ver'] = df['Android Ver'].apply(change_ver)
df['Android Ver'] = pd.to_numeric(df['Android Ver'], errors='coerce')

# 3-1-4
df['Installs'] = df['Installs'].astype(str)
df['Installs'] = df['Installs'].str.replace(',', '').str.replace('+', '')
df = df[df['Installs'].str.isnumeric()]
df['Installs'] = df['Installs'].astype(int)

# 3-1-5
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

filter1_5 = (df['Rating'].isna()) & (df['Reviews'] < 100) & (df['Installs'] < 50000)
df = df[~filter1_5]
def fill_nan(values):
    mean_value = round(values.mean(), 2)
    return values.fillna(mean_value)

df['Rating'] = df.groupby('Category')['Rating'].transform(fill_nan)

# 3-1-6
def convert_size(val):
    if isinstance(val, str):
        if 'M' in val:
            return int(float(val.replace('M', '')) * 1e6)
        elif 'K' in val:
            return int(float(val.replace('K', '')) * 1e3)
    return np.nan

df['Size'] = df['Size'].apply(convert_size)

# =========== Analysis ============
# 3-2-1
category_stats = df.groupby('Category')['Rating'].describe()
print("Category-wise rating stats:\n", category_stats)

# 3-2-2
free_apps = df[df['Type'] == 'Free']
def top_3_per_category(df, col):
    return (
        df.sort_values(by=col, ascending=False)
          .groupby('Category')
          .head(3)[['Category', 'App', col]]
    )

top_rating = top_3_per_category(free_apps, 'Rating')
top_reviews = top_3_per_category(free_apps, 'Reviews')
top_installs = top_3_per_category(free_apps, 'Installs')

print("\nTop 3 Free Apps by Rating:\n", top_rating.head(9))
print("\nTop 3 Free Apps by Reviews:\n", top_reviews.head(9))
print("\nTop 3 Free Apps by Installs:\n", top_installs.head(9))

# 3-2-3
df['Price'] = df['Price'].astype(str).str.replace('$', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

paid_apps = df[df['Type'] == 'Paid']
avg_price = paid_apps['Price'].mean()
min_price = paid_apps['Price'].min()
max_price = paid_apps['Price'].max()

print(f"\nPaid App Price Stats:\nAverage: {avg_price}, Min: {min_price}, Max: {max_price}")

# =========== Visualization ============
# 3-3-1
df['Genres'] = df['Genres'].str.split(';')
genre_exploded = df.explode('Genres')
genre_counts = genre_exploded['Genres'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(genre_counts.head(10), labels=genre_counts.head(10).index,
        autopct='%1.1f%%', startangle=90)
plt.title('Top 10 Genres by App Count')
plt.tight_layout()
plt.show()

# 3-3-2
target = ['BUSINESS', 'EDUCATION']
filter3_2 = df['Category'].isin(target)
subset = df[filter3_2]
subset_2 = subset.dropna(subset=['Rating'])

if len(subset_2) > 0:
    fig, ax = plt.subplots(figsize=(8, 8))
    subset_2.boxplot(column='Rating', by='Category', ax=ax)
    ax.set_title('Box plot of ratings for "Business" and "Education"')
    plt.tight_layout()
    plt.show()
else:
    print("No valid data available to plot the graph!")