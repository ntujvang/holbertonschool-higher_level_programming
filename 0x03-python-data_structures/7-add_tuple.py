#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = list(tuple_a)
    tup_b = list(tuple_b)
    if len(tup_a) < 2:
        for i in range(len(tup_a), 2):
            tup_a.append(0)
    if len(tup_b) < 2:
        for i in range(len(tup_b), 2):
            tup_b.appent(0)
    new_tup = tuple([tup_a[0] + tup_b[0], tup_a[1] + tup_b[1]])
    return new_tup
