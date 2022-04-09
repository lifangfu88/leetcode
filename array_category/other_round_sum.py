
# def roundx(x):







if __name__ == '__main__':
    # round sum 22, sum 21.5
    a = [2.5, 3.6, 7.8, 5.5, 2.1]
    # sum 19
    b = [2, 3, 7, 5, 2]
    d = [0.5, 0.6, 0.8, 0.5, 0.1]
    y = [3, 4, 8, 5, 2]

    # print((sum(a)))
    # print(sum(b))
    # for i in range(len(a)):
    #     d.append(a[i] - b[i])
    # print(sum(y))
    import bisect
    x = [2,3,5,6,8,10]
    print(bisect.bisect_left(x, 3))