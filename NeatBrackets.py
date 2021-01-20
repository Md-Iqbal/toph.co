s=input()
start_p = s.count('(')
end_p = s.count(')')
if (start_p == end_p) and (s[0] != ')' or s[-1] != '('):
    print("Yes")
else:
    print("No")