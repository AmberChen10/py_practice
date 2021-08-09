#237. Delete Node in a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
#876. Middle of the Linked List
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy = head
        count = 0     
        while head:
            count+=1
            head = head.next         
        mid = (count//2)
        for i in range(mid):
            dummy = dummy.next     
        return dummy
      
#21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
                
        if l1:
            tail.next = l1
        
        elif l2:
            tail.next = l2
        
        return dummy.next
      
#160. Intersection of Two Linked Lists
