# Reading File

# read(): 전체 내용 읽기
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# readline(): 한 줄씩 읽기
with open("example.txt", "r") as file:
    line = file.readline()
    print(line)

# readlines(): 모든 줄을 리스트로 반환
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Writing File

# write(): 파일 쓰기
with open("example.txt", "w") as file:
    file.write("Jisung Park\n")

# writelines(): 여러 줄 쓰기
lines = ["Fernando Torres\n", "Sergio Ramos\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)
# w모드 -> 기존 파일 내용을 초기화하고 새로운 내용을 작성할 때 사용용

# a 모드로 내용 추가
with open("example.txt", "a") as file:
    file.write("Kaka\n")
# a모드 -> 기존 내용을 유지하면서 새로운 내용을 추가할 때 사용

# 첫 번째 파일 처리
# 파일을 한 줄씩 읽어 단어들을 분리한 후, 1. 평균 단어 길이 2. 길이가 3보다 큰 단어들의 개수 계산
def compute_word_stats(file_path):
    total_words = 0
    total_length = 0
    words_greater_than_3 = 0

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()    # 공백을 기준으로 단어 분리
            for word in words:
                word_length = len(word)
                total_words += 1
                total_length += word_length
                if word_length > 3:
                    words_greater_than_3 += 1
    
    average_word_length = total_length / total_words if total_words > 0 else 0
    return average_word_length, words_greater_than_3

file_path = "metamorphosis.txt"
print(compute_word_stats(file_path))

# 두 번째 파일 처리
# 파일을 읽어 (제작연도, 영화제목) 튜플로 변환 후, 연도별로 정렬하는 기능
def generate_sorted_movie_list(file_path):
    movie_list = []

    with open(file_path, 'r') as file:
        for line in file:
            movie, year = line.split(':')
            movie_list.append((int(year.strip()), movie.strip()))   # 튜플로 리스트에 저장
    
    sorted_movie_list = sorted(movie_list, key=lambda x: x[1])  # 영화 제목을 기준으로 정렬
    return sorted_movie_list

file_path = "oscars.txt"

print(generate_sorted_movie_list(file_path))

# 세 번째 파일 처리
# 파일을 읽어 (나라, 인구) 튜플의 리스트를 생성하여 반환
def getPopulations(file):
    pops = []
    for line in open(file): # open()을 직접 호출하면, 기본적으로 파일을 읽기 모드('r')로 연다
        # 파일을 자동으로 닫아주진 않음
        country, pop = line.split('|')
        population = int(pop.replace(',', ''))
        pops.append((country, population))
    return pops

populations = getPopulations('population.txt')
print(populations[:5])

# 특정 나라의 인구 찾기
def find_tuple_by_first_item(tuples_list, value):
    for tup in tuples_list:
        if tup[0] == value:
            return tup
    return None

found_tuple = find_tuple_by_first_item(populations, 'France')
print(found_tuple)

# 더 간결한 버전
def find_tuple_by_first_item2(tuples_list, value):
    return next((tup for tup in tuples_list if tup[0] == value), None)
# next()를 이용해 첫 번째로 일치하는 값 반환
# 없으면 기본값 None 반환

# 네 번째 파일 처리
# 오스카 영화 데이터를 가공해 정렬하기
def read_and_write_oscars(file_path, output_path):
    movie_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                movie, year = line.split(':')
                movie_list.append((int(year.strip()), movie.strip()))

    movie_list.sort(reverse=True, key=lambda x: x[0])

    with open(output_path, 'w') as file:
        for year, movie in movie_list:
            file.write(f"{year} {movie}\n")

read_and_write_oscars("oscars.txt", "oscars2.txt")

# Note - words = line.split(' ', 1)
# 공백(스페이스)를 기준으로 분리,  최대 한 번만(split count=1) 나눔