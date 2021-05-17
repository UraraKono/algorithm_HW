import sys
M,L = map(int, input().split())
N = int(input())
for i in range(N):
    item, *values = input().split()
    price, level = map(int, values)
    if L >= level and M >= price:
        print (item, price)