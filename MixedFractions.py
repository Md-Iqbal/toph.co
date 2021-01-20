N, D = map(int, input().split())
result = int(N/D)
numerator = N%D
print(result, numerator, D)