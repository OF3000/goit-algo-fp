class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

        return self
    
    def bubble_sort(self):
        i= self.head
        while i.next is not None:
            current = self.head
            while current.next is not None:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
            i = i.next
        return self

def merge_sorted(l1, l2):
    res = LinkedList()

    cur1 = l1.head
    cur2 = l2.head

    while cur1 is not None and cur2 is not None:
        if cur1.data < cur2.data:
            res.insert_at_end(cur1.data)
            cur1 = cur1.next
        else:
            res.insert_at_end(cur2.data)
            cur2 = cur2.next
 

    while cur1 is not None:
        #print(cur1.data)
        res.insert_at_end(cur1.data)
        cur1 = cur1.next
    while cur2 is not None:
        res.insert_at_end(cur2.data)
        cur2 = cur2.next

    return res





if __name__ == "__main__":

    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    reversed = llist.reverse_list()
    print("Rreversed:")
    reversed.print_list()

    sorted = llist.bubble_sort()
    print("Sorted:")
    reversed.print_list()

    llist1 = LinkedList()

    # Вставляємо вузли в початок
    llist1.insert_at_beginning(7)
    llist1.insert_at_beginning(12)
    llist1.insert_at_beginning(17)

    # Вставляємо вузли в кінець
    llist1.insert_at_end(18)
    llist1.insert_at_end(19)

    sorted1 = llist1.bubble_sort()
    print("Sorted1:")
    sorted1.print_list()

    print("Merged:")
    merged = merge_sorted(sorted, sorted1)
    merged.print_list()

