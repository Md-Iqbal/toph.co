n = int(input())
while (n!=0):
    over_count=ball_count=0
    string = input()
    Ball = []
    Ball[:0]=string
    length = len(Ball)
    for i in range(0,length):
        if (Ball[i] != 'D' and Ball[i] != 'W' and Ball[i] != 'N'):
            ball_count += 1
    over_count = int(ball_count/6)
    ball_count = int(ball_count % 6)
    if over_count == 0 and ball_count > 1:
        print(ball_count, "BALLS")
    elif over_count == 0 and ball_count == 1:
        print(ball_count, "BALL")


    if over_count == 1 and ball_count == 1:
        print(over_count, "OVER", ball_count, "BALL")

    if over_count == 1 and ball_count > 1:
        print(over_count, "OVER", ball_count, "BALLS")

    if over_count > 1 and ball_count == 1:
        print(over_count, "OVERS", ball_count, "BALL")

    if over_count > 1 and ball_count > 1:
        print(over_count, "OVERS", ball_count, "BALLS")


    elif over_count == 1 and ball_count == 0:
        print(over_count, "OVER")
    elif over_count > 1 and ball_count == 0:
        print(over_count, "OVERS")
    n-=1
