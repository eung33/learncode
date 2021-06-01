

# # Tuple, 수정 불가, 속도 빠름
# (name, age, hobby) = ("김종국", 20, "코딩")

# print(name, age, hobby)

# #집합(set), 중복안됨, 순서없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = {"유재석", "박명수"}

# #교집합
# print(java & python)
# print(java.intersection(python))

# #합집합
# print(java | python)
# print(java.union(python))

# #차집합
# print(java - python)
# print(java.difference(python))

# #python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# #java를 잊었어요
# java.remove("김태호")
# print(java)

# #자료구조의 변경
# menu = {"커피", "우유", "쥬스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

#퀴즈 #4
#파이썬 코딩대회, 댓글 이벤트 1명은 치킨, 3명은 커피 쿠폰
#조건 1 : 댓글은 20명이 작성
#조건 2 : 무작위로 추첨, 중복 불가
#조건 3 : random 모듈의 shuffle과 sample활용

# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

# from random import *
# users = list(range(1, 21))
# # print(users)
# # shuffle(users)
# # print(users)

# winners = sample(users, 4)
# print(" --- 당첨자 발표 --- ")
# print(" 치킨 당첨자 : {0}".format(winners[0]))
# print(" 커피 당첨자 : {0}".format(winners[1:]))
# print("축하합니다.!")


# 분기 if for while
# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("커피나왔습니다. {0}".format(customer))

# 퀴즈 #6
# def std_weight(height, gender): #키는 m단위, 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

##module
# import theater_module

# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)

# from theater_module import price_soldier as price
# price(5)


# package 

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()




