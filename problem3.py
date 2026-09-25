# problem 3 AI logics


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_node(values):
    head = None
    tail = None

    for x in values:
        new = Node(x)

        if head is None:
            head = new
            tail = new
        else:
            tail.next = new
            tail = new

    return head


def add(linked_list1, linked_list2):
    head = None
    tail = None
    carry = 0

    while linked_list1 or linked_list2 or carry:

        if linked_list1:
            a = linked_list1.data
        else:
            a = 0

        if linked_list2:
            b = linked_list2.data
        else:
            b = 0

        total = a + b + carry

        new = Node(total % 10)
        carry = total // 10

        if head is None:
            head = new
            tail = new
        else:
            tail.next = new
            tail = new

        if linked_list1:
            linked_list1 = linked_list1.next

        if linked_list2:
            linked_list2 = linked_list2.next

    return head


def display(head):
    while head:
        print(head.data, end=" ")
        head = head.next


n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

linked_list1 = create_node(a)
linked_list2 = create_node(b)

result = add(linked_list1, linked_list2)

display(result)