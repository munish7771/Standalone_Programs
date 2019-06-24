n = int(input())
_matrix = []
_li = []
for i in range(n):    
    _list = list(map(lambda i:int(i),input().split()))
    _li += _list
    _matrix.append([-1]*n)
print(_matrix)
_li.sort()
if n % 2 == 0:
    _ex = n % 2
    _ey = n % 2 - 1
else:
    
_x = 0
_y = 0
_dir = l
while(True):
    if _x == 