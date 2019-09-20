# encoding: utf-8
'''
@author: QuanyiWang
@contact: wangquanyi888@gmail.com
@file: 
factorial.py
@time: 2019-09-15 07:39
'''
def factorial(n):
    result = 1
    while n>=1:
        result=result*n
        n=n-1
    return result

factorial=factorial(5)
print (factorial)
