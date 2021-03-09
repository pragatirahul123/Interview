list=[1,2,3,4,5,6,7,8,9]
index=0
count=0
count1=0
while index<len(list):
    if list[index]%2==0:
        count=count+1
    else:
        count1=count1+1
    index=index+1
print("Even",count)
print("Odd",count1)
    
