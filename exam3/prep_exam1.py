import numpy as np
import pandas as pd

data = pd.read_csv('health_data.csv')
# problem 1 - b : BMI 계산 및 그룹화
bmi = data['Weight'] / ((data['Height'] / 100) ** 2)
data['BMI'] = bmi
bins = [0, 18.5, 25, 30, np.inf]
labels = [0, 1, 2, 3]
data['BMI_Group'] = pd.cut(data['BMI'], bins=bins, labels=labels).astype(int)

# problem 1 - c : 'Risk'가 NaN인 경우, 같은 'BMI_Group'의 평균값으로 채우시오
data['Risk'] = data.groupby('BMI_Group')['Risk'].transform(lambda x: x.fillna(x.mean()))

# problem 1 - d : Min-Max 정규화
glucose_min = data['Glucose'].min()
glucose_max = data['Glucose'].max()

data['Glucose_Scaled'] = (data['Insulin'] - glucose_min) / (glucose_max - glucose_min)

# problem 2 - a : 위도 경도 도시 필터링
df_city = pd.read_csv('city.csv')
filter_lat = df_city['latitude'].between(35, 55)
filter_lon = df_city['longitude'].between(10, 40)
filtered_city = df_city[filter_lat & filter_lon]

# problem 2 - b : 인구 수 상위 3개 도시만 남기고, 나머지는 'Other'
top3_cities = df_city.sort_values(by='population', ascending=False)['city'].unique()[:3]
# 'city' 열 변경
df_city['city'] = df_city['city'].where(df_city['city'].isin(top3_cities), 'Other')

# problem 2 - c : 도시별 평균 위도와 경도 계산
city_avg_coords = df_city.groupby('city')[['latitude', 'longitude']].mean()
print(city_avg_coords)


# problem 3 - a : 각 문자열의 단어 수를 구한 Series를 만들어라
ser = pd.read_csv('words.csv')
word_counts = ser.apply(lambda x: len(x.split()))
print(word_counts)

# problem 3 - b : 모음이 3개 이상 포함된 문자열만 필터링
def count_vowels(word):
    count = 0
    for c in word.lower():
        if c in 'aeiou':
            count = count + 1
    return count
filtered = ser[ser.apply(count_vowels) >= 3]
print(filtered)

# problem 3 - c : 최빈 단어 상위 2개만 남기고 나머지는 'X'로 바꾸기
# 1. 단어 나누기
all_words = ser.str.split().explode()
# 2. 최빈값 상위 2개
top2_words = all_words.value_counts().index[:2].tolist()
# 3. 원래 구조로 되돌려서 'X' 처리
def keep_top2_words(sentence):
    return ' '.join([word if word in top2_words else 'X' for word in sentence.split()])
# 4. 적용
processed_ser = ser.apply(keep_top2_words)
print(processed_ser)

