def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 == None and list2 == None:
        return list1
    if list1 == None and list2 != None:
        return list2
    if list1 != None and list2 == None:
        return list1
    if list1.val <= list2.val:
        head = ListNode(list1.val, None)
        list1 = list1.next
    else:
        head = ListNode(list2.val, None)
        list2 = list2.next
    pointer = head
    while list1 != None and list2 != None:
        if list1.val <= list2.val:
            pointer.next = ListNode(list1.val, None)
            list1 = list1.next
        else:
            pointer.next = ListNode(list2.val, None)
            list2 = list2.next
        pointer = pointer.next
    if list1 != None:
        pointer.next = list1
    if list2 != None:
        pointer.next = list2
    return head