def factorial(n):
    # CONDIZIONE TERMINALE
    if n == 0 or n == 1:
        return 1
    # CONDIZIONE NON TERMINALE
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    N = 5
    print(factorial(N))
