import unittest

from src.linked_list import LinkedList


class Test(unittest.TestCase):
    def test_linked_list_beg(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({2: 2})
        linked_list.insert_beginning({1: 1})
        linked_list.insert_at_end({3: 3})
        linked_list.insert_at_end({4: 4})
        self.assertEqual(linked_list.head.data, {1: 1})
        self.assertEqual(linked_list.tail.data, {4: 4})
        self.assertEqual(str(linked_list), "{1: 1} -> {2: 2} -> {3: 3} -> {4: 4} -> None")

    def test_linked_list_end(self):
        linked_list = LinkedList()
        linked_list.insert_at_end({2: 2})
        self.assertEqual(linked_list.head.data, {2: 2})
        self.assertEqual(linked_list.tail.data, {2: 2})

    def test_print_empty(self):
        linked_list = LinkedList()
        self.assertEqual(str(linked_list), 'None')


    def test_to_list(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({2: 2})
        linked_list.insert_beginning({1: 1})
        linked_list.insert_at_end({3: 3})
        linked_list.insert_at_end({4: 4})
        self.assertEqual(linked_list.to_list(), [{1: 1}, {2: 2}, {3: 3}, {4: 4}])


    def test_get_data_by_id(self):
        linked_list = LinkedList()
        linked_list.insert_beginning([1, 1])
        self.assertEqual(linked_list.get_data_by_id(1), None)
        linked_list.insert_beginning({'id': 2})
        # linked_list.insert_beginning({1: 1})
        # linked_list.insert_at_end({3: 3})
        # linked_list.insert_at_end({4: 4})
        self.assertEqual(linked_list.get_data_by_id(2), {'id': 2})