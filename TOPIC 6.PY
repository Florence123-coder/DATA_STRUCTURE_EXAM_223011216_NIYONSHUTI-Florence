class Employee:
    def __init__(self, name, position, priority):
        self.name = name        # Name of the employee
        self.position = position  # Position of the employee (e.g., Manager, Assistant)
        self.priority = priority  # Priority level of the employee
        self.subordinates = []  # List to hold direct subordinates (children)

    def add_subordinate(self, employee):
        """Add a subordinate (child) to the employee"""
        self.subordinates.append(employee)

    def display_hierarchy(self, level=0):
        """Display the employee hierarchy in a readable format"""
        indent = "  " * level  # Add indentation based on level in the tree
        print(f"{indent}{self.name} ({self.position}, Priority: {self.priority})")
        for subordinate in self.subordinates:
            subordinate.display_hierarchy(level + 1)

# Example: Creating a hierarchical structure for the workplace shift scheduling system

# Create employees
ceo = Employee("Alice", "CEO", 1)
manager_1 = Employee("Bob", "Manager", 2)
manager_2 = Employee("Eva", "Manager", 2)
assistant_1 = Employee("John", "Assistant", 3)
assistant_2 = Employee("Sarah", "Assistant", 3)
worker_1 = Employee("Jake", "Worker", 4)
worker_2 = Employee("Lily", "Worker", 4)

# Building the hierarchy
ceo.add_subordinate(manager_1)
ceo.add_subordinate(manager_2)

manager_1.add_subordinate(assistant_1)
manager_1.add_subordinate(assistant_2)

assistant_1.add_subordinate(worker_1)
assistant_2.add_subordinate(worker_2)

# Display the hierarchical structure
print("Workplace Shift Scheduling Hierarchy:")
ceo.display_hierarchy()
