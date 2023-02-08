def fib_digit(n):
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append((fib[i-2] + fib[i-1]) % 10)

    return fib[-1]


def main():
    # n = int(input())
    # print(fib_digit(n))
    print(fib_digit(841645))
    # print(fib_digit(15))


if __name__ == "__main__":
    main()