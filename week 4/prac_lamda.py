lst1 = [3, 2, 4, 1, 5, 9, 3, 1]
lst1.sort()
print(lst1)

lst1.sort(reverse=True)
print(lst1)

lst2 = [3, -2, 4, 1, -5, 9, 3, -1]
lst2.sort(key=abs)
print(lst2)

lst3 = [3, -2, 4, 1, -5, 9, 3, -1]
lst3_sort = sorted(lst3, reverse=True)
print(f"original list : {lst3}")
print(f"sorted list : {lst3_sort}")

lam = lambda a, b: a + b
print(lam(3, 4))

lam1 = lambda tup: tup[0] / tup[1]
print(lam1((3, 2)))

lam2 = lambda x, y, z=0: x + y + z
print(lam2(3, 4))       # 기본값 z=0 적용
print(lam2(3, 4, 5))    # 기본값 무시하고 z=5 적용

lst2.sort(key=lambda x: abs(x))
print(f"using lambda : {lst2}")

courses = ['math250', 'cs210', 'cs344', 'cs323', 'phy161', 'phy313']
print(sorted(courses))     # 기본적인 사전순 정렬
print(sorted(courses, key=lambda x: x[-3:]))   # 숫자 기준 정렬

words = ["What", "goes", "around", "comes", "around"]
sentence = " ".join(words)
print(sentence)

print("@".join(["jini8014", "naver.com"]))