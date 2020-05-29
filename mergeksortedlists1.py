# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#this is a bruteforce approach for the leetcode problem.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        
        head = l3 = ListNode(0)
        
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
                
        for x in sorted(self.nodes):
            l3.next = ListNode(x)
            l3 = l3.next
            
        return head.next
        
