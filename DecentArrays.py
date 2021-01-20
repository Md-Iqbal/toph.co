n=int(input())
test=accending=[n]
accending=list(map(int, input().split()))
test=accending[:]
test.sort()
if test==accending:
    print("Yes")
else:
    print("No")