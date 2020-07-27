# 1.Write a Python program to print the following string in a specific format (see the output).
# def function():
#   text = "Hello\n\t\tworld"
#   return (text)
# print (function())

# 2. Write a Python program to get the Python version you are using
# import sys
# print('Python version is '+sys.version)

# 3. Write a Python program to display the current date and time
# import datetime
# today = datetime.datetime.today()
# print("Current date and time : ")
# print(today.strftime("%Y-%m-%d %H:%M:%S"))

# # 4.1 Write a Python program which accepts the radius of a circle from the user and compute the area
# def area(r):
#     from math import pi
#     result = pi * (r*r)
#     return(result)
#
# x = float(input('enter radius'))
# test=area(x)
# print(f'r = {x}')
# print(f'Area = {test}')

# 4.2
# from math import pi
# r = float(input("Input the radius of the circle : "))
# print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# 5.1 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# name=input("enter your name ")
# surname=input("enter your surname: ")
# print(f'Hello {surname} {name}')

# 5.2
# name = input("enter your name ")
# surname = input("enter your surname: ")
# print('Hello ' + surname + " " + name)

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# numbers = input('enter some space separated numbers: ')
# list = numbers.split(' ')
# tuple = tuple(list)
# print('list: ', list)
# print('Tuple: ', tuple)

# 7. Write a Python program to accept a filename from the user and print the extension of that
# filename=input('enter file name: ')
# list=filename.split('.')
# print('Output: ' + list[1])

# 8. Write a Python program to display the first and last colors from the following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]
# print('the first color is: '+color_list[0]+' and the last is '+color_list[-1])

# 9.1 Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# print('The examination will start from : '+str(exam_st_date[0])+' / '+str(exam_st_date[1])+' / '+str(exam_st_date[2]) )

# 9.2
# exam_st_date = (11,12,2014)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)

# 10.1 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# n=int(input('enter number: '))
# print('The result is :' +str(n+((n*10)+n)+((n*100)+(n*10)+n)))

# 10.2
# a = int(input("Input an integer a: "))
# b = int(input("Input an integer b: "))
# n1 = int( "%i" % a )
# n2 = int( "%i%i" % (a,b) )
# n3 = int( "%i%i%i" % (b,a,a) )
# print (n1)
# print (n2)
# print (n3)
# print (n1+n2+n3)

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# print('abs(17) -> '+str(abs(17)))
# print(abs.__doc__)

# 12. Write a Python program to print the calendar of a given month and year.
# import calendar
# year = int(input('Type year: '))
# month = int(input('Type month: '))
# print(calendar.month(year, month))

################################################################################ 13. Write a Python program to print the following here document. Go to the editor
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# Click me to see the sample solution

# 14. Write a Python program to calculate number of days between two dates.
# from datetime import date
# date1 = date(2014, 7, 2)
# date2 = date(2014, 7, 11)
# delta = date2 - date1
# print(str(delta.days)+" days")

# 15. Write a Python program to get the volume of a sphere with radius 6.
# from math import pi
# r=int(input("Add radius: "))
# d=r*2
# volume=(4/3)*pi*r**3

# 16.1 Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. Go to the editor
# x=int(input('Add number: '))
# if x > 17:
#     y = abs(x - 17) * 2
#     print('x greater than 17, so double result is ', y)
# else:
#     y = 17 - x
#     print('x is smaller than 17 on: ', y)

# 16.2
# def calc(x):
#     if x < 17:
#         return 17 - x
#     else:
#         return (x-17)*2
#
# print(calc(int(input('ghbyn: '))))
# print(calc(6))
# print(calc(117))

# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000. Go to the editor
# def calc(x):
#     result1 = 'is within 2000'
#     result2 = 'is within 1000'
#     if x/100 > 10:
#         return result1
#     else:
#         return result2
# # check = calc(int(input('Enter number from 1 to 1999: ')))
# # print(f'Your number {check}')

# #or 17.1
# print('Your number', calc(int(input('Enter number from 1 to 1999: '))))

# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. Go to the editor
# def calc():
#     a=(int(input('Enter number a: ')))
#     b=(int(input('Enter number b: ')))
#     c=(int(input('Enter number c: ')))
#     if a==b==c:
#         return 3*(a+b+c)
#     else:
#         return a + b + c
# print('Your result is: ', calc())

# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. Go to the editor
# def isinstring(stringtocheck):
#     liststr=stringtocheck.split(' ')
#     if liststr[0] == 'Is':
#         return stringtocheck
#     else:
#         return ('Is '+stringtocheck.lower())
# print(isinstring(str(input('Enter your test to check: '))))

# 19.1
# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str
#
# print(new_string("Array"))
# print(new_string("IsEmpty"))

# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. Go to the editor
# def ncopies(string, n):
#     result = ""
#     for i in range(n):
#         result = result + string
#     return result
# print(ncopies(str(input('add string: ')), int(input('add n: '))))

# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. Go to the editor
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")

# 22. Write a Python program to count the number 4 in a given list. Go to the editor
# def counter(listnumbers, x):
#     count=0
#     for num in listnumbers:
#         if num==x:
#             count=count+1
#     return count
# print(counter([3, 6, 8, 4, 6, 7, 14], 17))

###################################################################################### 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. Go to the editor


# 24. Write a Python program to test whether a passed letter is a vowel or not. Go to the editor
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     if char in all_vowels:
#         return "char is a vowel"
#     else:
#         return "char is NOT vowel"
# print(is_vowel('c'))
# print(is_vowel('e'))

# # 25. Write a Python program to check whether a specified value is contained in a group of values.
# def checker(list1, x):
#     return x in list1
# print(checker([1, 5, 6, 12], 12))
#
#
# # 25.1
# def checker(group_data, n):
#     for value in group_data:
#         if n == value:
#             return True
#     return False
# print(checker([1, 5, 8, 3], 3))
# print(checker([5, 8, 3], -1))

# 26. Write a Python program to create a histogram from a given list of integers. Go to the editor
# def histogram(list, n):
#     for i in list:
#         result = ''
#         times = i
#         while (times > 0):
#             result += n
#             times = times - 1
#         print(result)
# print(histogram([3, 2, 7], "Oo"))

# 27. Write a Python program to concatenate all elements in a list into a string and return it. Go to the editor
# def concatenator(list):
#     result = ''
#     for element in list:
#         result += str(element)
#     return result
# print(concatenator(['test', 'test2', 'test3', 'test4', 4, 'test', 'test2', 'test3', 'test4', 4, 'test', 'test2', 'test3', 'test4', 4, 'test', 'test2', 'test3', 'test4', 4]))

# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
#
# for x in numbers:
#     if x == 237:
#         print(x)
#         break;
#     elif x % 2 == 0:
#         print(x)

# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print(color_list_1.difference(color_list_2))

# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

# 30. Write a Python program that will accept the base and height of a triangle and compute the area. Go to the editor
# def tri_area(b, h):
#     area = 1 / 2 * b * h
#     return str(round(area, 3))
# print('Area is: '+tri_area(float(input('type base: ')), float(input('type height: ')))+' santimeters')

########################################################################## 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. Go to the editor

########################################################################## 32. Write a Python program to get the least common multiple (LCM) of two positive integers. Go to the editor

# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. Go to the editor
# def summ(a, b, c):
#     if a==b or b==c or a==c:
#         return str('0, because two ints are equal')
#     else:
#         return str(a+b+c)
#
# print('Summ is: '+summ(int(input('enter a: ')), int(input('enter b: ')), int(input('enter c: '))))

# 33.1
# def summ(a, b, c):
#     if a==b or b==c or a==c:
#         result=0
#     else:
#         result=a+b+c
#     return result
#
# print(summ(12, 6, 13))
# print(summ(12, 12, 13))
# print(summ(1112, 6, 13))

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. Go to the editor
# def summ(a, b):
#     if a+b in range(15, 20):
#         result=20
#     else:
#         result=a+b
#     return result
#
# print(summ(12, 1))

# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. Go to the editor
# def check(a, b):
#     if a==b or a+b==5 or abs(a-b)==5:
#         return True
#     else:
#         return False
# print(check(6, 6))
# print(check(1, 4))
# print(check(-11, -6))
# print(check(1, 6))
# print(check(27, 6))

# 36. Write a Python program to add two objects if both objects are an integer type. Go to the editor
# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#          raise TypeError("Inputs must be integers")
#     return a + b
#
# print(add_numbers(10, 11.1))

# 37. Write a Python program to display your details like name, age, address in three different lines. Go to the editor
# def userdata():
#     name='Alan'
#     age=16
#     address='Kiev, first street'
#     print('Hi, my name is {}\nI"m {} years\nI leave in {}'.format(name, age, address))
# userdata()

# 38. Write a Python program to solve (x + y) * (x + y). Go to the editor
# def calc(x, y):
#     result = (x + y) * (x + y)
#     return print("({} + {}) ^ 2) = {}".format(x, y, result))
# calc(7, 3)

# 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. Go to the editor
# def future_value(amt, interest, years):
#     result=amt*((1+(0.01*interest))**years)
#     return print(result)
# future_value(10000, 3.5, 7)

# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# import math
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
#
# print(distance)

# 41. Write a Python program to check whether a file exists. Go to the editor
# import os.path
# open('abc.txt', 'w')
# print(os.path.isfile('abc.txt'))

# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. Go to the editor
# import struct
# print(struct.calcsize("P") * 8)

# 43. Write a Python program to get OS name, platform and release information. Go to the editor
# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

# 44. Write a Python program to locate Python site-packages. Go to the editor
# import site;
# print(site.getsitepackages())

# 45. Write a python program to call an external command in Python. Go to the editor
# from subprocess import call
# call(["ls", "-l"])

# 46. Write a python program to get the path and name of the file that is currently executing. Go to the editor
# import os
# print("Current File Name : ",os.path.realpath(__file__))

# 47. Write a Python program to find out the number of CPUs using. Go to the editor
# import multiprocessing
# print(multiprocessing.cpu_count())

# 48. Write a Python program to parse a string to Float or Integer. Go to the editor
# n = "246.2458"
# print(float(n))
# print(int(float(n)))

# 49. Write a Python program to list all files in a directory in Python. Go to the editor
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
# print(files_list);

# 50. Write a Python program to print without newline or space. Go to the editor
# for i in range(0, 10):
#     print('*', end="")
# print("\n")

# 51. Write a Python program to determine profiling of Python programs. Go to the editor
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
# Click me to see the sample solution
#
# 52. Write a Python program to print to stderr. Go to the editor
# Click me to see the sample solution
#
# 53. Write a python program to access environment variables. Go to the editor
# Click me to see the sample solution
#
# 54. Write a Python program to get the current username Go to the editor
# import getpass
# print(getpass.getuser())
# 55. Write a Python to find local IP addresses using Python's stdlib Go to the editor
# Click me to see the sample solution
#
# 56. Write a Python program to get height and width of the console window. Go to the editor
# Click me to see the sample solution
#
# 57. Write a program to get execution time for a Python method. Go to the editor
# import time
# def sum_of_n_numbers(n):
#     start_time = time.time()
#     s = 0
#     for i in range(1,n+1):
#         s = s + i
#     end_time = time.time()
#     return s,end_time-start_time
#
# n = 5
# print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))
# 58. Write a python program to find the sum of the first n positive integers. Go to the editor
# Click me to see the sample solution

# 59. Write a Python program to convert height (in feet and inches) to centimeters. Go to the editor
# print("Input your height: ")
# h_ft = int(input("Feet: "))
# h_inch = int(input("Inches: "))
#
# h_inch += h_ft * 12
# h_cm = round(h_inch * 2.54, 1)
#
# print("Your height is : %d cm." % h_cm)

# 60. Write a Python program to calculate the hypotenuse of a right angled triangle. Go to the editor
# Click me to see the sample solution
# from math import sqrt
# print("Input lengths of shorter triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))
#
# c = sqrt(a**2 + b**2)
# print("The length of the hypotenuse is", c )

# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. Go to the editor
# d_ft = int(input("Input distance in feet: "))
# d_inches = d_ft * 12
# d_yards = d_ft / 3.0
# d_miles = d_ft / 5280.0
#
# print("The distance in inches is %i inches." % d_inches)
# print("The distance in yards is %.2f yards." % d_yards)
# print("The distance in miles is %.2f miles." % d_miles)

# 62. Write a Python program to convert all units of time into seconds. Go to the editor
# days = int(input("Input days: ")) * 3600 * 24
# hours = int(input("Input hours: ")) * 3600
# minutes = int(input("Input minutes: ")) * 60
# seconds = int(input("Input seconds: "))
#
# time = days + hours + minutes + seconds
#
# print("The  amounts of seconds", time)

# 63. Write a Python program to get an absolute file path. Go to the editor
# Click me to see the sample solution
#
# 64. Write a Python program to get file creation and modification date/times. Go to the editor
# Click me to see the sample solution
#
# 65. Write a Python program to convert seconds to day, hour, minutes and seconds. Go to the editor
# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

# 66. Write a Python program to calculate body mass index. Go to the editor
# height = float(input("Input your height in meters: "))
# weight = float(input("Input your weight in kilogram: "))
# print("Your body mass index is: ", round(weight / (height * height), 2))

# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure. Go to the editor
# kpa = float(input("Input pressure in in kilopascals> "))
# psi = kpa / 6.89475729
# mmhg = kpa * 760 / 101.325
# atm = kpa / 101.325
# print("The pressure in pounds per square inch: %.2f psi"  % (psi))
# print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
# print("Atmosphere pressure: %.2f atm." % (atm))

# from math import pi
# print("Точность плавающей точки для PI: %.2f, %.4f, %.8f" % (pi,pi,pi))
# print(round(pi, 2))

# 68. Write a Python program to calculate the sum of the digits in an integer. Go to the editor
# 68.1
# a = int(input('add integer: '))
# print(len(str(a)))

# 68.2
# a = int(input('add integer: '))
# list1=list(str(a))
# print(list1)
# print(sum((int(list1[i]) for i in range(0, int(len(list1))))))

# 68.3
# def sum_elements(a):
#     list1=list(str(a))
#     return list1
# a = int(input('add integer: '))
# sum_e=sum_elements(a)
# print(sum((int(sum_e[i]) for i in range(0, int(len(sum_e))))))

# 69. Write a Python program to sort three integers without using conditional statements and loops. Go to the editor
# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# z = int(input("Input third number: "))
#
# a1 = min(x, y, z)
# a3 = max(x, y, z)
# a2 = (x + y + z) - a1 - a3
# print("Numbers in sorted order: ", a1, a2, a3)

# 70. Write a Python program to sort files by date. Go to the editor
# import glob
# import os
#
# files = glob.glob("*.py")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))

# 71. Write a Python program to get a directory listing, sorted by creation date. Go to the editor


# 72. Write a Python program to get the details of math module. Go to the editor
# Imports the math module
# import math
# #Sets everything to a list of math module
# math_ls = dir(math) #
# print(math_ls)

# 72.1
# int_list = dir(int)
# int_list1=list(int_list)
# print(int_list1)
# print(int_list)

# 73. Write a Python program to calculate midpoints of a line. Go to the editor

# 74. Write a Python program to hash a word. Go to the editor
# Click me to see the sample solution
#
# 75. Write a Python program to get the copyright information. Go to the editor
# import sys
# # print("\nPython Copyright Information")
# print(sys.copyright)
# # print()

# 76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. Go to the editor
# Click me to see the sample solution
#
# 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform. Go to the editor
# Click me to see the sample solution
#
# 78. Write a Python program to find the available built-in modules. Go to the editor
# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(textwrap.fill(module_name, width=70))

# 79. Write a Python program to get the size of an object in bytes. Go to the editor
# import sys
# str1 = "one21212121212121"
# str2 = "four"
# str3 = "three"
# print()
# print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
# print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
# print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
# print()

# 80. Write a Python program to get the current value of the recursion limit. Go to the editor
# import sys
# print()
# print("Current value of the recursion limit:")
# print(sys.getrecursionlimit())


################################################################ STRING ##########################################################################
# 1
# def string_length(str1):
#     result = len(str1)
#     return result
# print(string_length(input("Type something: ")))





# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). Go to the editor

# def repitor(text):
#     if len(text) > 2:
#         list1 = list(str(text))
#         result = str((list1[-2] + list1[-1])*4)
#         return print(result)
#     else:
#         return print("type another")
# repitor("f")

# 17.2
# def repitor(text):
#     new_str = text[-2:]
#     result = new_str * 4
#     return print(result)
# repitor("AlanWake")

# 18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.

# def three_char(text):
#     if len(text) < 3:
#         return print(text)
#     else:
#         result = text[:3]
#         return print(result)
# three_char("te")

# 19. Write a Python program to get the last part of a string before a specified character. Go to the editor
# def splitter(text):
#     result = text.rsplit('/')[-1]
#     return print(result)
# splitter('https://www.w3resource.com/python-exercises')

# 19.2
# def splitter(text):
#     list1 = text.split('/')
#     return print(list1[-1])
# splitter('https://www.w3resource.com/python-exercises')

# 20. Reverse a string if it's length is a multiple of 4

# def reverse_string(str1):
#     if len(str1) % 4 == 0:
#        return ''.join(reversed(str1))
#     return str1
#
# print(reverse_string('abcd'))
# print(reverse_string('python'))

# 20.2
# def reverse_string(str1):
#     result = ''
#     if len(str1) % 4 == 0:
#         return result.join(reversed(str1))
#     else:
#         return print('error')
#     return result
#
# print(reverse_string('abcd'))
# print(reverse_string('python11'))

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

# def to_uppercase(text):
#     counter = 0
#     for symbol in text[:4]:
#         if symbol.upper() == symbol:
#             counter += 1
#     if counter >= 2:
#         return text.upper()
#     return text
#
#
# print(to_uppercase('teststing125'))
# print(to_uppercase('tesuusstsTIng125'))

# 22.Write a Python program to sort a string lexicographically.
# def lexicographically(text):
#     return sorted(text)
# print(lexicographically("AlanWake"))
#
# def lexicographically1(text):
#     return sorted(sorted(text), key=str.lower)
# print(lexicographically1("AlanWake"))

# # 23. Write a Python program to remove a newline in Python.
# str1 = 'Python Exercises\n'
# print(str1)
# print(str1.rstrip())

# 24. Write a Python program to check whether a string starts with specified characters.
# string = "w3resource.com"
# print(string.startswith("w3r"))

# 25. Write a Python program to create a Caesar encryption.


#
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
