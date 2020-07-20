class LinkedListNode:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        count = 0
        curr = self.head
        while (curr):
            if count == index:
                return curr.val
            curr = curr.next
        return -1

    def addAtHead(self, x: int) -> None:
        if self.head is None:
            self.head = LinkedListNode(x)
        else:
            temp = self.head
            self.head = LinkedListNode(x)
            self.head.next = temp
        self.size += 1

    def addAtTail(self, x: int) -> None:
        if (self.head is None):
            self.head = LinkedListNode(x)
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = LinkedListNode(x)
        self.size += 1

    def addAtIndex(self, x: int, index: int) -> None:
        if (index == 0):
            self.addAtHead(x)
        elif (index == self.size):
            self.addAtTail(x)
        elif (0 < index < self.size):
            count = 0
            prev = None
            curr = self.head
            while curr:
                if count == index:
                    node = LinkedListNode(x)
                    prev.next = node
                    node.next = curr
                    self.size += 1
                    return
                prev = curr
                curr = curr.next
                count += 1
        else:
            raise IndexError("Index out of bounds")

    def deleteAtIndex(self, index: int) -> None:
        if (0 <= index < self.size):
            count = 0
            curr = self.head
            prev = None
            while curr:
                if count == index:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.head = curr.next
                    self.size -= 1
                    return
                prev = curr
                curr = curr.next
                count += 1
        else:
            raise IndexError("Index out of bounds")

    def __str__(self) -> str:
        if self.head is None:
            return ""
        res = ""
        curr = self.head
        while curr.next:
            res += "{} -> ".format(curr.data)
            curr = curr.next
        res += "{}".format(curr.data)
        return res

    def has_cycle(self) -> bool:
        """ # 141: Given a linked list, determine if it has a cycle in it. """
        slow_ptr, fast_ptr = self.head, self.head
        while fast_ptr and fast_ptr.next:
            if fast_ptr is slow_ptr:
                return True

            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return False

    """
    Returns the start of cycle detection, and None if there is no cycle.

    Intuition:
    When cycle detected, Slow pointer will meet fast pointer if you start slow pointer at the head
    and increment them both by the same speed, 1.
    """

    def where_is_cycle(self):
        slow_ptr, fast_ptr = self.head, self.head
        while slow_ptr and fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr is slow_ptr:
                # Cycle detected
                slow_ptr = self.head
                while slow_ptr is not fast_ptr:
                    slow_ptr = slow_ptr.next
                    fast_ptr = fast_ptr.next
                return slow_ptr
        return None

    def get_middle_node(self):
        fast_ptr, short_ptr = self.head, self.head
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            short_ptr = short_ptr.next
        return short_ptr

    def reverse(self) -> None:
        prev, curr = None, self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    """
    Reverse a linked list from position m to n. Do it in one-pass.

    NOTE: 1 ≤ m ≤ n ≤ length of list.
    """

    def reverseBetween(self, m: int, n: int) -> None:
        if m == n:
            return

        curr, prev = self.head, None
        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m - 1, n - 1

        con, tail = prev, curr

        while n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1

        if con:
            con.next = prev
        else:
            self.head = prev
        tail.next = curr

    def _reverse(self, node):
        prev, next = None, None
        curr = node
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return node

    def is_palindrome(self) -> bool:
        """
        # 234: Given a singly linked list, determine if it is a palindrome.

        Time complexity - O(n)
        Space complexity - O(1)
        """
        if not self.head or not self.head.next:
            return True

        slowptr, fastptr = self.head, self.head
        mid, prev = None, None

        # get to the middle of linked list
        while fastptr and fastptr.next:
            fastptr = fastptr.next.next
            prev = slowptr
            slowptr = slowptr.next

        # reverse second half and compare the two halves
        if fastptr:
            mid = slowptr
            slowptr = slowptr.next
        second_half = self._reverse(slowptr)
        prev.next = None
        res = compare_ll(self.head, second_half)

        # reconstruct linked list
        if mid:
            prev.next = mid
            mid.next = self._reverse(second_half)
        else:
            prev.next = self._reverse(second_half)

        return res

    def __eq__(self, other):
        head1 = self.head
        head2 = other.head
        while head1 and head2:
            if head1.data == head2.data:
                head1 = head1.next
                head2 = head2.next
            else:
                return False

        if not head1 and not head2:
            return True
        return False


def get_count(node: LinkedListNode) -> int:
    count = 0
    curr = node
    while curr:
        count += 1
        curr = curr.next
    return count


def get_intersection_node(headA: LinkedListNode, headB: LinkedListNode) -> LinkedListNode:
    c1 = get_count(headA)
    c2 = get_count(headB)
    diff = abs(c1 - c2)
    if c1 > c2:
        curr1, curr2 = headA, headB
    else:
        curr1, curr2 = headB, headA

    # Traverse the bigger list by the difference of the lengths
    while diff > 0:
        curr1 = curr1.next
        diff -= 1

    # Traverse both lists in parallel until we come across common node
    while curr1 and curr2:
        if curr1 is curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next
    return None


def add_two_numbers(l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
    remainder = 0
    curr1, curr2 = l1, l2
    l3, front = None, None

    while curr1 or curr2:
        val1 = curr1.data if curr1 else 0
        val2 = curr2.data if curr2 else 0
        currSum = val1 + val2 + remainder

        if currSum > 9:
            currSum = currSum % 10
            remainder = 1
        else:
            remainder = 0

        newNode = LinkedList(currSum)
        if l3:
            l3.next = newNode
            l3 = newNode
        else:
            l3 = newNode
            front = newNode

        curr1 = curr1.next if curr1 else None
        curr2 = curr2.next if curr2 else None

    if remainder == 1:
        l3.next = LinkedListNode(1)
    return front


def reverseList(head: LinkedListNode):
    curr, prev = head, None
    while curr:
        tmp = curr.next
        curr.next = prev
        curr, prev = tmp, curr
    return prev


def reverseListRec(head: LinkedListNode):
    if not head or not head.next:
        return head

    p = reverseListRec(head.next)
    head.next.next = head
    head.next = None
    return p


"""
Write a function to delete a node (except the tail) in a singly linked list, 
given only access to that node.

NOTE:
- The linked list will have at least two elements.
- All of the nodes' values will be unique.
- The given node will not be the tail and it will always be a valid node of the linked list.
"""


def deleteNode(node: LinkedListNode) -> None:
    prev = node
    while node.next:
        node.val = node.next.val
        prev = node
        node = node.next

    prev.next = None


"""
Given a linked list, remove the n-th node from the end of list and return its head.

NOTE: n will always be valid (0 > n > len(linked list)). Solution is done in one-pass.
"""


def removeNthFromEnd(head: LinkedListNode, n: int):
    dummy = LinkedListNode(0)
    dummy.next = head
    first, second = dummy, dummy

    for i in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next


"""
"""


def swap_pairs(head: LinkedListNode):
    if not head:
        return None

    prev, curr = None, head
    while curr and curr.next:
        if not prev:
            head = curr.next
        else:
            prev.next = curr.next

        # swap
        curr.next.next, curr.next = curr, curr.next.next

        # double iteration
        prev = curr
        curr = curr.next

    return head


def compare_ll(node1: LinkedListNode, node2: LinkedListNode) -> bool:
    """ Check if two linked lists are the same by value. """
    while node1 and node2:
        if node1.data == node2.data:
            node1 = node1.next
            node2 = node2.next
        else:
            return False
    return not node1 and not node2


def middle_node(head: LinkedListNode) -> LinkedListNode:
    """
    # 876: Given a non-empty, singly linked list with head node head, return a middle node of linked list.

    NOTE: If there are two middle nodes, return the second middle node.
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def odd_even_list(head: LinkedListNode) -> LinkedListNode:
    """
    # 328: Given a singly linked list, group all odd nodes together followed by the even nodes. 
    Please note here we are talking about the node number and not the value in the nodes.

    You should try to do it in place. The program should run in O(1) space complexity and O(nodes) 
    time complexity.
    """
    if not head:
        return None

    odd, even = head, head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head


def remove_elements(head: LinkedListNode, val: int) -> LinkedListNode:
    """
    # 203: Remove all elements from a linked list of integers that have value val.
    """
    dummy = LinkedListNode(0)
    dummy.next = head

    prev, curr = dummy, head
    while curr:
        if curr.data == val:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.addAtTail(1)
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(4)
    ll.addAtIndex(5, 4)
    assert not ll.is_palindrome()
    print(ll)
    ll.reverseBetween(2, 4)
    print(ll)

    print("Passed all tests!")
