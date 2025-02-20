# Counter
# collections.Counter는 리스트, 문자열 등 iterable 객체에서 요소의 빈도를 쉽게 셀 수 있는 자료구조
# dict와 비슷하지만, 값이 각 요소의 등장 횟수가 됨

# 점수 빈도수 세기
from collections import Counter

quiz_scores = [85, 92, 85, 91, 75, 92, 85, 100, 76, 85, 75, 92]

score_frequencies = Counter(quiz_scores)

for score, frequency in score_frequencies.items():
    print(f"Score: {score}, Frequency: {frequency}")

# 매서드 사용 예제

# most_common(n): 가장 많이 등장한 n개의 요소 반환환
print("Most common scores:", score_frequencies.most_common(3))

# update(iterable): 다른 Counter나 리스트를 추가
score_frequencies.update([85, 100, 92])
print("Updated frequencies:", score_frequencies)

# subtract(iterable): 기존 Counter에서 값 감소
score_frequencies.subtract([85, 100])
print("After subtraction:", score_frequencies)

# total(): 전체 개수 합산
print("Total scores counted:", score_frequencies.total())

from collections import Counter

word_counts = Counter()

# 문서 단어 분석

word_counts = Counter()

with open("metamorphosis.txt") as file:
    for line in file:
        tokens = line.split()  
        for token in tokens:
            word_counts.update([token.lower().strip(",.")])

for word, count in word_counts.most_common(5):
    print(word, count)

commons = [(w, c) for w, c in word_counts.most_common() if len(w) > 3 and c > 1]
print(commons[:5])  # 길이가 4 이상이고 2번 이상 등장한 단어 5개 출력