arr = [[1, 5, 9, 7, 2, 0, 3, 0, 0],
       [0, 6, 4, 0, 0, 3, 0, 2, 0],
       [0, 3, 0, 6, 0, 0, 8, 0, 9],
       [0, 0, 0, 0, 8, 0, 0, 9, 1],
       [0, 0, 0, 4, 0, 2, 0, 0, 0],
       [4, 9, 0, 0, 3, 0, 0, 0, 0],
       [3, 0, 5, 0, 0, 1, 0, 7, 0],
       [0, 1, 0, 3, 0, 0, 2, 5, 0],
       [0, 0, 7, 0, 5, 4, 1, 6, 3]]

originalValues = [[False for x in range(9)] for y in range(9)]


def solve():
    fillOriginalValues()

    # print(findNextEmptyBox(0,0))

    backtrackingHelper(0, 0)

    printArray(arr)


def findNextEmptyBox(row, col):
    for i in range(0, 9):
        for k in range(0, 9):
            if(arr[i][k] == 0):
                return (i, k)

    return (-1, -1)


def backtrackingHelper(row, col):

    nextCord = findNextEmptyBox(row, col)
    # print(nextCord)
    if(nextCord[0] == -1):
        print("out of 0s")
        return True

    row = nextCord[0]
    col = nextCord[1]

    for num in range(1, 10):
        arr[row][col] = num

        if(isValid(row, col)):
            if(backtrackingHelper(row, col)):
                # print('backtracking return true')
                return True

        arr[row][col] = 0

    # print("return false")
    return False


def findSubgrid(row, col):
    # Assuming row and col start at 0 and go to 8
    # 1|2|3
    # 4|5|6
    # 7|8|9
    # ^ pattern for subgrids

    ref = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rRes, cRes = 0, 0
    if(row < 3):
        rRes = 0
    elif(row < 6):
        rRes = 1
    elif(row < 9):
        rRes = 2

    if(col < 3):
        cRes = 0
    elif(col < 6):
        cRes = 1
    elif(col < 9):
        cRes = 2

    return ref[rRes][cRes]


def isValid(row, col):
    # Check row, col and subgrid
    subgrid = findSubgrid(row, col)

    usedNums = []

    # Validate row
    for i in range(9):
        if(arr[row][i] != 0 and arr[row][i] in usedNums):
            return False
        else:
            usedNums.append(arr[row][i])

    usedNums.clear()

    # Validate col
    for i in range(9):
        if(arr[i][col] != 0 and arr[i][col] in usedNums):
            return False
        else:
            usedNums.append(arr[i][col])

    # Validate subgrid
    return validateSubgrid(subgrid)


def getSubgrid(subgrid):
    grid = [[0 for x in range(3)] for y in range(3)]

    if(subgrid == 1):
        for i in range(0, 3):
            for k in range(0, 3):
                grid[i][k] = arr[i][k]
    elif(subgrid == 2):
        for i in range(0, 3):
            for k in range(0, 3):
                grid[i][k] = arr[i][k+3]
    elif(subgrid == 3):
        for i in range(0, 3):
            for k in range(0, 3):
                grid[i][k] = arr[i][k+6]
    elif(subgrid == 4):
        for i in range(0, 3):
            for k in range(0, 3):
                grid[i][k] = arr[i+3][k]
    elif(subgrid == 5):
        for i in range(0, 3):
            for k in range(0, 3):
                grid[i][k] = arr[i+3][k+3]
    elif(subgrid == 6):
        for i in range(0, 3):
            for k in range(0, 3):
                grid[i][k] = arr[i+3][k+6]
    elif(subgrid == 7):
        for i in range(0, 3):
            for k in range(0, 3):
                grid[i][k] = arr[i+6][k]
    elif(subgrid == 8):
        for i in range(0, 3):
            for k in range(0, 3):
                grid[i][k] = arr[i+6][k+3]
    elif(subgrid == 9):
        for i in range(0, 3):
            for k in range(0, 3):
                grid[i][k] = arr[i+6][k+6]

    return grid


def validateSubgrid(subgrid):
    grid = getSubgrid(subgrid)

    usedNums = []
    for i in range(3):
        for k in range(3):
            if(grid[i][k] != 0 and grid[i][k] in usedNums):
                return False
            else:
                usedNums.append(grid[i][k])
    return True


def fillOriginalValues():
    global originalValues

    for i in range(0, 9):
        for k in range(0, 9):
            if(arr[i][k] != 0):
                originalValues[i][k] = True
            else:
                originalValues[i][k] = False


def printArray(arr):
    for i in range(0, 9):
        for k in range(0, 9):
            print(str(arr[i][k]) + " ", end="")
        print()


if __name__ == "__main__":
    solve()
