n, m = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
print(' '.join(map(str, sorted(setA | setB))))