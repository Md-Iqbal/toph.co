n = int(input())
numbers = list(map(int, input().strip().split()))[:n]
for i in range(n):
    print(format(sum(numbers[:i+1])/(i+1), '.5f'))