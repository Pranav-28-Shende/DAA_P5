def lcs(X, Y):
    m, n = len(X), len(Y)
    cost = [[0]*(n+1) for _ in range(m+1)]
    direction = [[""]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                cost[i][j] = cost[i-1][j-1] + 1
                direction[i][j] = "↖"
            else:
                if cost[i-1][j] >= cost[i][j-1]:
                    cost[i][j] = cost[i-1][j]
                    direction[i][j] = "↑"  
                else:
                    cost[i][j] = cost[i][j-1]
                    direction[i][j] = "←"  
    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if direction[i][j] == "↖":
            lcs_str.append(X[i-1])
            i -= 1
            j -= 1
        elif direction[i][j] == "↑":
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()
    return cost, direction, cost[m][n], "".join(lcs_str)


def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))


def longest_repeating_subsequence(S):
    m = len(S)
    cost = [[0]*(m+1) for _ in range(m+1)]
    direction = [[""]*(m+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, m+1):
            if S[i-1] == S[j-1] and i != j:
                cost[i][j] = cost[i-1][j-1] + 1
                direction[i][j] = "↖"
            else:
                if cost[i-1][j] >= cost[i][j-1]:
                    cost[i][j] = cost[i-1][j]
                    direction[i][j] = "↑"
                else:
                    cost[i][j] = cost[i][j-1]
                    direction[i][j] = "←"
    i, j = m, m
    lrs_str = []
    while i > 0 and j > 0:
        if direction[i][j] == "↖":
            lrs_str.append(S[i-1])
            i -= 1
            j -= 1
        elif direction[i][j] == "↑":
            i -= 1
        else:
            j -= 1
    lrs_str.reverse()
    return cost, direction, cost[m][m], "".join(lrs_str)
if __name__ == "__main__":
    X = "AGCCCTAAGGGCTACCTAGCTT"
    Y = "GACAGCCTACAAGCGTTAGCTTG"
    #Task1
    print("TASK 1: Longest Common Subsequence (LCS)")
    cost, direction, lcs_length, lcs_string = lcs(X, Y)
    print("\nCost matrix:")
    print_matrix(cost)
    print("\nDirection matrix:")
    print_matrix(direction)
    print(f"\nLength of LCS: {lcs_length}")
    print(f"LCS is: {lcs_string}")

    # TASK 2
    S = "AABCBDC"
    print("\nTASK 2: Longest Repeating Subsequence (LRS)")
    cost, direction, lrs_length, lrs_string = longest_repeating_subsequence(S)
    print("\nCost matrix:")
    print_matrix(cost)
    print("\nDirection matrix:")
    print_matrix(direction)
    print(f"\nLength of LRS: {lrs_length}")
    print(f"LRS is: {lrs_string}")
