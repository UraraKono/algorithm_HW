import sys

Q = int(input())

def prime(n):
    if n<=1: False
    if n==2 or n==3: return True
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True

def prime_all(left,n):
    is_prime = [True]*(n-left+1)
    if left ==1:
        is_prime[0] = False
    i=2
    while i*i <= n:
        if prime(i) == True:
            j=2
            while i*j<=n:
                if i*j>=left:
                    is_prime[i*j-left] = False
                j+=1
        i+=1  
    return [i+left for i in range(n-left+1) if is_prime[i]]

for i in range(Q):
    ans = 0
    l,r = map(int, input().split())
    prime_all_r=prime_all(l,r)
    print(prime_all_r)
    for i in range(len(prime_all_r)):
        if prime_all_r[i]>=l and prime_all_r[i]>=3:
            if prime((prime_all_r[i]+1)/2) == True:
                ans +=1
                print(prime_all_r[i])
    print(ans)