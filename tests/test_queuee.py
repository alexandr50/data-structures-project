"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import unittest

from src.queuee import Node, Queue

class Test(unittest.TestCase):

    def test_node(self):
        item = Node('data')
        self.assertEqual(item.data, 'data')
        self.assertEqual(item.next_node, None)

    def test_queue(self):
        item = Queue()
        self.assertEqual(item.head, None)
        self.assertEqual(item.tail, None)

    def test_enqueue_dequeue(self):
        item = Queue()
        item.enqueue('data1')
        item.enqueue('data2')
        item.enqueue('data3')
        self.assertEqual(item.head.data, 'data1')
        self.assertEqual(item.tail.data, 'data3')
        item.dequeue()
        self.assertEqual(item.head.data, 'data2')
        self.assertEqual(item.head.next_node.data, 'data3')

    def test_str(self):
        item = Queue()
        self.assertEqual(item.dequeue(), None)
        self.assertEqual(str(item), '')
        item.enqueue('data1')
        item.enqueue('data2')
        item.enqueue('data3')
        self.assertEqual(str(item), "data1\ndata2\ndata3")



