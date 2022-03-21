def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)  # set dummy val=0, .next 是head

    # reach node before left
    leftPrev = dummy
    curr = head
    for i in range(left - 1):
        leftPrev, curr = curr, curr.next
    # now curr=left, leftPrev=node before left

    # reverse from left to right
    prev = None
    for i in range(right - left + 1):
        tmpNext = curr.next
        curr.next = prev
        prev, curr = curr, tmpNext

    # update pointers
    leftPrev.next.next = curr  # curr is node after right
    leftPrev.next = prev  # prev is right

    return dummy.next