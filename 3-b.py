import sys
class Heap:
    def __init__(self, size):
        self.inf = 10**9+1
        self.size = size+1
        self.array = [self.inf]*self.size
        self.last = 0
    def add(self, value: int):
        if self.last != self.size:
            self.last += 1
            self.array[self.last] = value
            self.check_after_add(self.last) #制約を満たしているかチェック
            #print(self.array[1],self.array[2],self.array[3],self.array[4],self.array[5],self.array[6])
    def remove(self):
        if self.last!=0:
            removed = self.array[1]
            self.array[1] = self.array[self.last]
            self.array[self.last] = self.inf
            self.last -= 1
            self.check_after_remove(1)
            print(removed)
            #print('removed value=',removed)
            #print(self.array[1],self.array[2],self.array[3],self.array[4],self.array[5],self.array[6])
    def check_after_add(self, i):
        if i<2: return
        if self.array[i] > self.array[i//2]: #親の方が子より小さくなってたらスワップ
            tmp = self.array[i]
            self.array[i] = self.array[i//2]
            self.array[i//2] = tmp
            #print('i=',i)
            self.check_after_add(i//2)
    def check_after_remove(self, i): #親の方が子より大きいようにしたい 親が子より小さかったらスワップ
        if self.array[2*i] == self.inf and self.array[2*i+1] == self.inf: 
            return
        elif self.array[2*i] == self.inf and self.array[2*i+1] != self.inf:
            a = 2*i+1
            if self.array[i] < self.array[a]:
                self.swap(a,i)
                self.check_after_remove(a)
        elif self.array[2*i] != self.inf and self.array[2*i+1] == self.inf:
            a = 2*i
            if self.array[i] < self.array[a]:
                self.swap(a,i)
                self.check_after_remove(a)
        elif self.array[i] < self.array[2*i] or self.array[i] < self.array[2*i+1]:
            if self.array[2*i] >= self.array[2*i+1]:
                a = 2*i
                self.swap(a,i)
                self.check_after_remove(a)
            elif self.array[2*i+1] > self.array[2*i] and self.array[2*i+1] != self.inf:
                a = 2*i+1
                self.swap(a,i)
                self.check_after_remove(a)
            else: return
        else: return
    def swap(self,a,b): #self.array[a],self.array[b]をswap returnは何も返さない
        tmp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = tmp
Q = int(input())
rbuf = Heap(10**5) #もしかしたらこれが原因で時間かかるかも？
for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        #print('x=',s[1])
        rbuf.add(s[1])
    elif s[0] == 2:
        rbuf.remove()
