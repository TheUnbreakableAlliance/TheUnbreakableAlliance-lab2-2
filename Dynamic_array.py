from math import ceil


class DynamicArray(object):
    def __init__(self, capacity=1, grow_factor=0.2):
        self.length = 0  # Actual number of elements in dynamic array
        self.capacity = capacity  # Initialize chunk of memory size to 1
        self.grow_factor = grow_factor  # grow_factor is set to 1.2
        self.chunk = [None] * self.capacity  # Allocate initialized memory blocks

    def add_element(self, element):
        if element is not None and type(element) != int:
            return 'Input data must be int or None, please check it'
        if self.length == self.capacity:
            add_chunk_size = ceil(self.capacity * self.grow_factor)
            self.chunk += [None] * add_chunk_size
            self.capacity = self.capacity + add_chunk_size
        self.chunk[self.length] = element
        self.length += 1

    def __iter__(self):
        return Iterator(self.chunk, self.length)

    def __eq__(self, other):  # Check A is equality to B
        """for eq() implementation"""
        assert type(other) == DynamicArray
        if self.length != other.length:
            return False
        else:
            for i in range(self.length):
                if self.chunk[i] != other.chunk[i]:
                    return False
        return True

    def __str__(self):  # String serialization
        """for str() implementation"""
        return str(self.chunk[:self.length])


class Iterator(object):
    """ An iterator object of DynamicArray. """

    def __init__(self, chunk, length):
        self.chunk = chunk
        self.length = length
        self.element_index = -1

    def __iter__(self):
        """ Implement iter(self). """
        return self

    def __next__(self):
        """ Implement next(self). """
        self.element_index += 1
        if self.element_index >= self.length:
            raise StopIteration()
        return self.chunk[self.element_index]


def copy(lst):
    """ Copy an LST
    
    :param lst: The given DynamicArray
    """
    assert type(lst) is DynamicArray
    if lst.length == lst.capacity:
        res = DynamicArray(ceil(lst.capacity*(1+lst.grow_factor)))
        res.length = lst.length
    else:
        res = DynamicArray(lst.capacity)
        res.capacity = lst.capacity
        res.length = lst.length
    for i in range(lst.length):
        res.chunk[i] = lst.chunk[i]
    return res


def cons(lst, element=None):
    """ Add an element at the end of the array.

    :param lst: The given DynamicArray
    :param element: The given element
    """
    if type(lst) is int and type(element) == DynamicArray:
        res = cons(element, lst)
    else:
        assert type(lst) == DynamicArray
        res = copy(lst)
        res.add_element(element)
    return res


def remove(lst, value=None):
    """ Remove an element of array at specified position.

    :param lst: The given DynamicArray
    :param value: Index of the array.
    """
    assert type(lst) == DynamicArray
    if value < 0 or value >= lst.length:
        return 'The location accessed is not in the dynamic array'
    res = DynamicArray()
    for i in range(lst.length):
        if i != value:
            res.add_element(lst.chunk[i])
    return res


def length(lst):
    """ Return the length of array.

    :param lst: The given DynamicArray
    """
    assert type(lst) == DynamicArray
    return lst.length


def member(lst, v):
    """ Determines whether the given value is a member of the array.

    :param lst: The given DynamicArray
    :param v: The given value.
    :return: Value is member if return True, else not.
    """
    assert type(lst) == DynamicArray
    if v not in lst.chunk[:lst.length]:
        return False
    else:
        return True


def reverse(lst):
    """ Reverse the array.

    :param lst: The given DynamicArray
    """
    assert type(lst) == DynamicArray
    res = DynamicArray(len(lst.chunk))
    for i in range(lst.length):
        res.add_element(lst.chunk[lst.length - i - 1])
    return res


def to_list(lst):
    """ Transform the array to a list.

    :param lst: The given DynamicArray
    """
    assert type(lst) == DynamicArray
    res = []
    for i in range(lst.length):
        res.append(lst.chunk[i])
    return res


def from_list(lst):
    """ Add elements from a list to the empty array

    :param lst: The given list
    """
    assert type(lst) == list
    res = DynamicArray()
    for i in lst:
        res.add_element(i)
    return res


def find(lst, function):
    """ Search the array for elements that match the function

    :param lst: The given DynamicArray
    :param function: The given function
    :return: Ture or Flase
    """
    assert callable(function)
    for i in lst.chunk:
        if function(i):
            return True
    return False


def filter(lst, function):
    """ Filter the array by specific function

    :param lst: The given DynamicArray
    :param function: The given function
    :return: The transformed array
    """
    assert callable(function)
    res = DynamicArray(len(lst.chunk))
    for i in range(lst.length):
        if function(lst.chunk[i]):
            res.add_element(lst.chunk[i])
    return res


def map(lst, function):
    """ Applied function to every item of instances of DynamicArray,
    yielding the results.

    :param lst: The given DynamicArray
    :param function: The given function
    :return: The transformed array
    """
    assert type(lst) == DynamicArray
    assert callable(function)
    res = DynamicArray(len(lst.chunk))
    for i in range(lst.length):
        res.add_element(function(lst.chunk[i]))
    return res


def reduce(lst, function, initial_state):
    """  Apply function of two arguments cumulatively to the items of the
         array, from left to right, to reduce the array to a single value.

    :param lst: The given DynamicArray
    :param function: The given function
    :param initial_state: the optional initializer
    """
    assert type(lst) == DynamicArray
    assert callable(function)
    assert type(initial_state) == int
    state = initial_state
    for i in range(lst.length):
        if lst.chunk[i] is not None:
            state = function(state, lst.chunk[i])
    return state


def iterator(lst):
    """ An iterator object of DynamicArray.

    :param lst: The given DynamicArray
    """
    return iter(lst)


def empty():
    """ An empty array"""
    return DynamicArray


def concat(lst1, lst2):
    """ Concatenate arrays 1 and 2

    :param lst1: The given DynamicArray1
    :param lst2: The given DynamicArray2
    :return: Concatenated array
    """
    assert type(lst1) == DynamicArray
    res = DynamicArray()
    for i in range(lst1.length):
        res.add_element(lst1.chunk[i])
    for j in range(lst2.length):
        res.add_element(lst2.chunk[j])
    return res


def eq(lst1, lst2):
    """ Check whether two arrays are equal

    :return: Ture or Flase
    """
    assert type(lst1) == DynamicArray
    assert type(lst2) == DynamicArray
    return lst1.__eq__(lst2)


def str1(lst):
    """ Returns the string version of an array element"""
    assert type(lst) == DynamicArray
    res = str(lst.chunk[:lst.length])
    return res
