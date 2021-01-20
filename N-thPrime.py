def prime_function(n):
    prime = [2, 3]
    prime_check = True
    if n==1:
        return prime[0]
    elif n == 2:
        return prime[1]
    elif n>2:
        while(1):
            i = 4
            for check in range(2,(i//2)+1):
               if(i%check==0):
                   prime_check=False
                   break
            if prime_check==True:
                prime.append(i)
            if n==len(prime):
                break
            i+=1
        return prime[n-1]
print(prime_function(int(input())))
