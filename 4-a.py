import sys
class Hash:
    def __init__(self, md):
        self.array = [None]*md
        self.mod = md
    def add(self, val):
        if self.array[val%self.mod] == None:
            self.array[val%self.mod] = val
        elif self.array[val%self.mod] != val:
            i=1
            while self.array[(val%self.mod+i)%self.mod] != None:
                i+=1
                if i==self.mod:
                    print('full')
                    break
            else:
                self.array[(val%self.mod+i)%self.mod] = val
    def search(self, val):
        if self.array[val%self.mod] == None:
            print('not found')
        elif self.array[val%self.mod] == val:
            print('found')
        elif self.array[val%self.mod] != val:
            i=1
            while self.array[(val%self.mod+i)%self.mod] != val:
                i+=1
                if i==self.mod:
                    print('not found')
                    break
            else: print('found')      
Q = int(input())
if Q<100:
    hsh = Hash(Q//2+1)
else:
    hsh = Hash(Q//3)
for i in range(Q):
    typ, x = map(int, input().split())
    if typ == 0:
        hsh.add(x)
    else: hsh.search(x)