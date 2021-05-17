import sys

def KMP(text, pattern):
    t_len = len(text)
    p_len = len(pattern)
    #print('t_len',t_len,'p_len',p_len)
    #カーソル位置を保持する関数
    t_i = 0
    p_i = 0
    #skip tableを作成
    table = CreateTable(pattern)

    while t_i < t_len and p_i < p_len:
        #一致している場合は両方のカーソルを進める
        if text[t_i] == pattern[p_i]:
            #print('match t_i',t_i,'p_i',p_i)
            t_i += 1
            p_i += 1
        elif p_i == 0:
            #print('not same at the first pattern t_i',t_i,'p_i',p_i)
            t_i += 1
        else:
            #print('look up table t_i',t_i,'p_i',p_i)
            p_i = table[p_i]
    return (-1, t_i - p_i)[p_i == p_len]

def CreateTable(pattern):
    table = [0]*(len(pattern)+1)
    table[0] = -1
    i,j = 0,1

    while j < len(pattern):
        match = pattern[i] == pattern[j]
        if not match and i>0:
            i = table[i]
        else:
            if match:
                i += 1
            j += 1
            table[j] = i

    return table


S = list(input())
T = list(input())
#print(S)
#print(T)
print(KMP(S,T))

