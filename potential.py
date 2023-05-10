# POTENTIAL FOR DYNAMIC TABLE

import math
class AmortizedList:
    def __init__(self):
        self.data = [None]
        self.size = 0
        self.prev_potential = -1
        self.i = 0
        self.ac_cost = 0
        self.amor_cost = 0

    def append(self, item):
        self.ac_cost = 1
        if (self.size == len(self.data) and self.size != 0):
            self.resize()
        self.data[self.size] = item
        self.size += 1
        self.i += 1
        self.potential = 2*self.i - 2**math.ceil(math.log(self.i, 2))
        
        self.amor_cost = self.ac_cost + (self.potential - self.prev_potential)
        print(f"Previous Potential: {self.prev_potential}, Current Potenntial: {self.potential}")
        self.prev_potential = self.potential

        print(f"Actual Cost: {self.ac_cost} Amortized Cost: {self.amor_cost} ")
        print("\n")
        
    def resize(self):
        print(f"Doubling cost: {self.size}")
        new_data = [None] * (2 * len(self.data))
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.ac_cost = self.ac_cost + self.size
        self.data = new_data
        
    
new_list = AmortizedList()

for i in range(1, 11):
    print(f"Insert {i}")
    new_list.append(i)
    print(f'Size of Array: {new_list.size}, Capacity of Array: {len(new_list.data)}')


# POTENTIAL METHOD FOR AUGMENTED STACK

import math

class AugmentedStack:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.prev_potential = -1
        self.i = 0
        self.ac_cost = 0
        self.amor_cost = 0

    def push(self, item):
        self.ac_cost = 1
        self.stack.append(item)
        self.size += 1
        self.i += 1
        self.potential = 2 * self.i - 2 ** math.ceil(math.log(self.i, 2))
        self.amor_cost = self.ac_cost + (self.potential - self.prev_potential)
        print(f"Previous Potential: {self.prev_potential}, Current Potential: {self.potential}")
        self.prev_potential = self.potential
        print(f"Actual Cost: {self.ac_cost}, Amortized Cost: {self.amor_cost}")
        print("\n")

    def pop(self):
        if self.size == 0:
            print("Stack is empty!")
            return None
        item = self.stack.pop()
        self.size -= 1
        self.ac_cost = 1
        self.i += 1
        self.potential = 2 * self.i - 2 ** math.ceil(math.log(self.i, 2))
        self.amor_cost = self.ac_cost + (self.potential - self.prev_potential)
        print(f"Previous Potential: {self.prev_potential}, Current Potential: {self.potential}")
        self.prev_potential = self.potential
        print(f"Actual Cost: {self.ac_cost}, Amortized Cost: {self.amor_cost}")
        print("\n")
        return item

    def top(self):
        if self.size == 0:
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return self.size == 0


stack = AugmentedStack()

for i in range(1, 11):
    print(f"Push {i}")
    stack.push(i)
    print(f"Size of Stack: {stack.size}")
    print()

for _ in range(1, 11):
    print(f"Pop: {stack.pop()}")
    print(f"Size of Stack: {stack.size}")
    print()