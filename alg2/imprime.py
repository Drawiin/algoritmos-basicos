def imprime(n):
    if n == 1:
        print(n)
    else:
        imprime(n - 1)
        print(n)

if __name__ == "__main__":
    imprime(int(input()))