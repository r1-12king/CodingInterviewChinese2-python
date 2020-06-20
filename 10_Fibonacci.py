def fibonacci(n):
    f1 = 0
    f2 = 1
    if n==0:
        return f1
    if n==1:
        return f2

    fn = 0

    for i in range(2,n+1):
        fn = f1+f2
        f1 = f2
        f2 = fn

    return fn

if __name__ == '__main__':
    res = fibonacci(7)
    print(res)