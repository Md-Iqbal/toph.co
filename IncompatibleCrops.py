
#Has not soved yet

R, C = map(int, input().split())
counter = 0
crops = selection = []
for i in range(0, C):
    element = input()
    crops.append(element)
    selection.append(1)
for i in range(0, C):
    for j in range(0, R):
        if(crops[i][j] == '*'):
            crops.append(0)
            crops[i][j-1].append(0)
            crops[i][j+1].append(0)
            crops[i-1][j].append(0)
            crops[i+1][j].append(0)
for i in range(0, C):
    for j in range(0, R):
        if(crops[i][j] == '1'):
            counter=+1
print(counter)
