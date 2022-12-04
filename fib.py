def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
c=int(input())
for i in range(0,c+2):
    print(fib(i),end=" ")