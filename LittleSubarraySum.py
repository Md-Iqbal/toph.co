n,uperlimit,lowerlimit = map(int,input().split())
listxxx=list(map(int,input().split()))[:n]
result = 0
for i in range(uperlimit,lowerlimit+1):
    result+=listxxx[i]
print(result)