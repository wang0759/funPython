'''
By Quanyi Wang
formula for compound interest
Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.
'''
p=int(input("please enter the principal:"))
n=float(input("please enter the number of times the interest is compounded each year:"))
r=float(input("please enter the annual interest rate:"))
t = int(input("how many years do you want to save the money?"))
finalAmount = p*(1 + r/n)**(n*t)
print(finalAmount)
