H, M = map(int, input().split())
angle = float((30*H)-(5.5*M))
if angle >=180:
    angle = float(360-angle)
print("{:.5f}".format(angle))