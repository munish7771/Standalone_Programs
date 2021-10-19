#Author: ShubhayuB
# Python provides a built-in implementation of a priority queue.
#  The queue module is imported and the elements are inserted using the put() method. 
# The while loop is used to dequeue the elements using the get() method. 
# The time complexity of the queue.PriorityQueue class is O(log n).
from queue import PriorityQueue
print("Goal: To accept the rank and name of students enrolled in CS F111 and display their names according to rank:")
q = PriorityQueue()
print("No. of students")
num = int(input("Enter the value:"))
count = 0
while ( count < num) :
    count = count + 1
    name = input("Enter the name:")
    rank = input("Enter the rank:")
    q.put((rank, name))

print("The names of students enrolled in CSE F111 Class  based on their rank:")
while not q.empty():
    next_item = q.get()
    print(next_item)
