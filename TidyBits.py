A=int(input())
bit=str(bin(A))#convert A to binary and store as string
x=bit[2:]#remove first 2 index
replaced=x.replace("0","")#replace 0 with none
print(int(replaced,2))#convert into integer and 2 is the base of binary
