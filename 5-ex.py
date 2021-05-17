import sys

def Kaibun(pattern):
    ans = 0
    base = 1007 # 基数 
    h = 10**9+7 #除数
    l = len(pattern)
    text = [None]*l

    #baseの0乗からl乗までを作っておく
    base_array = [1]
    for i in range(l):
        base_array.append(base_array[i]*base%h)
    #print('base_array',base_array)

    size = int(l*(l+1)/2)
    H_p = [0]*size
    #H_rl = [0]*size
    p_len = [0]*size #indexがkの時の部分文字列の長さ
    k_i = [0]*size #indexがkの時の部分文字列の先頭index i
    
    for i in range(l):
        text[i] = pattern[l-i-1]

    k=0
    for i in range(l):
        for j in range(i,l):
            #Sのindexがi~j番目までの部分文字列
            p_len[k] = j-i+1 #この部分文字列の文字数
            k_i[k] = i #この文字列のpatternで見た時の先頭の文字のindex
            for m in range(p_len[k]):
                H_p[k] = (H_p[k]*base + ord(pattern[i+m]))%h
            k += 1

    H_t = [0]*l
    for i in range(1,l+1):
        for j in range(0,i):
            #print('i',i,'j',j)
            H_t[i-1] = (H_t[i-1]*base + ord(text[j]))%h #textの先頭からindex i文字目までのロリは
    #print('H_t',H_t)

    for k in range(size):
        H_tt = H_t[p_len[k]-1]
        #print('H_tt', H_tt)
        for i in range(l-p_len[k]):
            if H_p[k] == H_tt:
                ans += 1
            if k_i[k]+p_len[k] < l:
                H_tt = (H_tt*base - base_array[p_len[k]]*ord(text[i]) + ord(text[i+p_len[k]]))%h

    print(ans)

S = list(input())
Kaibun(S)
