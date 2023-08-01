import sys
l=len(sys.argv)-1
if __name__=="__main__":
    if(l==0):

        print('{} arguments.'.format(l), end='\n')
    elif(l==1):
            print('{} argument:'.format(l))
            print('{}:{}'.format(l,sys.argv[l]), end='\n')
    else :
        m=1
        print('{} arguments:'.format(l), end='\n')
        for i in sys.argv:
            if i!=sys.argv[0]:
                print('{}:{}'.format(m,i), end='\n')
                m+=1
