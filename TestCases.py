status = "AC"
def take_input():
    return map(int, input().split())

n,cpul,meml=take_input()
for i in range(0,n):
    di,cpui,memi=take_input()
    if cpui > cpul:
        status = "CLE"
        break
    if memi > meml:
        status = "MLE"
        break
    if di > 0:
        status = "WA"
        break
print(status)
