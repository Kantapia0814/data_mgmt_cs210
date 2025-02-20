# 리스트의 탐색의 시간복잡도: O(n)
# 딕셔너리는 해시 테이블 기반이기에 검색 속도 빠름: O(1)

# 1. 딕셔너리 생성
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# dict() 함수 사용
my_dict = dict(name='Alice', age=25, city='New York')

# 키-값 쌍을 리스트-튜플 형태로 전달
my_dict = dict([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# 2. 딕셔너리 값 접근

# 키를 사용해 값 가져오기
print(my_dict['name'])
print(my_dict['age'])   # 키가 없으면 KeyError 발생

# get() 사용하기
print(my_dict.get('name'))
print(my_dict.get('gender', 'Not Found'))   # 키가 없으면 기본값 반환

# 3. 딕셔너리 값 변경 & 추가

# 값 변경
my_dict['age'] = 30 # 기존 키의 값을 변경
print(my_dict)

# 값 추가
my_dict['gender'] = 'Female'
print(my_dict)

# 4. 딕셔너리 키-값 삭제 

# 특정 키 삭제
del my_dict['city']
print(my_dict)

# pop() 사용 → 키를 삭제하면서 값 반환
age = my_dict.pop('age')
print(age)
print(my_dict)

# 전체 삭제
my_dict.clear()
print(my_dict)

# 5. 딕셔너리 반복문 활용
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 키 반복
for key in my_dict:
    print(key, my_dict[key])

# value 반복
for value in my_dict.values():
    print(value)

# 키-값 반복
for key, value in my_dict.items():
    print(f'{key}: {value}')

# 데이터를 읽고 딕셔너리로 저장
file_path = "population.txt"
country_population = {}

with open(file_path, 'r') as file:
    for line in file:
        country, population = line.strip().split('|')
        country_population[country] = int(population.replace(',', ''))

# 특정 국가의 인구 조회
def get_population(country):
    return country_population.get(country, "Country not found")

# 전체 인구 합계 계산
def get_total_population():
    return sum(country_population.values())

# 평균 인구 계산
def get_average_population():
    return get_total_population() / len(country_population)

# 가장 인구 많은 국가 찾기
def get_max_population():
    max_country = max(country_population, key=country_population.get)
    return max_country, country_population[max_country]

max_country, max_population = get_max_population()
print(f"Country with max population: {max_country}, Population: {max_population}")

# 인구 3억 이상인 나라 찾기
large_countries = [c for c, p in country_population.items() if p > 300000000]
print(large_countries)
