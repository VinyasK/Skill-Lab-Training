class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    first = dummy
    second = dummy
    
    for _ in range(n + 1):
        first = first.next
    
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    
    return dummy.next

def print_list(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("null")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(remove_nth_from_end(head, 2))  

head = ListNode(1)
print_list(remove_nth_from_end(head, 1))  

head = ListNode(1, ListNode(2))
print_list(remove_nth_from_end(head, 1))  
