var=1
while var<=9:
    guess= int(input("enter a number"))
    if guess >1 and guess<9:
        print("well done")
        break
    var=var+1
