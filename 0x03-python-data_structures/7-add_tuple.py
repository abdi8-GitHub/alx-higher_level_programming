#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple(new_tuple)


if __name__ == '__main__':
    add_tuple(tuple_a=(), tuple_b=())
