import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Part 2
df = pd.read_csv('GermanCredit.csv')
# print(df.head())

# =========== Preprocessing ============
# 2-1-1
number_of_none = (df == 'none').sum()

sorted_none = number_of_none.sort_values(ascending=False)
get_top_3 = sorted_none.head(3)
df.drop(columns=get_top_3.index, inplace=True)

# 2-1-2
for col in df.select_dtypes(include='object'):
    df[col] = df[col].map(lambda val: val.replace("'", "") if isinstance(val, str) else val)

# 2-1-3
df['checking_status'] = df['checking_status'].replace({
    'no checking': 'No Checking',
    '<0': 'Low',
    '0<=X<200': 'Medium',
    '>=200': 'High'
})

# 2-1-4
df['savings_status'] = df['savings_status'].replace({
    'no known savings': 'No Savings',
    '<100': 'Low',
    '100<=X<500': 'Medium',
    '500<=X<1000': 'High',
    '>=1000': 'High'
})

# 2-1-5
df.loc[df['class'] == 'good', 'class'] = 1
df.loc[df['class'] == 'bad', 'class'] = 0

# 2-1-6
def map_employment(x):
    if x == 'unemployed':
        return 'Unemployed'
    if '<1' in x:
        return 'Amateur'
    if '1<=X<4' in x:
        return 'Professional'
    if '4<=X<7' in x:
        return 'Experienced'
    if '>=7' in x:
        return 'Expert'
    return x

df['employment'] = df['employment'].apply(map_employment)

# =========== Analysis ============
# 2-2-1-a
print("\nCross-tab of foreign_worker vs class:")
print(pd.crosstab(df['foreign_worker'], df['class']))

# 2-2-1-b
print("\nEmployment vs Savings Status:")
print(pd.crosstab(df['employment'], df['savings_status']))

# 2-2-2
filter2_3_1 = (df['personal_status'] == 'male single')
filter2_3_2 = (df['employment'] == 'Experienced')
print("The average credit amount of single males:", df[filter2_3_1 & filter2_3_2]['credit_amount'].mean())

# 2-2-3
print("The average credit duration for each of the job types:")
print(df.groupby('job')['duration'].mean())

# 2-2-4
edu = df[df['purpose'] == 'education']
print("\nMost common checking status for education loans:", edu['checking_status'].mode()[0])
print("Most common savings status for education loans:", edu['savings_status'].mode()[0])

# =========== Visualization ============
# 2-3-1
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

pd.crosstab(df['savings_status'], df['personal_status']).plot(kind='bar', ax=ax1, colormap='viridis')
ax1.set_title("Personal Status by Savings")
ax1.set_ylabel("Count")
ax1.set_xlabel("Savings")

pd.crosstab(df['checking_status'], df['personal_status']).plot(kind='bar', ax=ax2, colormap='plasma')
ax2.set_title("Personal Status by Checking")
ax2.set_ylabel("Count")
ax2.set_xlabel("Checking")

plt.tight_layout()
plt.show()

# 2-3-2
big_loans = df[df['credit_amount'] > 4000]
avg_age = big_loans.groupby('property_magnitude')['age'].mean()

plt.figure(figsize=(8, 5))
plt.bar(avg_age.index, avg_age.values, color='teal', edgecolor='black', width=0.5)
plt.title("Average Age by Property Type (credit > 4000)")
plt.ylabel("Average customer age")
plt.tight_layout()
plt.show()

# 2-3-3
filter3_3_1 = (df['savings_status'] == 'High')
filter3_3_2 = (df['age'] > 40)
subset = df[filter3_3_1 & filter3_3_2]

fig, axs = plt.subplots(1, 3, figsize=(18, 6))
for ax, col, title in zip(axs, ['personal_status', 'credit_history', 'job'],
                          ['Personal Status', 'Credit History', 'Job']):
    pie_data = subset[col].value_counts()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)

plt.tight_layout()
plt.show()