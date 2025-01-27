class Solution:

    # Function to rotate a linked list.
    def rotate(self, head, k):
        n = 1
        s = head
        p = None
        e = None
        while head.next:
            n += 1
            head = head.next
        e = head

        if (k % n):
            head = s
            for i in range(1, (k % n)):
                head = head.next
            e.next = s
            s = head.next
            head.next = None
        return s