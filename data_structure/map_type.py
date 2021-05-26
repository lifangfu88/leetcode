from collections import OrderedDict, defaultdict, deque


def map_test():
    """
    default dict doesn't expand the scope to create the real object outside of the map,
    it can be used to add typed value real handy

    :return:
    """
    map_a = {1: ['one'], 2: ['two']}

    map_b = defaultdict(lambda: [])
    map_b[0].append('zero')

    map_b.update(map_a)
    o = map_b.get(1)

    map_c = OrderedDict()

    map_c.update(map_b)

    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)

    # OrderedDict memorizes the order of map entry is put in
    od = OrderedDict()
    od[5] = 'five'
    od[3] = 'three'

    print(od.values())

    # deque double-end-queue, can be used as stack
    dq = deque([1, 2, 3, 4, 5])
    dq.append(6)
    assert 1 == dq.popleft()
    assert 6 == dq.pop()

def default_val():
    return 'zero'


if __name__ == '__main__':
    map_test()
