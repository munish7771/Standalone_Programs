t = int(input())
for i in range(t):
    n,k = input().split()
    n = int(n)
    k = int(k)
    if n % k == 0:
        print("Dishant")
    else:
        print("Arpa")