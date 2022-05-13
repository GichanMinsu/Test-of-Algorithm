# i=1
# result=0
# while i<1000:
#     if i%3==0:
#         result += i
#     i+=1
# print(result)

# i=1
# while i<6:
#     print("*"*i)
#     i += 1

# numbers = [1,2,3,4,5]
# result = [ n*2 for n in numbers if n % 2 == 1]
# print(result)

# for i in range(10):
#     print(i, end=' ')
      
      
# writedata.py
# f = open("C:/Users/WST-KIM/TestFile.txt", 'w')
# for i in range(1, 11):
#     data = "%d's text.\n" % i
#     f.write(data)
# f.close()

# readline_test.py
# f = open("C:/Users/WST-KIM/TestFile.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# class FourCal:
#     def setdate(self, first, second):
#         self.first = first
#         self.second = second
    
#     def add(self):
#         result = self.first + self.second
#         return result
    
#     def mul(self):
#         result = self.first * self.second
#         return result
    
#     def sub(self):
#         result = self.first - self.second
#         return result
    
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# a.setdate(4,2)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print("{0:0.0f}".format(a.div()))


# class MyError(Exception):
#     def __str__(self):
#         return "허용되지 않는 별명입니다."

# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)
    
    
# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError as e:
#     print(e)

# Q1
# from posixpath import split

# str1 = "a:b:c:d"
# str2 = str1.split(":")
# print(str2)
# str3 = "#".join(str2)
# print(str3)

# Q4
# def overhalf(lists):
#     result = 0
#     for list in lists:
#         if list >= 50:
#             result += list
#     return result

# A = [20, 55, 67, 82, 45, 33 ,90, 87, 100, 25]
# print(overhalf(A))

# Q5
# def fibo(n):
#     if n is 0:
#         return 0
#     elif n is 1:
#         return 1
#     else:
#         return fibo(n-2) + fibo(n-1)
    
# n = int(input("Enter :"))
# for i in range(n):
#     print(fibo(i), end=" ")

# Q6
# empty = input()
# list = empty.split(",")
# result = 0
# print(list)

# for i in list:
#     result += int(i)

# print(result)

