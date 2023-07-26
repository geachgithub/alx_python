import random
number=random.randint(-10000, 10000)
l_digit=number%10
if l_digit>5:
    text='and is greater than 5'
elif l_digit==0:
    text='and is 0'
elif l_digit<6 and l_digit!=0:
    text='and is less than 6 and not 0'
print('Last digit of {} is {} {} '.format(number,l_digit,text))