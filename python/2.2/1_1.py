def fib(n):
    fib_array = [0, 1]
    if n < 2:
        return fib_array[n]

    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])

    return fib_array[n]


def main():
    # n = int(input())
    # print(fib(n))
    # fib_array[2] = fib_array[0] + fib_array[1]
    # print(fib_array[2])
    print(fib(3))


if __name__ == "__main__":
    main()