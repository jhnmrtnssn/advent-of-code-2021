# Advent of Code - Day 5
# Part 2
import numpy as np


def parseInput():
    x1 = list([])
    y1 = list([])
    x2 = list([])
    y2 = list([])

    for line in open("input.txt"):
        line = line.strip().split()
        p1 = line[0].split(",")
        p2 = line[2].split(",")
        x1.append(int(p1[0]))
        y1.append(int(p1[1]))
        x2.append(int(p2[0]))
        y2.append(int(p2[1]))

    return x1, y1, x2, y2


def markHorizontal(line_map, x, y1, y2):
    if y1 < y2:
        start_y = y1
        stop_y = y2
    else:
        start_y = y2
        stop_y = y1
    for y in range(start_y, stop_y+1):
        line_map[x, y] += 1


def markVertical(line_map, y, x1, x2):
    if x1 < x2:
        start_x = x1
        stop_x = x2
    else:
        start_x = x2
        stop_x = x1
    for x in range(start_x, stop_x+1):
        line_map[x, y] += 1


def markDiagonal(line_map, x1, x2, y1, y2):
    if x1 < x2:
        if y1 < y2:
            for i in range(abs(x1-x2)+1):
                line_map[x1 + i, y1 + i] += 1
        else:
            for i in range(abs(x1-x2)+1):
                line_map[x1 + i, y1 - i] += 1
    else:
        if y1 < y2:
            for i in range(abs(x1-x2)+1):
                line_map[x1 - i, y1 + i] += 1
        else:
            for i in range(abs(x1-x2)+1):
                line_map[x1 - i, y1 - i] += 1


def markMap(line_map, x1, y1, x2, y2):
    if x1 == x2:
        markHorizontal(line_map, x1, y1, y2)
    elif y1 == y2:
        markVertical(line_map, y1, x1, x2)
    else:
        markDiagonal(line_map, x1, x2, y1, y2)

    return line_map


#######  PART 2  #######

x1, y1, x2, y2 = parseInput()
line_map = np.zeros([1000, 1000])
for i, _ in enumerate(x1):
    line_map = markMap(line_map, x1[i], y1[i], x2[i], y2[i])

n_intersections = 0
for row in line_map:
    for elem in row:
        if elem > 1:
            n_intersections += 1

# 18418 too low
# 18841 too high
print(n_intersections)
