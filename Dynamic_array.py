from math import ceil
from typing import Optional, Callable, Any, Union


DeType = Union[int, str, None]
Default = Union['DynamicArray', None]


class DynamicArray(object):
    def __init__(self: 'DynamicArray',
                 capacity: int = 1,
                 grow_factor: float = 0.2):
        self.length = 0  # Actual number of elements in dynamic array
        self.capacity = capacity  # Initialize chunk of memory size to 1
        self.grow_factor = grow_factor  # grow_factor is set to 1.2
        self.chunk: list[DeType] = [None] * self.capacity  # initialized blocks

    def add_element(self: 'DynamicArray',
                    element: Optional[DeType]) -> None:
        if element is not None and type(element) != int:
            raise Exception('Input data error, please check it')
        if self.length == self.capacity:
            add_chunk_size = ceil(self.capacity * self.grow_factor)
            self.chunk += [None] * add_chunk_size
            self.capacity = self.capacity + add_chunk_size
        self.chunk[self.length] = element
        self.length += 1

    def __iter__(self: 'DynamicArray') \
            -> 'Iterator':
        return Iterator(self.chunk, self.length)

    def __eq__(self: 'DynamicArray',
               other) -> bool:  # Check A is equality to B
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

    def __init__(self: 'Iterator',
                 chunk: list[Optional[DeType]],
                 length: int) -> None:
        self.chunk = chunk
        self.length = length
        self.element_index = -1

    def __iter__(self: 'Iterator') \
            -> Optional['Iterator']:
        """ Implement iter(self). """
        return self

    def __next__(self: 'Iterator') -> Optional[DeType]:
        """ Implement next(self). """
        self.element_index += 1
        if self.element_index >= self.length:
            raise StopIteration()
        return self.chunk[self.element_index]


def copy(lst: DynamicArray) -> DynamicArray:
    """ Copy an LST

    :param lst: DynamicArray
    :return: DynamicArray
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


def cons(lst: Optional[DynamicArray],
         element: Optional[int] = None) -> DynamicArray:
    """ Add an element at the end of the array.

    :param lst: DynamicArray
    :param element: The given element
    :return: DynamicArray
    """
    assert type(lst) == DynamicArray
    res = copy(lst)
    res.add_element(element)
    return res


def remove(lst: DynamicArray,
           value: Optional[int]) -> DynamicArray:
    """ Remove an element of array at specified position.

    :param lst: DynamicArray
    :param value: int
    :return: DynamicArray
    """
    assert type(lst) == DynamicArray
    res = DynamicArray()
    for i in range(lst.length):
        if i != value:
            res.add_element(lst.chunk[i])
    return res


def length(lst: DynamicArray) -> int:
    """ Return the length of array.

    :param lst: DynamicArray
    :return: int
    """
    assert type(lst) == DynamicArray
    return lst.length


def member(lst: DynamicArray,
           v: int = None) -> bool:
    """ Determines whether the given value is a member of the array.

    :param lst: DynamicArray
    :param v: int
    :return: bool
    """
    assert type(lst) == DynamicArray
    if v not in lst.chunk[:lst.length]:
        return False
    else:
        return True


def reverse(lst: DynamicArray) -> DynamicArray:
    """ Reverse the array.

    :param lst: The given DynamicArray
    :return: DynamicArray
    """
    assert type(lst) == DynamicArray
    res = DynamicArray(len(lst.chunk))
    for i in range(lst.length):
        res.add_element(lst.chunk[lst.length - i - 1])
    return res


def to_list(lst: DynamicArray) -> list:
    """ Transform the array to a list.

    :param lst: DynamicArray
    :return: list
    """
    assert type(lst) == DynamicArray
    res: list[DeType] = []
    for i in range(lst.length):
        res.append(lst.chunk[i])
    return res


def from_list(lst: list) -> DynamicArray:
    """ Add elements from a list to the empty array

    :param lst: list
    :return: DynamicArray
    """
    assert type(lst) == list
    res = DynamicArray()
    for i in lst:
        res.add_element(i)
    return res


def find(lst: DynamicArray,
         function: Callable[[Optional[DeType]], Any]) -> bool:
    """ Search the elements that match the function

    :param lst: DynamicArray
    :param function: function
    :return: bool
    """
    assert callable(function)
    for i in lst.chunk:
        if function(i):
            return True
    return False


def filter(lst: DynamicArray,
           function: Callable[[Optional[DeType]], Any]) -> DynamicArray:
    """ Filter the array by specific function

    :param lst: DynamicArray
    :param function: Any
    :return: DynamicArray
    """
    assert callable(function)
    res = DynamicArray(len(lst.chunk))
    for i in range(lst.length):
        if function(lst.chunk[i]):
            res.add_element(lst.chunk[i])
    return res


def map(lst: DynamicArray,
        function: Callable[[Optional[DeType]], Any]) -> DynamicArray:
    """ Applied function to every item of instances of DynamicArray,
    yielding the results.

    :param lst: DynamicArray
    :param function: Any
    :return: DynamicArray
    """
    assert type(lst) == DynamicArray
    assert callable(function)
    res = DynamicArray(len(lst.chunk))
    for i in range(lst.length):
        res.add_element(function(lst.chunk[i]))
    return res


def reduce(lst: DynamicArray,
           function: Callable[[Any, Optional[DeType]], Any],
           initial_state: Optional[int] = None) -> DeType:
    """  Apply function of two arguments cumulatively to the items of the
         array, from left to right, to reduce the array to a single value.

    :param lst: DynamicArray
    :param function: Any
    :param initial_state: Any
    """
    assert type(lst) == DynamicArray
    assert callable(function)
    assert type(initial_state) == int
    state = initial_state
    for i in range(lst.length):
        if lst.chunk[i] is not None:
            state = function(state, lst.chunk[i])
    return state


def iterator(lst: DynamicArray) -> Iterator:
    """ An iterator object of DynamicArray.

    :param lst: The given DynamicArray
    """
    return iter(lst)


def empty() -> DynamicArray:
    """ An empty array"""
    return DynamicArray()


def concat(lst1: DynamicArray,
           lst2: DynamicArray) -> DynamicArray:
    """ Concatenate arrays 1 and 2

    :param lst1: DynamicArray
    :param lst2: DynamicArray
    :return: DynamicArray
    """
    assert type(lst1) == DynamicArray
    res = DynamicArray()
    for i in range(lst1.length):
        res.add_element(lst1.chunk[i])
    for j in range(lst2.length):
        res.add_element(lst2.chunk[j])
    return res


def eq(lst1: DynamicArray,
       lst2: DynamicArray) -> bool:
    """ Check whether two arrays are equal

    :return: bool
    """
    assert type(lst1) == DynamicArray
    assert type(lst2) == DynamicArray
    return lst1.__eq__(lst2)


def str1(lst: DynamicArray) -> str:
    """ Returns the string version of an array element
    :param lst:
    :return: str
    """
    assert type(lst) == DynamicArray
    res = str(lst.chunk[:lst.length])
    return res
