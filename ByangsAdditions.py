A, B = input().split()
count=0
listA = listB = []
listA[:0] = A
listB[:0] = B
if len(listA)>len(listB):length=len(listA)
else:length=len(listB)
for i in range(0,length):
    x = int(listA[i])
    y=int(listB[i])
    if(x+y)>10:
        print("Yes")
        count=1
        break
if count==0:
    print("No")
