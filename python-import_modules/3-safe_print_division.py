
def safe_print_division(a,b):
    c=0
    try:
       c = a/b
    except ZeroDivisionError:
       Exception='zero devision error' 
    finally:
        if b!=0:
         print('Inside result: {}'.format(c))
         #print('{}/{}={}'.format(a,b,c))
         return c
        else :
            print('Inside result: {}'.format('None'))
            #print('{}/{}={} '.format(a,b,'None'))

           
#safe_print_division(1,-1)