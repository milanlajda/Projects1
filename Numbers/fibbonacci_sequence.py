def fibonacci_sequence(l):
    counter=0
    sn=0
    sn1=1
    sn2=0
    fsequence=[]
    while counter < l:
        if counter == 0:
            fsequence.append(sn)
        elif counter == 1:
            fsequence.append(sn1)
        elif counter > 1:
            fsequence.append(fsequence[counter-2]+fsequence[counter-1])

        counter=counter+1
    print fsequence



fibonacci_sequence(100)
