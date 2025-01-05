# --- Binary Search Tree (BST) for Employee Management ---
class EmployeeNode:
    def __init__(self, employee_id, name, shift_time, priority):
        self.employee_id = employee_id  # Unique ID of the employee
        self.name = name                # Employee name
        self.shift_time = shift_time    # Shift time (e.g., '9:00 AM')
        self.priority = priority        # Priority (lower number is higher priority)
        self.left = None                # Left child in BST
        self.right = None               # Right child in BST

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, employee_id, name, shift_time, priority):
        """Insert a new employee into the BST."""
        new_node = EmployeeNode(employee_id, name, shift_time, priority)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, node, new_node):
        """Recursively insert an employee node based on priority."""
        if new_node.priority < node.priority:
            if node.left is None:
                node.left = new_node
            else:
                self._insert_recursive(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert_recursive(node.right, new_node)

    def display_inorder(self, node):
        """In-order traversal to display employees sorted by priority."""
        if node:
            self.display_inorder(node.left)
            print(f"{node.name} (Priority: {node.priority}, Shift: {node.shift_time})")
            self.display_inorder(node.right)

# --- Circular Queue for Shift Request Management ---
class CircularQueue:
    def __init__(self, size):
        self.size = size                # Maximum size of the queue
        self.queue = [None] * size       # List to hold the queue elements
        self.front = -1                  # Front pointer
        self.rear = -1                   # Rear pointer

    def is_full(self):
        """Check if the queue is full."""
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front == -1

    def enqueue(self, employee_id, name, shift_time):
        """Add a new shift request to the queue."""
        if self.is_full():
            print("Queue is full. Overwriting the oldest request.")
            self.dequeue()  # Remove the oldest shift request before adding a new one
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = (employee_id, name, shift_time)
        print(f"Added Shift Request for {name} (Shift: {shift_time})")

    def dequeue(self):
        """Remove the oldest shift request from the queue."""
        if self.is_empty():
            print("Queue is empty. No shift request to dequeue.")
        else:
            removed_request = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1  # Queue is now empty
            else:
                self.front = (self.front + 1) % self.size
            print(f"Removed Shift Request for {removed_request[1]} (Shift: {removed_request[2]})")

    def display(self):
        """Display all shift requests in the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Shift Request Queue:")
            i = self.front
            while i != self.rear:
                print(f"{self.queue[i][1]} (Shift: {self.queue[i][2]})")
                i = (i + 1) % self.size
            print(f"{self.queue[self.rear][1]} (Shift: {self.queue[self.rear][2]})")

# Example Usage: Manage Employees and Shift Requests
if __name__ == "__main__":
    # Create a Binary Search Tree to manage employees by priority
    bst = BinarySearchTree()

    # Insert employees with priority
    bst.insert(employee_id=1, name="Alice", shift_time="9:00 AM - 5:00 PM", priority=2)
    bst.insert(employee_id=2, name="Bob", shift_time="10:00 AM - 6:00 PM", priority=1)
    bst.insert(employee_id=3, name="Charlie", shift_time="8:00 AM - 4:00 PM", priority=3)

    # Display employees sorted by priority (in-order traversal)
    print("Employees sorted by priority (BST):")
    bst.display_inorder(bst.root)

    # Create a Circular Queue to manage shift requests
    queue = CircularQueue(size=3)

    # Add shift requests to the queue
    queue.enqueue(employee_id=1, name="Alice", shift_time="9:00 AM - 5:00 PM")
    queue.enqueue(employee_id=2, name="Bob", shift_time="10:00 AM - 6:00 PM")
    queue.enqueue(employee_id=3, name="Charlie", shift_time="8:00 AM - 4:00 PM")
    queue.enqueue(employee_id=4, name="David", shift_time="7:00 AM - 3:00 PM")  # This will overwrite the oldest request

    # Display the current shift request queue
    queue.display()

    # Remove a shift request from the queue (dequeue)
    queue.dequeue()

    # Display the updated shift request queue
    queue.display()
