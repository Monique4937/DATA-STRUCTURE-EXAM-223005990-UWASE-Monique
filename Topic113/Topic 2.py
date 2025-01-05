class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
        elif self.front == -1: 
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
            return None
        elif self.front == self.rear:  
            item = self.queue[self.front]
            self.front = self.rear = -1
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
        return item

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
            return
        print("Circular Queue elements:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.stack:
            print("Stack is empty!")
            return None
        return self.stack.pop()

    def display(self):
        if not self.stack:
            print("Stack is empty!")
            return
        print("Stack elements:")
        print(self.stack[::-1])

print("Circular Queue:")
cq = CircularQueue(5)
cq.enqueue("Vendor Request 1")
cq.enqueue("Vendor Request 2")
cq.enqueue("Vendor Request 3")
cq.display()
print(f"Dequeued: {cq.dequeue()}")
cq.display()

print("\nStack:")
stack = Stack()
stack.push("Task 1: Confirm booking")
stack.push("Task 2: Send invoice")
stack.push("Task 3: Schedule meeting")
stack.display()
print(f"Popped: {stack.pop()}")
stack.display()
