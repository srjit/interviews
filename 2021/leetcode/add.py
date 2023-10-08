from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        flag = 1
        root = None
        carry = 0
        begin = None
        
        while l1 is not None and l2 is not None:

            num1 = l1.val
            num2 = l2.val
                    
            sum_ = num1 + num2 + carry
            if len(str(sum_)) > 1:
                carry = int(str(sum_)[0])
                add_ = int(str(sum_)[1])
            else:
                carry = 0
                add_ = int(str(sum_)[0])
                            
            l1 = l1.next
            l2 = l2.next

            root = ListNode()
            root.val = add_
            root.next = None
            if flag == 1:
                begin = root
                flag = 0

            root = root.next
            

        if carry > 0:
            root = ListNode()
            root.val = carry
            root.next = None

            
        return begin


sol = Solution()

l1 = ListNode()
l2 = ListNode()
l3 = ListNode()
l1.val = 2
l1.next = l2
l2.val = 4
l2.next = l3
l3.val = 3
l3.next = None

l4 = ListNode()
l5 = ListNode()
l6 = ListNode()
l4.val = 5
l4.next = l5
l5.val = 6
l5.next = l6
l6.val = 4
l6.next = None

x = sol.addTwoNumbers(l1, l4)
print(x.val, x.next)
