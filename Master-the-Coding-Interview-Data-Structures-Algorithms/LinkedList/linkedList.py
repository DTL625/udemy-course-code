# ch. 100
class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedList:
    head = None
    tail = None
    value = None
    len = 0

    def __init__(self):
        self.head = None
        self.tail = None

    # ch.97
    def append_node(self, value):
        if not isinstance(value, listNode):
            value = listNode(value)

        if self.head is None:
            self.head = value
        else:
            self.tail.next = value
        self.tail = value
        self.len += 1

    # ch.98
    def prepend_node(self, value):
        if not isinstance(value, listNode):
            value = listNode(value)
        if self.head is not None:
            value.next = self.head
        self.head = value
        self.len += 1

    def insert(self, idx, value):
        if not isinstance(value, listNode):
            value = listNode(value)
        if idx == 0:
            self.prepend_node(value)
        elif idx > self.len:
            self.append_node(value)

        current = self.head
        current_idx = 1

        while current is not None:
            if current_idx == idx:
                value.next = current.next
                current.next = value
            current = current.next
            current_idx += 1
        self.len += 1

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
# ll.prepend_node(15)
ll.append_node(4)
ll.append_node(3)
ll.print_list()
ll.insert(5, 80)
# ll.prepend_node(31)

ll.print_list()
