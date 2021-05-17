import sys
def RollingHashMatch(text, pattern):
    base = 1007 # 基数 
    h = 10**9+7 #除数
    t_len = len(text)
    p_len = len(pattern)
    t_hash = p_hash = 0
    base_l = 1
    for i in range(p_len):
        base_l *= base
        base_l = base_l%h
    #print('base_l',base_l)
    #patternとtextの最初のp_len文字に関するハッシュ値を計算
    H_p = H_t = 0
    for i in range(p_len):
        #print('pattern[i]',i,ord(pattern[i]))
        #print('text[i]',i,ord(text[i]))
        H_p = (H_p*base + ord(pattern[i]))%h
        H_t = (H_t*base + ord(text[i]))%h
        #print('H_p',H_p,'H_t',H_t)
    for i in range(t_len - p_len+1):
        #print('2nd i',i)
        if H_p == H_t:
            #print('H_p',H_p,'H_t',H_t)
            print(i)
        if i+p_len < t_len:
            H_t = (H_t*base - base_l*ord(text[i]) + ord(text[i+p_len]))%h
            #print('text[i]',text[i],'text[i+p_len]',text[i+p_len])
            #print('2nd elif H_p',H_p,'H_t',H_t)
S = list(input())
T = list(input())
#print(S)
#print(T)
RollingHashMatch(S,T)
