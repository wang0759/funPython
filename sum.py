# encoding: utf-8
'''
@author: QuanyiWang
@contact: wangquanyi888@gmail.com
@file: sum.py
@time: 2019-09-14 22:06
'''

def sum(n):
    sum=0
    while n>=1:
        sum = sum + n
        n=n-1
    return sum

sum=sum(100)
print(sum)



