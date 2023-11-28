from typing import List, Optional

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return print(f"{self.val}")

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            buf1 = list1[0]
            buf2 = list2[0]
            op = []
            while buf1 is not None and buf2 is not None:
                if buf1.val == buf2.val:
                    op.append(buf1)
                    op.append(buf2)
                    
                    buf1 = buf1.next
                    buf2 = buf2.next

                elif buf1.val < buf2.val:
                    op.append(buf1)
                    buf1 = buf1.next
                elif buf2.val  < buf1.val:
                    op.append(buf2)
                    buf2 = buf2.next

            if buf1 is not None:
                while buf1 is not None:
                    op.append(buf1)
                    buf1 = buf1.next
            if buf2 is not None:
                while buf2 is not None:
                    op.append(buf2)
                    buf2 = buf2.next

            prev = op[0]
            for idx in range(len(op)):
                prev.next = op[idx]
                prev = op[idx]

            return op
                    
                    

def create_nodes(l):

    op = []
    prev = None
    for idx, i in enumerate(l):
        node = ListNode(i)
        if idx != 0:
            prev.next = node
        op.append(node)
        prev = node
    return op




_l1 = [2,3,4,7,9,12]
_l2 = [4, 6, 7, 11, 13]


    
l1 = create_nodes(_l1)
l2 = create_nodes(_l2)

s = Solution()
op = s.mergeTwoLists(l1, l2)

import ipdb; ipdb.set_trace()







