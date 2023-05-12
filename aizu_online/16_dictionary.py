class Dictionary(object):
    def __init__(self, size):
        self.size = size
        self.a = [None] * size

    def hash(self, x):
        key = hash(x) % self.size
        while self.a[key] and self.a[key] != x:
            key = (key + 10 ** 9 + 7) % self.size
        return key

    def insert(self, x):
        self.a[self.hash(x)] = x

    def find(self, x):
        if self.a[self.hash(x)]:
            print('yes')
        else:
            print('no')


n = int(input())
dic = Dictionary(n)
for i in range(n):
    command, str = input().split()
    if command == 'insert':
        dic.insert(str)
    else:
        dic.find(str)