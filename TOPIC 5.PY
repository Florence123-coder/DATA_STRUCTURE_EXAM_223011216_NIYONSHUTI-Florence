import heapq

class Employee:
    def __init__(self, name, position, priority):
        self.name = name          # Name of the employee
        self.position = position  # Position of the employee (e.g., Manager, Assistant)
        self.priority = priority  # Priority level of the employee
        self.shift_time = None    # This could be used to track the shift time dynamically

    def __lt__(self, other):
        """This method is needed to compare employees in the heap based on priority"""
        return self.priority < other.priority

    def __repr__(self):
        return f"{self.name} ({self.position}, Priority: {self.priority})"


# Create a min-heap to dynamically track the employees based on their priority
shift_schedule_heap = []

# Function to add an employee to the heap
def add_employee_to_heap(employee):
    heapq.heappush(shift_schedule_heap, employee)
    print(f"Added {employee.name} with Priority {employee.priority} to the heap.")

# Function to get the employee with the highest priority (the root of the heap)
def get_highest_priority_employee():
    if shift_schedule_heap:
        return shift_schedule_heap[0]
    else:
        return None

# Function to remove the highest priority employee from the heap (when shift is assigned)
def assign_shift_to_employee():
    if shift_schedule_heap:
        employee = heapq.heappop(shift_schedule_heap)
        print(f"Assigned shift to {employee.name} with Priority {employee.priority}.")
    else:
        print("No employees available in the heap.")

# Example: Adding employees to the heap
employee1 = Employee("Alice", "CEO", 1)
employee2 = Employee("Bob", "Manager", 2)
employee3 = Employee("John", "Assistant", 3)
employee4 = Employee("Sarah", "Assistant", 3)
employee5 = Employee("Eva", "Worker", 4)

# Add employees to the heap dynamically
add_employee_to_heap(employee1)
add_employee_to_heap(employee2)
add_employee_to_heap(employee3)
add_employee_to_heap(employee4)
add_employee_to_heap(employee5)

# Display the employee with the highest priority (the root of the heap)
print("\nEmployee with the highest priority (root of the heap):")
print(get_highest_priority_employee())

# Assign shifts to employees based on priority
print("\nAssigning shifts to employees based on priority...")
assign_shift_to_employee()  # Assign the highest priority employee
assign_shift_to_employee()  # Assign the next highest priority employee

# Check the remaining employees in the heap
print("\nRemaining employees in the heap:")
for employee in shift_schedule_heap:
    print(employee)
