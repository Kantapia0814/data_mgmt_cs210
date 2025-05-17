import pandas as pd
import numpy as np

# 문제 1. 다음 데이터를 DataFrame으로 만들고, 'population' 열을 출력하세요.
data = {
    'state': ['NY', 'CA', 'TX'],
    'population': [19.8, 39.5, 28.3]
}
df = pd.DataFrame(data)
print(df)
print(df['population'])

# 문제 2. 위 DataFrame에 'population_million'이라는 새 열을 추가하세요. 값은 'population' 열에 1,000,000을 곱한 결과입니다.
df['population_million'] = df['population'] * 1000000
print(df)

# 문제 3. 모든 열 이름을 'State', 'Pop_Mil', 'Pop_Real'로 변경해보세요.
df.columns = ['State', 'Pop_Mil', 'Pop_Real']
print(df)

# 문제 4. 'Pop_Real' 열을 삭제하고, 남은 DataFrame을 출력해보세요.
del df['Pop_Real']
print(df)

# 문제 5. 다음 DataFrame이 있을 때, **두 번째 행(숫자 위치)**을 iloc을 사용해 출력하세요.
df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [5, 15, 25]
})
print(df.iloc[1])

# 문제 6. 위 DataFrame에서 'A'와 'B' 열 중 'A' 값이 20 이상인 행만 선택해서 출력하세요.
print(df[df['A'] >= 20])

# 문제 7. 다음 데이터로부터 DataFrame을 만들고, 인덱스 '2023'에 [6.5, 8.8]이라는 값을 갖는 새 행을 추가하세요.
df = pd.DataFrame({
    'NY': [5.9, 6.3],
    'CA': [7.5, 8.2]
}, index=[2021, 2022])
df.loc[2023] = [6.5, 8.8]
print(df)

# 문제 8. 다음 Series에서 결측치(NaN)의 개수를 출력하세요.
s = pd.Series([1.0, np.nan, 2.5, None, 4.0])
print(s.isnull().sum())

# 문제 9. 아래 DataFrame에서 각 열의 평균을 구하세요. 단, skipna=False 옵션을 사용해서 NaN이 있으면 NaN을 반환하게 하세요.
df = pd.DataFrame({
    'x': [1, 2, np.nan],
    'y': [4, np.nan, 6]
})
print(df.mean(skipna=False))

# 문제 10. 다음 DataFrame의 절댓값을 구하고, 각 행(row)의 누적합(cumsum)을 구해서 새로운 DataFrame으로 출력하세요.
df = pd.DataFrame({
    'a': [-1, -2, 3],
    'b': [4, -5, 6]
})
df = np.abs(df)
new_df = df.cumsum(axis=1)
print(new_df)