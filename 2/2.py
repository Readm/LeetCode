class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def one_digit(n1, n2, carry):
            #carry: 0 or 1
            if not (n1 or n2 or carry):
                return None
            elif not (n1 or n2) and carry:
                return ListNode(1)
            else:
                if not n1:
                    n1 = ListNode(0)
                if not n2:
                    n2 = ListNode(0)

                num = n1.val + n2.val + carry
                new_carry = num/10

                ln = ListNode(num % 10)
                ln.next = one_digit(n1.next, n2.next, new_carry)
                return ln
        return one_digit(l1, l2, 0)

