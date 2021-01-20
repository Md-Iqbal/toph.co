p=int(float(input()))
result=int(p//10)
rest=10-result
plus='+'*result
dot='.'*rest
print("[{}{}] {}%".format(plus, dot, p))