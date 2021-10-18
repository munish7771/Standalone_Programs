# Author: ShubhayuB


# Floyd's cycle detection algorithm is a pointer algorithm that uses only two pointers which move at different speeds.
# The goal is that one of the pointer moves one step at a time while the other pointer moves two steps at a time.
# If these two points meet at some point, we can say, the linked list has a cycle. Else it does not have a cycle.
# This is very famously called as the Tortoise-Hare algorithm, considering the two pointers of different speeds.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def detectCycle(head):

    tortoise = hare = head

    while hare and hare.next:

        # The tortoise is moving one step at once
        tortoise = tortoise.next

        # The hare is moving two steps at once
        hare = hare.next.next

        # If the tortoise and the hare meet, the linked list has a cycle.
        if tortoise == hare:
            return True

    # If tortoise and the hare never meet, it returns false
    return False


if __name__ == '__main__':

    head = None
    for i in reversed(range(5)):
        head = Node(i + 1, head)


    head.next.next.next.next.next = head.next.next

    if detectCycle(head):
        print('Cycle Found')
    else:
        print('No Cycle Found')
