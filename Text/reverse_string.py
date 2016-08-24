def reverse_string(str):
    #veta=str(a)
    revstr = []
    limit = len(str)
    for x in range (0, len(str)):
        revstr.append(str[limit-x])
    print revstr




reverse_string("abcd")
#reverse_string("12345")
#reverse_string("asdfghj")