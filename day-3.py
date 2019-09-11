# def main(a):
#     if a%2 ==0:
#         print('偶数')
#     else:
#         print('奇数')
# main(10)

# def main(a):
#     for i in range(2,a):
#         if(a % i) == 0:
#             print(a,'不是素数')
#             break
#         else:
#            print(a,'是素数')
#         break
# main(7)
# import random
# import numpy as np
# COUNT = 1
# def main(u,p):
#     global COUNT
#     u = input('请输入账号')
#     p = input('请输入密码')
#     y = random.randrange(1000,9999)
#     res = int(input('验证码是：%d' %y))
#     np.random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
# ])
#     if res == y: 
#            if u == 'admin' and p == '123456':
#               print('登录成功') 
#     else:
#         print('验证码错误，请重新输入')
#         if COUNT !=3:
#             COUNT += 1
#             main(u,p)
#         else:
#             print('尝试次数达到上限,请去客服咨询,客服电话:13838384381')
# main('admin','123456')

# # pyMySQL,函数体内需要改变外部变量需要global
# def login():
#     username = input('zhang')
#     password = input('zhang')
#     if username == '' and password == '':  
# def verify():
# def verify():
#     pass

# def error():
#     pass

# def API():
#     pass

# def start():
#     login





#  作业一：
# def getPentagonalNumber(n):
#     count=0
#     for i in range(1,n+1):
#         num = i*(i*3-1)/2
#         print('%d' %num,end = ' ')
#         count +=1
#         if count % 10 ==0:
#             print('\n')
# getPentagonalNumber(100)

# 作业二：
# def sumDigits(n):
#     count = 1
#     nu = input('请输入一个整数:>>')

# # 作业三：
# def displaySortedNumbers(num1,num2,num3):
#     num1,num2,num3 = map(int(input('请输入三个整数:>>'))).split(',')


# 作业四：
# def printChars():
#     for i in range(73,91):
#         print(chr(i),end=" ")
#         if i% 10 == 0:
#             print("\n")
# printChars()

# 作业五：
# def numberOfDaysInAYear(year):
#     for count in range(year,year+11):
#         if count % 4 == 0 and count % 100 != 0 or count % 400 == 0:
#             print("{}年有366天".format(count))
#         else:
#             print("{}年有365天".format(count))
# numberOfDaysInAYear(2016)

# 作业六：
# def distance(x1,x2,y1,y2):
#     dis =((x2-x1)**2+(y2-y1)**2)**0.5
#     print("这两点的距离是: %f" %dis)
# distance(1,4,4,2)

# 作业七：
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print("本地时间为 :", localtime)
# main()

# 作业八:
# import random
# def sz():
#     a=random.choice([1,2,3,4,5,6])
#     b=random.choice([1,2,3,4,5,6])
#     if a+b==2 or  a+b==3 or a+b==12:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你输了')
#     elif a+b==7 or a+b==11:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你赢了')
#     else:
#         print('%d + %d = %d' %(a,b,a+b))
#         c=random.choice([1,2,3,4,5,6])
#         d=random.choice([1,2,3,4,5,6])
#         if c+d==7:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你输了')
#         elif c+d==a+b:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你赢了')
# sz()



    








    




    



