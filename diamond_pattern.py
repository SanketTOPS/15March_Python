def fib(f, N):
    f[1] = 0
    f[2] = 1
    for i in range(3, N):
        f[i] = f[i - 1] + f[i - 2]

def fiboTriangle(n):
    N = n * (n + 1)     # Changed this equation
    f = [0]*(N + 1)
    fib(f, N)
    fiboNum = 1
    for i in range(n):
        for j in range(n-i):
            print(end=" ")
        for j in range(i):
            print(f[fiboNum], end=" ")
            fiboNum+=1
        print()
    for i in range(n,0,-1):
        for j in range(n-i):
            print(end=" ")
        for j in range(i):
            print(f[fiboNum], end=" ")
            fiboNum+=1
        print()        


n=3
fiboTriangle(n)