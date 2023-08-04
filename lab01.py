# #1
# print("Twinkle, twinkle, little star,\n \tHow I wonder what you are!\n \t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
# ------------------------------

# #2
# import sys
# print(sys.version)
# ------------------------------

# #3
# import datetime
# timenow = datetime.datetime.now()
# print(timenow)
# ------------------------------

# #4
# from math import pi
# r = float(input("input radius:" ))
# print("area: "+ str(pi * r**2))
# ------------------------------

# #5
# first_name = input("input first name: ")
# last_name = input("input last name: ")
# print(last_name, first_name)
# ------------------------------

# #6
# nums = input("input a number list: ")
# list = nums.split(",")
# tuple = tuple(list)
# print(list)
# print(tuple)
# ------------------------------

# #7
# filename = input("input file name: ")
# file_extent = filename.split(".")
# print("file type is:", file_extent[-1])
# ------------------------------

# #8
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1],)

# 9
# exam_st_date = (11, 12, 2014)
# exam_st_date2 = [11, 12, 2014]
# print("%i / %i / %i"%exam_st_date)
# print("{}/{}/{}".format(*exam_st_date))
# ------------------------------

# 10
# def calculate_integer_series(start, base):
#     root = start
#     result = 0
#     for i in range(base):
#         print(start)
#         result += start
#         start = start * 10 + root
#     print(result)

# calculate_integer_series(5, 3)
# ------------------------------


# #11
# print(abs.__doc__)
# ------------------------------

# # 12
# import calendar

# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))
# ------------------------------

# 13
# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)
# ------------------------------

# # 14
# from datetime import date

# f_date = date(2023, 8, 1)
# l_date = date(2023, 8, 10)
# delta = l_date - f_date
# print(delta.days)
# ------------------------------


# 15
# import math

# def get_volume(r):
#     return 4 / 3 * math.pi * r**3

# print(get_volume(6))

# r = int(input("Nhap ban kinh: "))
# print("the tich hinh cau ban kinh r: {} la {}".format(r, 4 / 3 * math.pi * r**3))
# -------------------


# # 16
# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2


# print(difference(22))
# print(difference(14))
# ------------------------------


# # 17
# def kiem_tra(n):
#     return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)

# print(kiem_tra(600))
# ------------------------------


# # 18
# def sum(a, b, c):
#     if a == b == c:
#         return a**3
#     return a + b + c


# print(sum(3, 3, 3))
# ------------------------------

# 19
# def new_string(text):
#   if len(text) >= 2 and text [:2] == "Is":
#     return text
#   return "Is" + text
# print(new_string("Array"))
# print(new_string("IsEmpty"))
# ------------------------------


# # 20
# def copy(string, time):
#     result = ""
#     for x in range(time):
#         result = result + string
#     return result

# print(copy("ab", 3))
# ------------------------------


# # 21
# def check_number(n):
#     if n % 2 == 0:
#         return "{} is even".format(n)
#     return "{} is odd".format(n)

# print(check_number(15))
# print(check_number(8))
# ------------------------------


# 22
# def count_4(list):
#     count = 0
#     for num in list:
#         if num == 4:
#             count += 1
#     return count

# print(count_4([1, 2, 3, 4, 4]))
# ------------------------------


# 23
# def copy_2_first_char(string, time):
#     result = ""
#     if len(string) < 2:
#         result = string
#     else:
#         for x in range(time):
#             result = result + string[0:2]
#     return result


# print(copy_2_first_char("abcde", 3))
# print(copy_2_first_char("fg", 2))
# ------------------------------


# 24
# vowels = ["o","e","a","o","i"]
# def is_vowel(char):
#     if char in vowels:
#         return True
#     return False

# print(is_vowel("w"))
# ------------------------------

# 25
# def contain(data, n):
#     for value in data:
#         if n in data:
#             return True
#         return False
# print(contain([1,2,3,4], 5))
# ------------------------------


# ------------------------------
# import math


# def ktra_nguyento(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n))):
#         if n % i == 0:
#             return False
#     return True


# def in_songuyento(n):
#     for i in range(n):
#         if ktra_nguyento(i):
#             print(i)


# in_songuyento(100)
# ------------------------------
