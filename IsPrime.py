number=int(input())
check=0
if number > 1:
    for i in range(2, int((number/2))+2):
        if number % i == 0:
            print("No")
            check=1
            break
if check==0:
    print("Yes")