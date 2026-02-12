src/main.py
```python
import time
from dataclasses import dataclass
from typing import Optional

@dataclass
class Message:
    id: str
    content: str
    timestamp: float = time.time()

class MessageQueue:
    def __init__(self):
        self._queue = []

    def enqueue(self, message: Message) -> None:
        """Add a message to the end of the queue."""
        self._queue.append(message)

    def dequeue(self) -> Optional[Message]:
        """Remove and return the oldest message, or None if empty."""
        if self.is_empty():
            return None
        return self._queue.pop(0)

    def peek(self) -> Optional[Message]:
        """Return the oldest message without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self._queue[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._queue) == 0

    def size(self) -> int:
        """Return the number of messages in the queue."""
        return len(self._queue)

    def clear(self) -> None:
        """Remove all messages from the queue."""
        self._queue.clear()

def test_enqueue_dequeue():
    queue = MessageQueue()
    msg1 = Message(id="1", content="Hello")
    msg2 = Message(id="2", content="World")
    queue.enqueue(msg1)
    queue.enqueue(msg2)
    assert queue.dequeue() == msg1
    assert queue.dequeue() == msg2
    assert queue.dequeue() is None

def test_empty_queue():
    queue = MessageQueue()
    assert queue.is_empty()
    assert queue.peek() is None
    assert queue.dequeue() is None

if __name__ == "__main__":
    test_enqueue_dequeue()
    test_empty_queue()
