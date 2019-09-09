# a = float(input('请输入'))
# b = float(input('请输入另一个'))
# print('%.2f - %.2f =%.2f'%(a,b,a-b))



# F = float(input('输入华氏度'))
# C = (F-32)/1.8
# print('%.2f 摄氏度'%C)



# year = int (input ('请输入一个年份:>>'))
# if(year % 4 == 0 and year % 100  != 0 )or (year % 400 == 0):
#     print('%d是闰年' % year)
# else:
#     print('%d不是闰年'%year)



# Number = input('请输入一个数字:')
# bai = int(Number[0])
# shi = int(Number[1])
# ge = int(Number[2])
# if bai**3+shi**3+ge**3 == int (Number):
#     print('是水仙花')
# else:
#     print('不是水仙花')



# 作业一
# celsius = float(input('请输入'))
# fahrenheit = (9/5)*celsius+32
# print("%1f华氏度 is %.1f摄氏度" %(celsius,fahrenheit))



# 作业二
# import math
# radius = float(input('请输入圆的半径：'))
# length = float(input('请输入圆柱的高：'))
# area = radius * radius * math.pi
# volume = area * length
# print('面积:%.2f'%area)
# print('体积:%.2f'%volume)



# 作业三
# feet = float(input('请输入英尺数：'))
# meters = feet * 0.305
# print('%.1f feet is %.4fmeters'%(feet,meters))



# 作业四
# M = float(input('请输入按千克计算的水量：'))
# initialTemperature = float(input('请输入水的初始温度：'))
# finalTemperature = float(input('请输入水的最终温度：'))
# Q = M * (finalTemperature - initialTemperature) * 4184
# print('所需能量:%.1f%Q',Q)



# 作业五
# balance = float(input('请输入差额：'))
# interest_rate = float(input('请输入年利率：'))
# insterest = balance * (interest_rate / 1200)
# print('下月需付利息:%.5f'%insterest)



# 作业六
# v0 = float(input('请输入初始速度：'))
# v1 = float(input('请输入末速度：'))
# t = float(input('请输入速度变化所占用的时间：'))
# a = (v1 - v0) / t
# print('平均加速度是:%.4f'%a)



# 作业七
# num = float(input('请输入每月存款数：'))
# rate = 0.05 / 12
# interest = 1 + rate
# count =[0]
# for i in range(6):
#     month = (100 + count[i]) * interest
#     count.append(month)
# print('六个月后的账户总额：%.2f' % count[6])



# 作业八
# num = int(input('请输入1-1000的一个整数：'))
# bai = int(num % 10)
# shi = int(num /10 % 10)
# ge = int(num /100)
# sum = ge + shi + bai
# print('各位数字之和：',sum)



#  作业九
# import math
# r = float(input('请输入五边形顶点到中心的距离：'))
# s = 2*r*math.sin(math.pi/5)
# area = 5*s*s/(4*math.tan(math.pi/5))
# print('五边形的面积%.2f' %area)



# 作业十
# import math
# x1 = float(input('请输入第一个坐标:'))



# 作业十一
# import math
# s = float(input('请输入五角星的边长:'))
# area = (5*s*s)/(4*math.tan(math.pi/5))
# print("输入的面积为:%.2f" %area)



#  作业十二
# a = eval(input('Please input an ASCII code:'))
# b = chr(a)
# print('The character is:',b)


# 作业十三
# import math
# x1,y1 = eval(input('Please input point1(latitude and longitude) in degrees:'))
# x2,y2 = eval(input('Please input point2(latitude and longitude) in degrees:'))
# radius = 6371.01
# x11 = math.radians(x1) 
# y11 = math.radians(y1)
# x22 = math.radians(x2)
# y22 = math.radians(y2)
# d = radius * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11-y22))
# print('The distance between the two points is %5.2f km' %d)



# 作业十四
# a = input("请输入一个四位整数:")
# print(a [::-1])



# 作业十五
# import hashlib
# a = input('请输入一行文本:')
# m = hashlib.md5()
# b = a.encode(encoding='utf-8')
# m.update(b)
# a_md5 = m.hexdigest()
# print('md5加密前为：' + a)
# print('md5加密后为：' + a_md5)



# 作业十六
# name = input("Please input employee's name:")
# hours = eval(input('Please input number of hours worked in a week:'))
# PayRate = eval(input('Please input hourly pay rate:'))
# federalRate = eval(input('Please input federal tax withholding rate:'))
# stateRate = eval(input('Please input state tax withholding rate:'))
# Federal = hours * PayRate * federalRate
# State = hours * PayRate * stateRate
# Gross = hours * PayRate
# NetPay = hours * PayRate - Federal - State
# Total = Federal + State
# print('Employee Name:',name)
# print('Hours Worked:',hours)
# print("Pay Rate:",PayRate)
# print("GrossPay:",Gross)
# print("Deductions:")
# print("\tFederal withholding (20.0%):KaTeX parse error: Expected 'EOF', got '\tState' at position 19:",State)
# print("\̲t̲S̲t̲a̲t̲e̲ ̲withholding (9",State)
# print("\tTotal Deduction:",Total)
# print("NetPay:",NetPay)









