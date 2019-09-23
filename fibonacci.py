
# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    # b=1; a=0; a+b=1; 
    # a=1; b=1; a+b=2;
    # a=1; b=2; a+b=3;
    # =为赋值，非等于。

    a, b = b, a + b 


print() # line ending
