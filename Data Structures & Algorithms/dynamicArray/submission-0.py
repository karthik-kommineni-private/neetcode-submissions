class DynamicArray:
    # A simple resizable array implementation

    def __init__(self, capacity: int):
        # Initialize with given capacity
        self.arr = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        # Return element at index i
        # NOTE: Missing boundary check (assumes 0 <= i < size)
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Overwrite element at index i with n
        # NOTE: Missing boundary check (assumes 0 <= i < size)
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Append n; resize if we've reached capacity
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Remove and return last element (returns None if empty)
        if self.size > 0:
            self.size -= 1
            return self.arr[self.size]

    def resize(self):
        # Double capacity and copy elements into new list
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        # Return current number of stored elements
        return self.size

    def getCapacity(self) -> int:
        # Return current capacity before next resize
        return self.capacity
