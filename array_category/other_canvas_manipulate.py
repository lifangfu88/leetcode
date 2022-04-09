

def rec(start, length, width):
    res = [[0] * width for _ in range(length)]
    return res


def mod(start, length, width, canvas, x):
    for i in range(start[0], start[0] + width):
        for j in range(start[1], start[1] + length):
            canvas[i][j] = x
    return canvas

def mov():
    """
    move rec, and recover any previously overriden rec
    redraw the canvas with new rec starting points
    """


if __name__ == '__main__':
    org = rec((0, 0), 10, 10)
    a = mod((0, 0), 3, 4, org, 1)
    for r in a:
        print(r)
    print('===========================')
    b = mod((2, 2), 3, 3, a, 2)
    for r in b:
        print(r)
