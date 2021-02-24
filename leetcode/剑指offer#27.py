class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode = None
        currNode = head
        while currNode:
            nextNode = currNode.next
            currNode.next = preNode
            preNode = currNode
            currNode = nextNode
        return preNode
