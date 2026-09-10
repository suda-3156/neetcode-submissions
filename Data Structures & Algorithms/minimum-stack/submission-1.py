class StackItem:
    def __init__(self, val: int, next: Optional["StackItem"], next_min: Optional["StackItem"]):
        self.val = val
        self.next = next
        self.next_min = next_min

class MinStack:
    def __init__(self):
        self.head = None
        self.minimum = None

    def push(self, val: int) -> None:
        self.head = StackItem(val, self.head, None)

        if not self.minimum or self.minimum.val >= self.head.val:
            self.head.next_min = self.minimum
            self.minimum = self.head

    def pop(self) -> None:
        if self.head == self.minimum:
            self.minimum = self.minimum.next_min

        self.head = self.head.next

    def top(self) -> int:
        return self.head.val
        
    def getMin(self) -> int:
        return self.minimum.val
