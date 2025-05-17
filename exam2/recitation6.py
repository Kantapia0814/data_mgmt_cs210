import re
# GPT problem 1 - 숫자만 찾기
text1 = "My age is 25 and my brother is 30 years old."
# answer = re.search(r'[1-9]\d{0,5}', text1)
answer = re.findall(r'[1-9]\d+', text1)
print(answer)

# GPT problem 2 - 이메일 찾기
text2 = "Contact me at hello123@gmail.com or at work_email@company.com"
answer = re.findall(r'\w+\@\w+\.com', text2)
print(answer)

# GPT problem 3 - 같은 문자로 시작하고 끝나는 소문자 단어 찾기
text3 = "madam went to level racecar not car"
answer = re.compile(r'\b([a-z])[a-z]*\1\b')
for match in answer.finditer(text3):
    print(match.group())

# problem 1
# 1-1 정수만, 앞뒤 공백
re.compile(r'\s\$[1-9]\d{0,5}\s')
# 1-2 소수점 두자리 포함
re.compile(r'\s\$[1-9]\d{0,5}\.\d{2}\s')
# 1-3 (2)의 패턴에서 달러와 센트 값을 그룹으로 추출
re.compile(r'\$([1-9]\d{0,5})\.(\d{2})')
# 1-4 소문자로만 된 단어 중 시작과 끝이 같은 것
re.compile(r'\b([a-z])[a-z]*\1\b')
# 1-5 정수형 달러 또는 소수점 달러 모두 인식
re.compile(r'\s\$(?:[1-9]\d{0,5}|\d{1,6}\.\d{2})\s')
# 1-6 문자로 시작, . , ; 가 아니고 숫자로 끝나지 않기
re.compile(r'^[a-zA-Z][^.,;]+[^0-9]$')

# problem 2
sentence = "The wind flows through the mountains and into the river."

cutting = r'^The.*\bmountains\b.*river\.$'
if (re.search(cutting, sentence)):
    print("True")
    sentences = sentence.split('mountains')
    for i in range(len(sentences)):
        print(sentences[i].strip())
else :
    print("False")

# problem 3
# 한 줄이 쉼표(,)로 구분된 데이터
# 이름이 a로 시작하고, 두 번째 항목이 student이며, 세 번째 항목이 존재하는 3필드 데이터
filter = re.compile(r'^a[^,]*,student\,[^,]+$')

with open("people.txt", "r") as input, open("astudents.txt", "w") as output:
    for line in input:
        if (filter.search(line.strip())):
            output.write(line)

# problem 4
# 소문자 알파벳 또는 _로 시작
name_filter = re.compile(r'^[a-z_]')
# 적어도 하나의 대문자(A~Z)가 포함
pw_filter = re.compile(r'[A-Z]')
# 영문자로 시작 + 올바른 이메일 구조
email_filter = re.compile(r'^[a-zA-Z][^@]+@[a-zA-Z][^@]*$')

def makeID(name, pw, email):
    while True:
        name = input("What is your name : ")
        if name_filter.match(name):
            break
        else:
            print("Username must start with a lowercase letter or underscore.")
    while True:
        pw = input("What is your password : ")
        if len(pw) >= 6 and pw_filter.search(pw):
            break
        else:
            print("Password must be at least 6 characters long and include an uppercase letter.")
    while True:
        email = input("Enter email: ")
        if email_filter.match(email):
            break
        else:
            print("Email must start with a letter and have one '@' followed by a letter.")

    print("\nSignup successful!")
    print(f"Username: {name}")
    print(f"Email: {email}")

