def gcd(a, b):
    gcd = 1
    for i in range(2, min(a, b)):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


def main():
    # a, b = map(int, input().split())
    # print(gcd(a, b))
    print(gcd(3918848, 1653264))


if __name__ == "__main__":
    main()