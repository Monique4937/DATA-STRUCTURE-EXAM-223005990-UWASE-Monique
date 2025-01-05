class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:  
            print(f"Queue is full! Cannot add: {item}")
        elif self.front == -1:  
            self.front = self.rear = 0
            self.queue[self.rear] = item
            print(f"Enqueued: {item}")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print(f"Enqueued: {item}")

    def dequeue(self):
        if self.front == -1: 
            print("Queue is empty! No item to dequeue.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear: 
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued: {item}")
        return item

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
            return
        print("Current Circular Queue:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


print("Dynamic Tracking with Circular Queue:")
queue_size = 5
cq = CircularQueue(queue_size)


cq.enqueue("Vendor Inquiry 1")
cq.enqueue("Customer Booking 2")
cq.enqueue("Vendor Inquiry 3")
cq.enqueue("Customer Inquiry 4")
cq.enqueue("Vendor Assignment 5")  
cq.display()

cq.dequeue()  
cq.enqueue("New Booking 6")  
cq.display()
