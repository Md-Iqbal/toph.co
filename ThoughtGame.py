n=int(input())
for i in range(0,n):
    a,b=map(int, input().split())
    avg = int((a+b)/2)
    if avg%2==0:
        print("Sadia will be happy.")
    else:
        print("Oops!")
