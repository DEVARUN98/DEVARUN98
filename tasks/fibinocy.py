def fib(n):
    a=0
    b=1
    if(n==1):
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):#0,1,1,2,3,5
            c=a+b
            a=b
            b=c
            print(c)
fib(8)