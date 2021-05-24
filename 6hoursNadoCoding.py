

# Tuple, 수정 불가, 속도 빠름
(name, age, hobby) = ("김종국", 20, "코딩")

print(name, age, hobby)

#집합(set), 중복안됨, 순서없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = {"유재석", "박명수"}

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

#python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊었어요
java.remove("김태호")
print(java)

#자료구조의 변경
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#퀴즈 #4
#파이썬 코딩대회, 댓글 이벤트 1명은 치킨, 3명은 커피 쿠폰
#조건 1 : 댓글은 20명이 작성
#조건 2 : 무작위로 추첨, 중복 불가
#조건 3 : random 모듈의 shuffle과 sample활용

from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
