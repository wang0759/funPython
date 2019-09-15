# encoding: utf-8
'''
@author: QuanyiWang
@contact: wangquanyi888@gmail.com
@file: 阶乘.py
@time: 2019-09-15 07:39
'''
def jiecheng(n):
    result = 1
    while n>=1:
        result=result*n
        n=n-1
    return result
jiecheng=jiecheng(5)
print (jiecheng)