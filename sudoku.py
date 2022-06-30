#sudoku project implementation tues Jun 28, 2022
import pygame
from random import sample, shuffle

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
testboard = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def solution(b):
    lst = list(range(1,10))
    for i in range(81):
        x = i//9
        y = i%9
        if b[x][y] == 0:
            shuffle(lst)
            for num in lst:
                if is_valid(b, num, (x,y)):
                    b[x][y] = num
                    if not check_empty(b):
                        return True
                    else:
                        if solution(b):
                            return True
            break
    b[x][y] = 0
    return False

def board_create(b):
    nonempty = get_nonempty(b)
    filledcount = len(nonempty)
    rounds = 3
    while rounds > 3 and filledcount >= 17:
        x,y = nonempty.pop()
        filledcount -= 1
        removed = b[x][y]
        b[x][y] = 0
        copy = b.copy()
        counter = 0
        solve(copy)
        if counter != 1:
            b[x][y] = removed
            filledcount+= 1
            rounds -= 1
    return


def printBoard(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

def get_nonempty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] != 0:
                emptyarr = [(i,j)]
                return emptyarr

def check_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j)
    return None

def is_valid(b, num, pos):
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    x = pos[1] // 3
    y = pos[0] // 3

    for i in range(y*3, y*3 + 3):
        for j in range(x * 3, x*3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(b):
    find = check_empty(b)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1,10):
        if is_valid(b, i, (row, column)):
            b[row][column] = i

            if solve(b):
                return True

            b[row][column] = 0

    return False

solution(board)
printBoard(board)
print("---------------------")
board_create(board)
printBoard(board)