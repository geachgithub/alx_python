def fibonacci_sequence(n):
    num=[]
    i=2
    if n==0:
        num.append(0)
    elif n==1:
        num.append(0)
        num.append(1)
    elif n>1:
        num.append(0)
        num.append(1)
        for i in range(2,n):
            j=i-1
            k=i-2
            num1=num[j]+num[k]
            num.append(num1)
    else :
        num.append()
    print(num)
fibonacci_sequence(100)
