num=int(input("enter a number"))
count=2
position=0
while num!=0:
    i=2
    while i<count:
        if count%i==0:
            break
        i=i+1
    else:
        print(count)
        num=num-1
    count=count+1
