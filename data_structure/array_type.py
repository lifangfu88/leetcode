def array_type():
    arr_a = ['1', '2', '3']
    arr_b = ['1', '2', '3']
    # remove element from list end, right end
    arr_a.pop()
    # remove value
    arr_a.remove('1')
    # add element at right end
    arr_a.append('4')
    # insert at certain position (index, value)
    arr_a.insert(0, '0')
    # extend list in place
    arr_a.extend(arr_b)
    # count of certain value
    arr_a.count('1')
    # index of first appearance
    arr_a.index('0')
    # sort, optional reverse flag
    arr_a.sort()
    # reverse
    arr_a.reverse()
    # remove all elements
    arr_a.clear()


if __name__ == '__main__':
    array_type()
