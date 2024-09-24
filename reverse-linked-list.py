# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize a pointer to keep track of the previous node
        prev = None

        # Create a helper function to perform the recursive reversal
        def helper(head, prev):

            # Base case:  if the next node is None, return prev (end of the list)
            if head is None:
                return prev

            # Create a variable to represent the next node
            next = head.next

            # Reverse the current node's pointer to point to the previous node
            head.next = prev

            # Call the helper function for the next node, passing the current node as the new previous node
            return helper(next, head)

        # Start the recursive reversal process with the initial head and None for prev
        return helper(head, prev)
        
