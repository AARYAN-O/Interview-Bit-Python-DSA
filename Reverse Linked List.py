# Definition for singly-linked list.
class ListNode:
	def __init__(self,value=0,next=None):
		self.value=value
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):
        prev=None
        current=A
	# currrent.next contains the address of the next node.
	# prev is a Node and current.next is a pointer to the next node.
	# Then, how can two things having different datatypes be on the either sides of equals to operator.
	# This is so because they are both part of same Nodes.
	
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        
        return prev
