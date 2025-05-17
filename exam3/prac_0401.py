import pandas as pd
import numpy as np

# 문제 1. 다음 DataFrame을 만들고, NaN이 포함된 행(row) 을 제거해보세요.
df = pd.DataFrame([
    [1, 2, 3],
    [4, np.nan, 6],
    [np.nan, np.nan, np.nan],
    [7, 8, 9]
])
print(df.dropna())
print(df.dropna(axis=1))

# 문제 2. 위 DataFrame에서 NaN이 모든 열에 있는 행만 제거하세요.
print(df[df.apply(lambda row: not row.isnull().all(), axis=1)])

# 문제 3. 다음 DataFrame의 NaN을 모든 셀에 대해 0으로 채워보세요.
df = pd.DataFrame([
    [1, np.nan, 3],
    [4, 5, np.nan]
])
print(df.fillna(0))

# 문제 4. fillna()를 사용해서, **1열(두 번째 column)**에는 99, 2열에는 88로 NaN을 채워보세요 (딕셔너리 이용).
print(df.fillna({0 : 99, 1 : 88}))

# 문제 5. 아래 두 개의 DataFrame을 수직 연결 (행 concat) 하세요.
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
print(pd.concat([df1, df2], axis=0))

# 문제 6. 다음 두 개의 DataFrame을 수평 연결 (열 concat) 하세요.
df3 = pd.DataFrame({'X': [10, 20]})
df4 = pd.DataFrame({'Y': [30, 40]})
print(pd.concat([df3, df4], axis=1))

# 문제 7. 만약 두 DataFrame의 행 개수가 다르면 concat(axis=1) 결과는 어떻게 되는지 실험해보세요.
df5 = pd.DataFrame({'A': [1, 2, 3, 4]})
print(pd.concat([df5, df3], axis=1))

# 문제 8. 다음 DataFrame에서 apply()를 사용해, 각 열의 모든 값에 대해 절댓값을 구하세요.
df = pd.DataFrame({
    'a': [-1, -2],
    'b': [3, -4]
})
print(df.apply(lambda col: abs(col), axis=0))

# 문제 9. apply()를 사용해서 각 열에서 평균을 뺀 값으로 바꾸는 함수를 적용해보세요.
print(df.apply(lambda x: x - x.mean(), axis=0))

# 문제 11. 다음 데이터로부터 연도(year)별 총 인구(pop)를 구하세요.
data = {
    'state': ['A', 'A', 'B', 'B'],
    'year': [2020, 2021, 2020, 2021],
    'pop': [5.1, 5.3, 6.2, 6.4]
}
df = pd.DataFrame(data)
print(df.groupby('year')['pop'].sum())

# 문제 12. 다음 데이터에서 전공(major)과 연도별로 졸업생 수를 세고, 2022년에 심리학(Psychology) 전공 졸업생 수를 구하세요.
df = pd.DataFrame({
    'Major': ['Psychology', 'Economics', 'Psychology', 'Economics'],
    'Graduating Year': [2021, 2021, 2022, 2022],
    'School': ['A', 'B', 'A', 'B']
})
print(df.groupby(['Major', 'Graduating Year']).size())
filter12 = (df['Major'] == 'Psychology') & (df['Graduating Year'] == 2022)
print(df[filter12].shape[0])