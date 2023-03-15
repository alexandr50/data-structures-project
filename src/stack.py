class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None



    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        data_to_push = Node(data)
        if self.top:
            data_to_push.next_node = self.top
        self.top = data_to_push



    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        top = self.top
        self.top = top.next_node
        return top.data

    def __str__(self):
        res  = ''
        cur = self.top
        while cur:
            res += cur.data
            res += '-->'
            cur = cur.next_node
        res += 'None'
        return res


