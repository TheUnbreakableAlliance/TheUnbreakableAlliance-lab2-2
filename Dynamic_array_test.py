# Author: Fan Yuxin, Weng Wenchao
import unittest
from Dynamic_array import *
from hypothesis import given
import hypothesis.strategies as st


class TestDynamicArray(unittest.TestCase):
    # Add a new element
    def test_Add_a_new_element(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        l2 = cons(cons(empty1, None), 1)
        self.assertEqual(str(empty1), "[]")
        self.assertEqual(str(l1), "[1, None]")
        self.assertEqual(str(l2), "[None, 1]")
        self.assertNotEqual(empty1, l1)
        self.assertNotEqual(empty1, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(cons(1, empty1), None))

    # Remove an element by value
    def test_Remove_an_element(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        self.assertEqual(str(remove(l1, 0)), "[None]")
        self.assertEqual(str(remove(l1, 1)), "[1]")

    # Size
    def test_size(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        l2 = cons(cons(cons(empty1, None), 1), 2)
        self.assertEqual(length(empty1), 0)
        self.assertEqual(length(l1), 2)
        self.assertEqual(length(l2), 3)

    # Is member
    def test_is_member(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        self.assertFalse(member(empty1, None))
        self.assertTrue(member(l1, None))
        self.assertTrue(member(l1, 1))
        self.assertFalse(member(l1, 2))

    def test_reverse(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        l2 = cons(cons(empty1, None), 1)
        self.assertEqual(l1, reverse(l2))

    def test_to_list(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        self.assertEqual(to_list(l1), [1, None])

    def test_from_list(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        l2 = cons(cons(empty1, None), 1)
        self.assertEqual(l1, from_list([1, None]))
        self.assertEqual(concat(l1, l2), from_list([1, None, None, 1]))

    def test_find(self):
        l1 = from_list([1, 2, 3, 4])
        self.assertTrue(find(l1, lambda x: x % 2 == 0))
        self.assertFalse(find(l1, lambda x: x % 5 == 0))

    def test_filter(self):
        l1 = from_list([1, 2, 3, 4])
        self.assertEqual(filter(l1, lambda x: x % 2 == 0), from_list([2, 4]))
        self.assertEqual(to_list(filter(l1, lambda x: x % 2 == 0)), [2, 4])

    def test_map(self):
        l1 = from_list([1, 2, 3, 4])
        self.assertEqual(map(l1, lambda x: x % 2), from_list([1, 0, 1, 0]))

    def test_reduce(self):
        l1 = from_list([1, 2, 3, 4])
        self.assertEqual(reduce(l1, lambda x, y: x * y, 1), 24)

    def test_iter(self):
        x = [1, 2, 3, 4]
        lst = from_list(x)
        tmp = []
        try:
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst), tmp)

    def test_empty1(self):
        res = DynamicArray()
        self.assertEqual(to_list(res), [])

    def test_concat(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        l2 = cons(cons(empty1, None), 1)
        l3 = from_list([1, None, None, 1])
        self.assertEqual(concat(l1, l2), l3)

    def test_eq(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        l2 = cons(cons(empty1, 1), None)
        self.assertEqual(eq(l1, l2), True)

    def test_str(self):
        empty1 = DynamicArray()
        l1 = cons(cons(empty1, 1), None)
        self.assertEqual(str1(l1), "[1, None]")

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, lst):
        self.assertEqual(to_list(from_list(lst)), lst)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        lst = from_list(lst)
        res = DynamicArray()
        self.assertEqual(concat(res, lst), lst)
        self.assertEqual(concat(lst, res), lst)

    @given(a=st.lists(st.integers()),
           b=st.lists(st.integers()),
           c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        lst1 = from_list(a)
        lst2 = from_list(b)
        lst3 = from_list(c)
        self.assertEqual(concat(concat(lst1, lst2), lst3),
                         concat(lst1, concat(lst2, lst3)))
