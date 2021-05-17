import sys
max_sum = 0
max_index = 0
N, M = map(int, input().split())
a = list(map(int, input().split()))
sum_m =[]
# 最初のM個のsum
for i in range(M):
    max_sum += a[i]
sum_m.append(max_sum)
for j in range(1,N-M):
    sum_m.append(sum_m[j-1]-a[j-1]+a[j+M-1])
    if sum_m[j]>max_sum:
        max_sum = sum_m[j]
        max_index = j
print(max_sum, max_index+1)