# n = int(input())
# _start = [int(i) for i in input().split()]
# _end = [int(i) for i in input().split()]
n = 5
_start = [2,4,1,0,3]
_end = [3,5,4,5,4]
_out = [0 for i in range(n)]
_cmp = [] + _start
stack = []

def remove(time):
    pass
# _start, _end = zip(*sorted(zip(_start, _end)))
# print(_start)
# print(_end)
# print(_out)
time = 0
while(time<n):
    if time == 0:
        _out[_start.index(time)] = 0
    else:
        # for all time > 0
        out = [stack.remove(i + 1) for i,val in enumerate(_end) if val==time]
        map(lambda i :print(i),_end)
        # for i in out:
        #     stack.remove(i)
        _out[_start.index(time)] = stack[-1]
        print(_out)
    stack.append(_start.index(time) + 1)
    time += 1

print(_out)
