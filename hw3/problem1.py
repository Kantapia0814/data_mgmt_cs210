import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('EuCitiesTemperatures.csv')
# print(df.head())

# Part 1
# =========== Preprocessing ============
# 1-1-1
def fill_nan(values):
    mean_value = round(values.mean(), 2)
    return values.fillna(mean_value)

country_latitude = df.groupby('country')['latitude']
df['latitude'] = country_latitude.transform(fill_nan)
country_longitude = df.groupby('country')['longitude']
df['longitude'] = country_longitude.transform(fill_nan)

# 1-1-2
filter_lat = (df['latitude'].between(40, 60))
filter_lon = (df['longitude'].between(15, 30))
subsetofcities_df = df[filter_lat & filter_lon]

country_counts = subsetofcities_df['country'].value_counts()
max_countries = country_counts.max()
most_common_countries = country_counts[country_counts == max_countries]
print(most_common_countries)

# 1-1-3
df['RegionType'] = df['EU'].astype(str) + "_" + df['coastline'].astype(str)
region_avg_temps = df.groupby('RegionType')['temperature'].mean()
df['temperature'] = df.apply(lambda row: region_avg_temps[row['RegionType']] if pd.isna(row['temperature']) else row['temperature'], axis=1)

# 1-2-1
region_counts = df['RegionType'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(region_counts.index, region_counts.values, color='skyblue', edgecolor='black', width=0.5)
plt.xlabel('Region Type EU_Coastline')
plt.ylabel('Number of Cities')
plt.title('City Count per Region Type')
plt.tight_layout()
plt.show()

# 1-2-2
plt.figure(figsize=(8, 8))
countries = df['country'].unique()
colors = plt.cm.tab20(np.linspace(0, 1, len(countries)))

for i, country in enumerate(countries):
    subset = df[df['country'] == country]
    plt.scatter(subset['longitude'], subset['latitude'], color=colors[i], label=country, s=30)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("City Map by lat/long")
plt.grid(True)
plt.tight_layout()
plt.show()

# 1-2-3
unique_countries = df[['country', 'population']].drop_duplicates()
plt.figure(figsize=(8, 6))
plt.hist(unique_countries['population'], bins=5, color='coral', edgecolor='black')
plt.xlabel('Population (in millions)')
plt.ylabel('Number of Countries')
plt.title('Country Count by Population Group')
plt.tight_layout()
plt.show()

# 1-2-4
def decide_color(temp):
    if temp > 10:
        return 'red'
    elif temp < 6:
        return 'blue'
    else:
        return 'orange'

df['temp_color'] = df['temperature'].apply(decide_color)
regions_types = df['RegionType'].unique()
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.flatten()

for i, region in enumerate(regions_types):
    sub = df[df['RegionType'] == region].reset_index(drop=True)
    axs[i].scatter(range(len(sub)), sub['latitude'], c=sub['temp_color'], s=40)
    axs[i].set_title(f"Region: {region}")
    axs[i].set_xlabel("City Index")
    axs[i].set_ylabel("Latitude")
    axs[i].set_xticks(range(len(sub)))

plt.tight_layout()
plt.show()
