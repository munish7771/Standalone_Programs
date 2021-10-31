# Input -> List of lists 
# Output -> find the number of pairs of lists such that both of them dont have 0 in common index

from math import factorial

def compare(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] == 0 and arr2[i] == 0: return 0
    return 1
def is_all_zero(l, Arr):
    # print(l)
    # print(Arr)
    return l*"0" == ''.join(str(i) for i in Arr)

def solve (N, M, Arr):
    zero_arr = []
    ones = 0
    # code here
    for i in range(len(Arr)):
        if 0 not in Arr[i]:
            ones += 1
        else:
            zero_arr += [Arr[i]]
    zero_len = len(zero_arr)
    total = ones * zero_len
    for i in range(zero_len):
        if is_all_zero(M, zero_arr[i]) :continue
        for j in range(i + 1, zero_len):
            if is_all_zero(M, zero_arr[j]): continue
            total += compare(zero_arr[i], zero_arr[j])
    total += int(factorial(ones)/(2 * factorial(ones - 2)))
    return total

T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    Arr = [list(map(int, input().split())) for i in range(N)]

    out_ = solve(N, M, Arr)
    print (out_)