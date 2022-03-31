
given_string = input()
word1 = input()
word = list(word1)


def matrix(string, n):
    lst1 = []
    for i in range(len(string)):

        if i % n == 0:
            sub = string[i:i + n]
            lst = []
            for j in sub:
                lst.append(j)

            lst1.append(lst)
    return lst1


mat = matrix(given_string, int(len(given_string) ** 0.5))
ROW = len(mat[0])
COL = len(mat)


def isvalid(row, col, prevRow, prevCol):

    return (row >= 0) and (row < ROW) and (col >= 0) and \
           (col < COL) and not (row == prevRow and col == prevCol)


rowNum = [-1, -1, -1, 0, 0, 1, 1, 1]
colNum = [-1, 0, 1, -1, 1, -1, 0, 1]


def DFS(mat, row, col, prevRow, prevCol, word, path, index, n):

    if index > n or mat[row][col] != word[index]:
        return
    path += "[" + str(row) + ", " + str(col) + "] " + "->"

    if index == n:
        print(path)
        return
    for k in range(8):
        if isvalid(row + rowNum[k], col + colNum[k], prevRow, prevCol):
            DFS(mat, row + rowNum[k], col + colNum[k], row, col, word, path, index + 1, n)


def findWords(mat, word, n):

    for i in range(ROW):
        for j in range(COL):
            if mat[i][j] == word[0]:
                DFS(mat, i, j, -1, -1, word, "", 0, n)


findWords(mat, word, len(word) - 1)
