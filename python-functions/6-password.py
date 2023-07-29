
def validate_password(password):
    l,u,d,s=0,0,0,0
    word=password
    if len(word)>8:
        for i in word:
            if (i.islower()):
                l+=1
            if (i.isupper()):
                u+=1
            if (i.isdigit()):
                d+=1
            if (i==" "):
                s+=1
    if (l>0 and u>0 and d>0 and s==0):
        #print('good')
        return True
    else :
        return False
        #print('bad')
#validate_password('Getachew1234')