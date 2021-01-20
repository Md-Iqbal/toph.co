A = input()
listA=newlistA=[]
listA = list(A)
newlistA.append(listA[0].upper())
for i in range(1, len(listA)):
    if listA[i]=='s':
        newlistA.append('$')
    elif listA[i] == 'i':
        newlistA.append('!')
    elif listA[i] == 'o':
        newlistA.append('()')
    else:
        newlistA.append(listA[i])
newlistA.append('.')
A=''.join(map(str, newlistA))
print(A)