import sys
# 一文字ずつ文字を収納しようとしてできていないやつ

class Robot:
    def __init__(self,init,N):
        self.array = ['']*(N+1)
        self.array[0] = init
        #self.leng = [0] * (N+1)
        #self.leng[0] = len(init)
        #print(self.array[0])
        #print(self.array[1])
    def add(self, i, j, c):
        #print('j',j,'array[j]',self.array[j])
        self.array[i] = c+self.array[j]
        #self.leng[i] = self.leng[j]+1
        #print('i',i,'array[i]',self.array[i])
    def remove(self, i, j):
        tmp = self.array[j]
        #print('self.leng[j]',self.leng[j])
        #self.leng[i] = self.leng[j] - 1
        self.array[i] = tmp[:len(self.array[j])-1]
        #print('tmp',tmp)
        #print('self.array[i]',self.array[i]) 
S = input()
N = int(input())
dsgn = Robot(S,N)
for i in range(N):
    s = input().split()
    t = int(s[0])
    j = int(s[1])
    if t == 1:
        c = s[2]
        #print('c=',c)
        dsgn.add(i+1,j,c)
    if t == 2:
        dsgn.remove(i+1,j)
Q = int(input())
for i in range(Q):
    s = int(input())
    #print('s=', s)
    print(dsgn.array[s])