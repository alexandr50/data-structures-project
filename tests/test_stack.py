"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack, Node


class Test(unittest.TestCase):

    def test_node_1(self):
        item = Node(10)
        self.assertEqual(item.data, 10)
        self.assertEqual(item.next_node, None)

    def test_stack(self):
        item = Stack()
        self.assertEqual(item.top, None)
        self.assertEqual(item.stack_data, [])

    def test_node_2(self):
        item = Stack()
        item.push('data_1')
        item.push('data_2')
        self.assertEqual(item.top.data, 'data_2')
        item.pop()
        self.assertEqual(len(item.stack_data), 1)
