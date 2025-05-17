import pandas as pd
import numpy as np

# 문제 1. Series 생성과 인덱스 접근
p1 = pd.Series([15, 30, 45], index=['x', 'y', 'z'])

# 인덱스 'y'에 해당하는 값을 출력하시오.
print(p1['y'])
# 'z', 'x' 순서로 값을 가져오시오.
print(p1[['z', 'x']])

# 문제 2. 조건 필터링
p2 = pd.Series([5, -2, 8, -1, 0], index=['a', 'b', 'c', 'd', 'e'])

# 0보다 큰 값들만 출력하시오.
print(p2[p2 > 0])
# 음수인 값들을 100으로 바꾼 새로운 Series를 만들어보시오.
new_p2_2 = p2.copy()
new_p2_1 = p2.apply(lambda x: 100 if x < 0 else x)
filter2 = (p2 < 0)
new_p2_2[filter2] = 100
print(new_p2_1)
print(new_p2_2)

# 문제 3. 딕셔너리 기반 Series 만들기
# 다음 딕셔너리를 기반으로 Series를 만들되, 인덱스를 ['B', 'C', 'D']로 지정하시오. {'A': 100, 'B': 200, 'C': 300}

# 생성된 Series를 출력하시오.
ps_data = {'A': 100, 'B': 200, 'C': 300}
p3 = pd.Series(ps_data, index=['B', 'C', 'D'])
print(p3)
# NaN이 있는 인덱스를 찾아 출력하시오.
print(p3[p3.isnull()].index)

# 문제 4. Series 연산
p4 = pd.Series([3, 6, 9], index=['a', 'b', 'c'])

# 모든 값에 대해 제곱한 결과를 새로운 Series로 저장하시오.
new_p4 = np.power(p4, 2)
print(new_p4)
# 값이 5보다 큰 항목만 필터링해서 출력하시오.
filter4 = (new_p4 > 5)
print(new_p4[filter4])

# 문제 6. 값 대체하기
p6 = pd.Series(['apple', 'banana', 'apple', 'cherry'])

# 'apple'을 'fruit'으로 바꾸시오.
p6.replace('apple', 'fruit', inplace=True)
# 각 과일의 등장 횟수를 세시오.
print(p6.value_counts())

# 문제 7. apply 함수 사용하기
p7 = pd.Series([85, 92, 78, 65, 99])
def scoring(x):
    if x > 90:
        return 'A'
    elif x > 80:
        return 'B'
    else:
        return 'C'
p7 = p7.apply(scoring)
print(p7)

