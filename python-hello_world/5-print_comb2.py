for i in range(99):
    print('{:02d}'.format(i,), end=', ' )
    if i==98:
        print('{}'.format(i+1), end="\n")
        break