#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid1 = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid1))  # Expected output: 12

    grid2 = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    print(island_perimeter(grid2))  # Expected output: 10

    grid3 = [
        [1, 1],
        [1, 1]
    ]
    print(island_perimeter(grid3))  # Expected output: 8

    grid4 = [
        [1, 0],
        [0, 1]
    ]
    print(island_perimeter(grid4))  # Expected output: 8

    grid5 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(island_perimeter(grid5))  # Expected output: 0

    grid6 = [
        [1]
    ]
    print(island_perimeter(grid6))  # Expected output: 4