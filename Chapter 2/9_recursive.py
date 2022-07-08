import sys
sys.setrecursionlimit(3000)

n = 2000
fn = [-1] * (n+1)
fn[0] = 0
fn[1] = 1

def fibo(n):
    if (fn[n] != -1): return fn[n];
    fn[n] = fibo(n-1)+fibo(n-2)
    return fn[n]