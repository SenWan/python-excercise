def fibo(n):
    if n <= 1 :
        return n
    else:
        return (fibo(n - 1) + fibo(n - 2))


n_terms = 10
for i in range(n_terms):
    print(fibo(i))
