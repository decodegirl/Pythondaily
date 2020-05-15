 # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add_two_numbers(self, l1,l2):
        head = l3 = ListNode(0)
        carry = 0 

        #check if they exist
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
                
            if l2:
                carry += l2.val
                l2 = l2.next
            
            #update l3(change intewger val on the node on l3)
                
            l3.val = carry % 10
            carry =  carry //10
            
            #iterate l3 forward if there is l2 or l2 or carry
            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
                
        return head
    
   