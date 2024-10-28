#Write a Python class that simulates a Queue. The class should implement methods like push,
#pop, peek (the last two methods should return None if no element is present in the queue).

class Queue:
    def __init__(self):
        self.queue_values=list()

    def push(self, new_val):
        self.queue_values.append(new_val)


    def pop(self):
        if len(self.queue_values) == 0:
            return None
        tmp = self.queue_values[0]
        self.queue_values=self.queue_values[1:]
        return tmp

    def peek(self):
        if len(self.queue_values) == 0:
            return None
        return self.queue_values[0]

def test_queue():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())  # Should print 1
    print(q.peek())  # Should print 2
    print(q.pop())  # Should print 2
    print(q.pop())  # Should print 3
    print(q.pop())  # Should print None

if __name__ == "__main__":
    test_queue()
