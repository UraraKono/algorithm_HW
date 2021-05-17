import sys
N,K = map(int, input().split())
m = 10**9+7
def combination_mod(n,k):
    m = 10**9+7
    n_fact = 1
    for i in range(n):
        n_fact = n_fact*(i+1)
        n_fact = n_fact%m
        if i+1==k:
            k_fact = n_fact
        if i+1==n-k:
            n_k_fact = n_fact
    return n_fact,k_fact,n_k_fact
def pow_mod(n,a):
    m = 10**9+7
    if a==0: return 1
    tmp = pow_mod(n*n%m,a//2)
    if a%2==1: tmp = tmp*n%m
    return tmp
NCK = combination_mod(N,K)
NCK_mod = NCK[0]*pow_mod(NCK[1],m-2)*pow_mod(NCK[2],m-2)%m
print(NCK_mod)