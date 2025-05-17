import pandas as pd
import numpy as np

# 문제 1: value_counts
p1 = pd.Series(['cat', 'dog', 'cat', 'bird', 'dog', 'cat', 'fish'])
# 각 동물의 등장 횟수를 출력하세요
val_count = p1.value_counts()
print(val_count)
# 가장 많이 나온 상위 2개의 값을 출력하세요
print(val_count.head(2))

# 문제 2: apply – 간단한 연산
p2 = pd.Series([3, 6, 9, 12])
# 모든 값에 2를 더한 결과를 출력하세요
print(p2 + 2)
# 모든 값을 제곱한 결과를 출력하세요
print(np.power(p2, 2))

# 문제 3: apply – 조건이 있는 함수
p3 = pd.Series([1, 5, 10, 15])
# 값이 5 이상이면 'high', 그렇지 않으면 'low'라고 출력하는 함수로 변환하세요 (apply() 사용)
def spp3(x):
    if x >= 5:
        return 'high'
    else:
        return 'low'
print(p3.apply(spp3))

# 문제 4: map – 딕셔너리 매핑
p4 = pd.Series(['a', 'b', 'c', 'a', 'd'])
# 'a'는 'apple', 'b'는 'banana', 'c'는 'cherry'로 바꾸고, 나머지는 NaN으로 출력하세요 (map() 사용)
d4 = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
print(p4.map(d4))

# 문제 5: map – 함수 매핑
p5 = pd.Series([10, 20, 30])
# 각 값에 대해 x + 5를 적용하는 lambda 함수를 이용하여 값을 바꾸세요
print(p5 + 5)
# 같은 작업을 apply()로도 해보세요. 결과가 같은지 확인해보세요
new_p5 = p5.apply(lambda x: x + 5)
print(new_p5)

# 문제 6: Series → DataFrame 변환
p6 = pd.Series({'MIT': 10000, 'Rutgers': 30000, 'NYU': 25000})
# reset_index()를 사용해서 DataFrame으로 변환하세요
p6 = p6.reset_index()
print(p6)
# 컬럼 이름을 'University', 'Students'로 바꾸세요
p6.columns = ['University', 'Students']
print(p6)
# 문제 7: DataFrame 만들기 & 정보 추출
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Department': ['HR', 'Engineering', 'Marketing']
}
# DataFrame을 만들고 출력하세요
df = pd.DataFrame(data)
print(df)
# 컬럼 이름들을 출력하세요
print(df.columns)
# 행과 열의 개수를 출력하세요
rows, cols = df.shape
print("행 개수:", rows)
print("열 개수:", cols)
# 각 열에 결측치가 있는지 확인하세요
print(df.isnull())