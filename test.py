def bleh(brick_arr):
    M = [[] for i in range(len(brick_arr))]
    for i in range(max(brick_arr)):
        for j in range(len(brick_arr)):
            if brick_arr[j] > i:
                M[j].append(1)
            else:
                M[j].append(0)
    R = len(M)
    C = len(M[0])

    S = []
    for i in range(R):
        temp = []
        for j in range(C):
            if i == 0 or j == 0:
                temp += M[i][j],
            else:
                temp += 0,
        S += temp,

    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
            else:
                S[i][j] = 0

    max_of_s = S[0][0]
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    return max_of_s


# Driver Program
if __name__ == "__main__":
    brick_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(bleh(brick_arr))
