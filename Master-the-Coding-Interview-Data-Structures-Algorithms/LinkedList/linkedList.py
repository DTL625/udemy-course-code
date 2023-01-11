class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedList:
    head = None
    tail = None
    value = None

    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, value):
        if not isinstance(value, listNode):
            value = listNode(value)

        if self.head is None:
            self.head = value
        else:
            self.tail.next = value
        self.tail = value

    def prepend_node(self, value):
        pass

    def print_list(self):
        current = self.head
        rs = []
        while current is not None:
            rs.append(current.value)
            current = current.next
        print(rs)

ll = linkedList()
ll.append_node(10)
ll.append_node(21)
ll.append_node(12)
ll.print_list()

