import numpy as np

# problem 1
X = np.array([
    [5, 6, np.nan, 7],
    [1, np.nan, 0, 5],
    [-1, 5, np.nan, 2]
])

# my solution
for i in range(len(X)):
    for j in range(len(X[i])):
        if np.isnan(X[i][j]):
            X[i][j] = 0

for i in range(len(X)):
    row_mean = np.mean(X[i])
    for j in range(len(X[i])):
        X[i][j] -= row_mean

print(X)

# problem 1
# GPT solution
Y = np.array([
    [5, 6, np.nan, 7],
    [1, np.nan, 0, 5],
    [-1, 5, np.nan, 2]
])

Y = np.nan_to_num(X)    # nan을 0으로
# axis=1 -> 행마다 계산, keepdims=True -> 결과를 (n, 1) 형태로 유지
row_means = Y.mean(axis=1, keepdims=True)   
Y = Y - row_means       # 행 기준으로 평균 빼기
print(Y)

# problem 2
X = np.array([
    [17, 19, 13],  # 학생 1
    [14, 15, 20],  # 학생 2
    [20, 18, 15]   # 학생 3
])
# axis=0 -> 열마다 계산
max_scores = X.max(axis=0)    # 각 퀴즈의 최대 점수
min_scores = X.min(axis=0)    # 각 퀴즈의 최소 점수
avg_scores = X.mean(axis=0)   # 각 퀴즈의 평균 점수
result = []

for i in range(len(max_scores)):
    row = []
    row.append(max_scores[i])
    row.append(min_scores[i])
    row.append(avg_scores[i])
    result.append(row)

result = np.array(result)
print(result)

# problem 2
def getStats(scores):
    res = np.empty((scores.shape[1], 3))
    res[:, 0] = np.max(scores, axis=0)
    res[:, 1] = np.min(scores, axis=0)
    res[:, 2] = np.average(scores, axis=0)
    return res, np.average(scores)

# problem 3
def moveRow(arr):
    # arr[1:] : 두 번째 행부터 끝까지, arr[:1] : 첫 번째 행
    # np.vstack : 수직으로 쌓아서 새로운 배열 리턴
    return np.vstack((arr[1:], arr[:1]))

def moveCol(arr):
    # arr[:, 1:] : 열 1~끝
    # arr[:, :1] : 첫 번째 열 
    return np.hstack((arr[:, 1:], arr[:, :1]))

print(moveRow(X))

# problem 4
arr2 = [[3,1,-2],[1,8,2],[6,1,5]]
ndarray = np.array(arr2)

means = np.mean(ndarray, axis=1, keepdims=True) # 평균  
squared_diff = (ndarray - means) ** 2           # 편차 제곱
row_vars = np.mean(squared_diff, axis=1)        # 평균 (분산 구하기)
row_stds = np.sqrt(row_vars)                    # 루트

print(row_stds)

# problem 5
random_arr = np.random.uniform(5, 10, (5, 3))
for i, row in enumerate(random_arr):
    top2_idx = np.argsort(row)[-2:]  # 상위 2개 (작은→큰)
    top2_idx = top2_idx[::-1]        # 큰→작은 순서로 뒤집기
    top2_values = np.sort(row)[-2:][::-1]   # 값을 출력
    print(f"row {i}: {top2_idx}")
    print(f"row {i}: {top2_values}")
random_arr[random_arr > 8] = 10
random_arr[random_arr < 6] = 5

print(random_arr)


# problem 6
def one_hot_encode(data):
    classes = sorted(set(data))
    class_index = {}
    for i, label in enumerate(classes):
        class_index[label] = i
    
    one_hot = np.zeros((len(data), len(classes)), dtype=int)

    for row_idx, label in enumerate(data):
        col_idx = class_index[label]
        one_hot[row_idx, col_idx] = 1

    return one_hot

# GPT problem 1
scores = np.array([
    [70, 85, 90],
    [60, 95, 88],
    [75, 65, 92],
    [90, 100, 100]
])
row_mean = scores.mean(axis=1)
for i in range(len(row_mean)):
    if row_mean[i] < 80:
        for j in range(len(scores[i])):
            scores[i][j] += 5

row_mean = scores.mean(axis=1, keepdims=True)  # shape: (4, 1)

# 2. 평균이 80보다 작은 학생을 True로 마스킹
mask = row_mean < 80    
scores += (mask * 5)  

scores = np.array([
    [58, 72, 90, 66],
    [88, 94, 85, 91],
    [70, 60, 65, 75],
    [95, 100, 98, 97],
    [55, 59, 60, 62]
])

# 1. 과목별 통계 (열 기준 → axis=0)
max_scores = scores.max(axis=0)
min_scores = scores.min(axis=0)
avg_scores = scores.mean(axis=0)

# (4, 3) 배열 만들기: 과목 수 x [최대, 최소, 평균]
stats = np.stack([max_scores, min_scores, avg_scores], axis=1)

# 2. 학생별 평균 (행 기준 → axis=1)
student_avg = scores.mean(axis=1, keepdims=True)  # (5, 1) 형태 유지

# 평균 70 미만인 학생 마스크
mask = student_avg < 70   # (5, 1) → True/False

# 3. 보정 점수 적용 (True면 +10, False면 +0)
scores += (mask * 10)

# 4. 최대 점수 100으로 제한
scores = np.clip(scores, 0, 100)


board = np.array([
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
])

# 1. 행, 열, 대각선 합 계산
row_sums = board.sum(axis=1)               # 각 행의 합
col_sums = board.sum(axis=0)               # 각 열의 합
main_diag = np.trace(board)                # 왼쪽 → 오른쪽 대각선
anti_diag = np.trace(np.fliplr(board))     # 오른쪽 → 왼쪽 대각선