#Write a Python class that simulates a Stack. The class should implement methods like push,
# pop, peek (the last two methods should return None if no element is present in the stack).
from torch.distributed.tensor import empty


class Stack:
    def __init__(self):
        self.stack_val=list()

    def push(self,new_val):
        self.stack_val.append(new_val)
    def pop(self):
        if len(self.stack_val) == 0:
            return None
        return self.stack_val.pop()
    def peek(self):
        if len(self.stack_val) == 0:
            return None
        return self.stack_val[len(self.stack_val)-1]

def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  # Should print 3
    print(s.peek())  # Should print 2
    print(s.pop())  # Should print 2
    print(s.pop())  # Should print 1
    print(s.pop())  # Should print None

if __name__ == "__main__":
    test_stack()

