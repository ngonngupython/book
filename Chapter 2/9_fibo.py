def fibo_norecursive(n):
    if (n==0): return 0;
    if (n==1): return 1;

    f0 = 0
    f1 = 1
    fn = f0+f1
    for i in range(2, n+1):
        fn = f1 + f0
        f0 = f1
        f1 = fn

    return fn

print(fibo_norecursive(20))