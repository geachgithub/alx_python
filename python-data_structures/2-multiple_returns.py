
def multiple_returns(sentence):
    length=len(sentence)
    if sentence=='':
        return(length, 'none')
        #print('none')
    else :
        return(length,sentence[0])
        '''print('Length : {:d} - first character: {}'.format(length, sentence[0]))
multiple_returns('kwfkkf')'''