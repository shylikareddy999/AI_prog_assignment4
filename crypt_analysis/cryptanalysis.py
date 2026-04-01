from itertools import permutations

letters = ('T', 'W', 'O', 'F', 'U', 'R')
digits = range(10)

for perm in permutations(digits, len(letters)):
    T, W, O, F, U, R = perm

    if T == 0 or F == 0:
        continue

    TWO = 100*T + 10*W + O
    FOUR = 1000*F + 100*O + 10*U + R

    if 2 * TWO == FOUR:
        print("Solution Found:")
        print("T =", T, "W =", W, "O =", O)
        print("F =", F, "U =", U, "R =", R)
        print("TWO + TWO =", TWO + TWO)
        print("FOUR =", FOUR)
        break