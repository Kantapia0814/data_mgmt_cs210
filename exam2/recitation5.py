import csv
import json

# problem 1
# countries.txt 파일을 읽고, 
# 특정 조건을 만족하는 데이터(지역 ID가 1번인 나라들)의 평균 인구 수를 계산
popSum = 0
popCnt = 0
with open('countries.txt', 'r') as f:
    reader = csv.DictReader(f, fieldnames=['id', 'name', 'region', 'population'], delimiter=' ')
    for row in reader:
        values = list(row.values())
        if 'NA' in values or 'na' in values:
            continue
        if int(row['region']) == 1:
            print(','.join(values))
            popSum += int(row['population'])
            popCnt += 1
print("Average population of countries in region 1: ", popSum/popCnt)

# problem 2
with open("departments.csv", "r", newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    data = [line for line in reader]

maxSalary = 0
department = ''
for row in data:
    if len(row[2].strip()) == 0:
        row[2] = '000'
    avgSalary = int(row[3])
    if avgSalary > maxSalary:
        maxSalary = avgSalary
        department = row[1]

with open("departments_upd.csv", "w", newline='') as csvout:
    writer = csv.writer(csvout)
    writer.writerow(header)
    writer.writerows(data)

print("Department with highest salary is: ", department)

# problem 3
# CSV 파일에서 부서 정보 읽고, 
# 최고 평균 급여를 가진 부서를 찾아 저장하는 작업
with open("departments.csv", "r", newline='') as input:
    reader = csv.DictReader(input, fieldnames=['department_id', 'department_name', 'manager_id', 'avg_salary'], delimiter= ' ')
    data = [line for line in reader]
maxSalary = 0
department = ''
for row in data:
    values = list(row.values())
    if len(row['manager_id'].strip()) == 0:
        row['manager_id'] = '000'
    avgSalary = int(values[3])
    if avgSalary > maxSalary:
        maxSalary = avgSalary
        department = values[1]

with open("departments_upd.csv", "w", newline='') as output:
    writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(data)
print("Department with highest salary is: ", department)

# problem 4
person_dict = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
# dict → JSON 문자열로 변환
json_string = json.dumps(person_dict, indent=4, sort_keys=True)
print(json_string)

# problem 5
sampleJson = """[
  {
    "id": 1,
    "name": "name1",
    "color": ["red", "green"]
  },
  {
    "id": 2,
    "name": "name2",
    "color": ["pink", "yellow"]
  }
]"""
# problem 5
# JSON 문자열 → Python 리스트로 변환 + 특정 값 추출
data = json.loads(sampleJson)

name_list = []
for items in data:
    name_list.append(items['name'])

# problem 6
sampleJson = """{ 
   "company":{ 
      "employee":[
          {
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }},
         {
         "name":"josh",
         "payable":{ 
            "salary":9000,
            "bonus":100
         }},
         {
         "name":"jake",
         "payable":{ 
            "salary":5000,
            "bonus":200
         }
      }
   ]
}}"""
# problem 6
# emma의 total = salary + bonus
# 전체 직원의 평균 salary 계산
data = json.loads(sampleJson)
emma_total = 0
employee_total = 0
employee_count = 0
for item in data["company"]["employee"]:
    salary = item["payable"]["salary"]
    employee_total += salary
    employee_count += 1
    if item["name"] == "emma":
        emma_total = item["payable"]["salary"] + item["payable"]["bonus"]

print("Emma's total payable amount = ", emma_total)
print("employee's average salary = ", employee_total/employee_count)

# GPT problem 1
with open("employees.json", "r", newline='') as input:
    data = json.load(input)
for item in data:
    item["total_pay"] = item["salary"] + item["bonus"]

with open("updated_employees.json", "w", newline='') as output:
    json.dump(data, output, indent=4)

