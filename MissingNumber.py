sum = int(input())
a,b,c = map(int, input().split())
missing = sum - (a+b+c)
print(missing)