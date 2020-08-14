import sys
sys.path.append('../')
from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.current.next
            return
        if self.storage.length >= self.capacity:
            if self.current == self.storage.tail:
                self.current = self.storage.head
                self.current.value = item
            else:
                self.current.next.value = item
                self.current = self.current.next

    def get(self):
        buffli = []
        node = self.storage.head

        while node:
            buffli.append(node.value)
            node = node.next
        return buffli