class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_back(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def delete(self, key):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            if prev:
                prev.next = temp.next
            else:
                self.head = temp.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h][i] = (key, value)
                return
        self.table[h].append((key, value))

    def get(self, key):
        h = self._hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return None

    def remove(self, key):
        h = self._hash(key)
        self.table[h] = [(k, v) for (k, v) in self.table[h] if k != key]

def main():
    while True:
        print("\n📘 Data Structures Library")
        print("1. Stack")
        print("2. Queue")
        print("3. Linked List")
        print("4. Binary Search Tree")
        print("5. Hash Table")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            stack = Stack()
            stack.push(10)
            stack.push(20)
            print("Top of stack:", stack.peek())
            print("Popped:", stack.pop())

        elif choice == '2':
            queue = Queue()
            queue.enqueue(10)
            queue.enqueue(20)
            print("Front of queue:", queue.peek())
            print("Dequeued:", queue.dequeue())

        elif choice == '3':
            ll = SinglyLinkedList()
            ll.insert_back(10)
            ll.insert_back(20)
            ll.insert_front(5)
            print("List after insertions:")
            ll.print_list()
            ll.delete(10)
            print("List after deleting 10:")
            ll.print_list()

        elif choice == '4':
            bst = BinarySearchTree()
            bst.insert(30)
            bst.insert(10)
            bst.insert(40)
            bst.insert(20)
            print("Inorder traversal:")
            bst.inorder()

        elif choice == '5':
            ht = HashTable()
            ht.put("name", "Kohinoor")
            ht.put("age", 20)
            print("Name:", ht.get("name"))
            ht.remove("name")
            print("Name after removal:", ht.get("name"))

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
