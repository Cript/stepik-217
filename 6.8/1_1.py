# number_of_numbers = 5
# A = [2, 3, 9, 2, 9]

number_of_numbers = int(input())
A = [int(i) for i in input().split()]
max_number = 11

B = [0] * max_number
AA = [0] * number_of_numbers

for number in A:
    B[number] += 1

for i in range(1, max_number):
    B[i] = B[i] + B[i - 1]

for j in range(number_of_numbers - 1, -1, -1):
    AA[B[A[j]] - 1] = str(A[j])
    B[A[j]] -= 1

print(' '.join(AA))


