from math import ceil


class DynamicArray(object):
    def __init__(self, capacity=1, grow_factor=0.2):
        self.length = 0    # Actual number of elements in dynamic array
        self.capacity = capacity  # Initialize chunk of memory size to 1
        self.grow_factor = grow_factor   # grow_factor is set to 1.2
        self.chunk = [None] * self.capacity  # Allocate initialized blocks

    def add_element(self, element):
        if element is not None and type(element) != int:
            return 'Input data must be int or None, please check it'
        if self.length == self.capacity:
            add_chunk_size = ceil(self.capacity * self.grow_factor)
            self.chunk += [None] * add_chunk_size
            self.capacity = self.capacity + add_chunk_size
        self.chunk[self.length] = element
        self.length += 1

    def __eq__(self, other):    # Check A is equality to B
        assert type(other) == DynamicArray
        if self.length != other.length:
            return False
        else:
            for i in range(self.length):
                if self.chunk[i] != other.chunk[i]:
                    return False
        return True

    def __str__(self):     # String serialization
        return str(self.chunk[:self.length])


def cons(lst, element=None):
    if type(lst) is int and type(element) == DynamicArray:
        res = cons(element, lst)
    else:
        assert type(lst) == DynamicArray
        res = DynamicArray()
        for i in range(lst.length):
            res.add_element(lst.chunk[i])
        res.add_element(element)
    return res


def remove(lst, value=None):
    assert type(lst) == DynamicArray
    if value < 0 or value >= lst.length:
        return 'The location accessed is not in the dynamic array'
    res = DynamicArray()
    for i in range(lst.length):
        if i != value:
            res.add_element(lst.chunk[i])
    return res


def length(lst):
    assert type(lst) == DynamicArray
    return lst.length


def member(lst, v):
    assert type(lst) == DynamicArray
    if v not in lst.chunk[:lst.length]:
        return False
    else:
        return True


def reverse(lst):
    assert type(lst) == DynamicArray
    res = DynamicArray()
    for i in range(lst.length):
        res.add_element(lst.chunk[lst.length-i-1])
    return res


def to_list(lst):
    assert type(lst) == DynamicArray
    res = []
    for i in range(lst.length):
        res.append(lst.chunk[i])
    return res


def from_list(lst):
    assert type(lst) == list
    res = DynamicArray()
    for i in lst:
        res.add_element(i)
    return res


def find(lst, function):
    assert callable(function)
    for i in lst.chunk:
        if function(i):
            return True
    return False


def filter(lst, function):
    assert callable(function)
    res = DynamicArray()
    for i in range(lst.length):
        if function(lst.chunk[i]):
            res.add_element(lst.chunk[i])
    return res


def map(lst, function):
    assert type(lst) == DynamicArray
    assert callable(function)
    res = DynamicArray()
    for i in range(lst.length):
        res.add_element(function(lst.chunk[i]))
    return res


def reduce(lst, function, initial_state):
    assert type(lst) == DynamicArray
    assert callable(function)
    assert type(initial_state) == int
    state = initial_state
    for i in range(lst.length):
        if lst.chunk[i] is not None:
            state = function(state, lst.chunk[i])
    return state


def iterator(lst):
    length = lst.length
    res = lst
    index = 0

    def foo():
        nonlocal res
        nonlocal length
        nonlocal index
        if (index >= length) | (res is None):
            raise StopIteration
        tmp = res.chunk[index]
        index = index+1
        return tmp
    return foo


def empty():
    return DynamicArray


def concat(lst1, lst2):
    assert type(lst1) == DynamicArray
    res = DynamicArray()
    for i in range(lst1.length):
        res.add_element(lst1.chunk[i])
    for j in range(lst2.length):
        res.add_element(lst2.chunk[j])
    return res


def eq(lst1, lst2):
    assert type(lst1) == DynamicArray
    assert type(lst2) == DynamicArray
    return lst1.__eq__(lst2)


def str1(lst):
    assert type(lst) == DynamicArray
    res = str(lst.chunk[:lst.length])
    return res
