# 문제 1: 리스트의 모든 요소를 제곱하기
numbers = [2, 4, 6, 8, 10]
sq_num = [i ** 2 for i in numbers]
print(sq_num)

# 문제 2: 짝수만 필터링하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = [i for i in numbers if i % 2 == 0]
print(even_num)

# 문제 3: 문자열 길이로 정렬하기
words = ["apple", "banana", "kiwi", "cherry", "grape"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# 문제 4: 두 숫자를 더한 후 짝수인지 판별하기
lam = lambda x, y: (x + y) % 2 == 0
print(lam(3, 5))

# 문제 5: 첫 번째 문자가 'A'인 단어만 필터링하기
words = ["Apple", "Banana", "Avocado", "Cherry", "Apricot", "Blueberry"]
filtered_words = [i for i in words if i[0] == 'A']
print(filtered_words)

# 문제 6: 리스트의 곱 구하기 (reduce() 사용)
numbers = [1, 2, 3, 4, 5]

from functools import reduce
fac = reduce(lambda x, y: x * y, numbers)
print(fac)

# 문제 7: 튜플 리스트 정렬하기
points = [(1, 2), (4, 1), (5, -1), (3, 3)]
sorted_tup = sorted(points, key=lambda x: x[1])
print(sorted_tup)

# 문제 8: 특정 문자 포함 단어 필터링
words = ["cat", "dog", "elephant", "tiger", "rabbit"]
filters_words = [[word for j in range(len(word)) if word[j] == 't'] for word in words]
print(filters_words)

# 정답
words = ["cat", "dog", "elephant", "tiger", "rabbit"]
filters_words = list(filter(lambda word: 't' in word, words))
print(filters_words)

# 문제 9: 두 개의 리스트 요소를 합친 새 리스트 만들기
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_lst = [list1[i] + list2[i] for i in range(len(list1))]
print(new_lst)

# 문제 10: 학생 점수 평균 구하기
scores = [80, 90, 70, 85, 95]
aver = reduce(lambda x, y: x + y, scores) / len(scores)
print(aver)