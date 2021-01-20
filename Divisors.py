x = int(input())
for i in range(1, int(x/2)+1):
    if(x%i==0):
        print (i,)
print (x)