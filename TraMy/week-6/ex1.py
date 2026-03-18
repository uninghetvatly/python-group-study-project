# Reverse Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if (head == None):
            return head
        prev = None
        current = head
        while (current):
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev
        