# def solve (A, R, L):
    # _return = ""
    # _sum = sum(A)
    # print(_sum)
    # _s = 0
    # _len = len(A)
    # for i in range(len(R)):
    #     l = L[i] 
    #     r = R[i]
    #     _s = 0
    #     while(l <= r):
    #         # print(str(l) + ":" +str(r)+":",end="") 
    #         if l % _len == 1 and l + _len <= r:
    #             _s += _sum
    #             l += _len
    #             # print("new L:"+str(l))
    #         else:
    #             _s += A[(l % _len) - 1]
    #             l += 1
    #         # print("sum =" +str(_s))
    #     _return += " " + str(_s)
    #     # print("$")
    # return _return
def solve (A, R, L):
    _len = len(A)
    for i in range(len(R)):
        _left = 0
        _right = 0
        _middle = 0
        l = L[i] 
        r = R[i]
        if l % _len == 1:
            _left = 0
            print(_left,end=":")
        else:
            _left = sum(A[:- (l%_len + 1)])    
            print(_left,end=":")
            l = l + l%_len + 1
            ## to change
        if r - l >= _len:
            _n = _len//(r - l)
            _middle = sum(A)*_n
            print(_middle,end=":")
            l += _n*_len
        _right = sum(A[:r - l])
        print(_right)
        print(_left+_right+_middle)
        print("done")
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    out_ = solve(A, R, L)
    # print (' '.join(map(str, out_)))
    print(out_)