def has_cycle(head):
    node = head
    seen_num = []
    while node != None:
        if node.data in seen_num:
            return 1
        seen_num.append(node.data)
        node = node.next
    return 0