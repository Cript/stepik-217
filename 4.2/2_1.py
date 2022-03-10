def main():
    # k, l = 4, 14
    # dictionary = {'0': 'a', '10': 'b', '110': 'c', '111': 'd'}
    # sss = '01001100100111'

    decoded_string = ''
    dictionary = {}
    k, l = input().split()
    for line in range(int(k)):
        letter, code = input().split()
        dictionary[code] = letter[0]
    sss = input()

    code_length = 1
    while sss:
        substr = sss[0:code_length]
        if substr in dictionary:
            decoded_string += dictionary[substr]
            sss = sss[code_length:]
            code_length = 1
            continue
        code_length += 1

    print(decoded_string)

if __name__ == '__main__':
    main()
