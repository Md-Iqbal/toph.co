n = int(input())
numbers = list(map(int, input().split()))[:n]
Sum = avg = 0
for i in range(0,n):
    Sum += numbers[i]
    print(float(Sum)/float(i+1))