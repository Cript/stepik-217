def gcd(a, b):
    if b == 0:
        return a

    if a == 0:
        return b

    if a >= b:
        return gcd(a % b, b)

    if b >= a:
        return gcd(a, b % a)


def main():
    # a, b = map(int, input().split())
    # print(gcd(a, b))
    print(gcd(14159572, 63967072))


if __name__ == "__main__":
    main()