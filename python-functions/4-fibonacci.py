def fibonacci_sequence(n):
    num=[]
    i=3
    if n==1:
        num.append(0)
    elif n==2:
        num.append(0)
        num.append(1)
    elif n>2:
        num.append(0)
        num.append(1)
        for i in range(2,n):
            j=i-1
            k=i-2
            num1=num[j]+num[k]
            num.append(num1)
    return num
    '''print(num)
fibonacci_sequence(0)
fibonacci_sequence(1)
fibonacci_sequence(2)
fibonacci_sequence(6)
fibonacci_sequence(20)'''



