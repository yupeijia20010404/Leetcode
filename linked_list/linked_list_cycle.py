def hasCycle(self, head: Optional[ListNode]) -> bool:
    if head == None or head.next == None:
        return False
    fast = head.next.next
    slow = head.next
    while fast != slow:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True