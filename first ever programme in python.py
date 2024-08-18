def upperlower():
    string=input("Enter string:")
    up=0
    low=0
    for i in string:
        if(i.islower()):
            low=low+1
        elif(i.isupper()):
            up=up+1
    print("The no. of upper case characters in the string is:",up)
    print("The no. of lower case characters in the string is:",low)
