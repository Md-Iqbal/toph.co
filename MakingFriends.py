x = int(input())
count=0
for i in range(1, int(x/2)+1):
    if(x % i == 0):
        count+=1
print(count)
