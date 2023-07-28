
def is_prime(number):
    prime=False
    c=0
    if number>0:
        for i in range(1, number+1):
            if number%i==0:
                c+=1
    else :
        prime = False

    if c>2:
        prime=False
    elif c<=2 and number>0 :
        prime=True
    print(prime)
    '''return prime
is_prime(17)    
is_prime(15)    
is_prime(-5)    
is_prime(0)''' 
