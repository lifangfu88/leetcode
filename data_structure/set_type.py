def set_type():
    set_a = {'1', '2', '3', '2'}
    set_b = {'0', '2', '4'}
    set_a.add('3')
    # randomly remove element
    set_a.pop()
    # union in-place
    set_a.update(set_b)
    # remove element, key error when absent
    set_a.remove('0')
    # remove element, silently do nothing when absent
    set_a.discard('100')
    # all elements that are in this set but not the others
    set_c = set_a.difference({'5', '4'}, {'1', '2'})
    # Remove all elements of another set from this set.
    set_a.difference_update(set_b)
    # all elements that are in exactly one of the sets.
    set_d = set_a.symmetric_difference(set_b)
    # Update a set with the symmetric difference of itself and another. multiple union operation
    set_a.symmetric_difference_update(set_b)

    # Return True if two sets have a null intersection. aka. there is no common element
    t = set_a.isdisjoint({10086})

    f = set_a.issubset({'1', '2', 3})
    t = set_a.issuperset({})
    assert t is True


if __name__ == '__main__':
    set_type()
