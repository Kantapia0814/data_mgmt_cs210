import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# Problem 1 – Short Answer Questions
# 1-1
ser = Series({'A':25, 'B':31, 'C':26}, name='scores')
print(ser.reset_index().scores[1])

# 1-2
df = DataFrame(np.arange(1,9).reshape(4,2), index=['A','B','C','D'])
df.loc['B':'D'][0].max()

# 1-3
df = DataFrame(np.arange(1,25).reshape(4,6))
print(df.iloc[-3:])

# 1-4
data = DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Abby'],
   'subject_id':['sub1','sub2','sub3','sub4','sub5']
})
print(data.T[1:3][2][0])

# Problem 2 - fillna로 특정 값만 설정 가능?
data = DataFrame({
    'Univ': ['USC', 'Yale', 'Harvard', 'UCLA', 'NCSU', 'NYU'],
    'IVY': ['No', np.nan, 'Yes', np.nan, 'No', np.nan]
})
data.loc[1, 'IVY'] = 'Yes'  # Yale
data.loc[3, 'IVY'] = 'No'   # UCLA
data.loc[5, 'IVY'] = 'No'   # NYU

print(data)

# Problem 3 - NaN을 평균으로 채우고, 3의 배수만 출력
from numpy import nan as NA
nums = Series(np.random.randint(1, 10, 20))

for i in range(5):
    nums[np.random.randint(0, 20, 1)] = NA

nums = nums.fillna(round(nums.mean()))
# nums.apply(lambda x: x if x % 3 == 0 else -1)
print(nums[nums % 3 == 0])

# Problem 4 - 최빈값 상위 2개만 남기고 나머지 -1로 바꾸기
ser = pd.Series(np.random.randint(1, 6, [12]))
top2 = ser.value_counts()[:2]
print(top2)
print(ser.where(ser.isin(top2), -1))

# Problem 5 - 각 단어의 첫 글자 대문자로
ser = Series(['how', 'to easily', 'learn', 'spoken spanish'])
capitalized = ser.apply(str.title)
print(capitalized)

# Problem 6 - 모음이 2개 이상 포함된 단어 찾기
ser = Series(['how', 'to easily', 'learn', 'spoken spanish'])
def count_vowels(word):
    count = 0
    for c in word.lower():
        if c in 'aeiou':
            count = count + 1
    return count
print(ser.apply(count_vowels) >= 2)

# Problem 7 - DataFrame에서 두 열, 두 행의 위치 바꾸는 함수
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 95]
}, index=['row1', 'row2', 'row3'])
print(df)

def switch_columns(df, col1, col2):
    cols = df.columns.tolist()
    i1, i2 = cols.index(col1), cols.index(col2)
    cols[i1], cols[i2] = cols[i2], cols[i1]
    return df[cols]
def switch_rows(df, row1, row2):
    df_copy = df.copy()
    temp = df_copy.loc[row1].copy()
    df_copy.loc[row1] = df_copy.loc[row2]
    df_copy.loc[row2] = temp
    return df_copy
print(switch_rows(df, 'row1', 'row3'))