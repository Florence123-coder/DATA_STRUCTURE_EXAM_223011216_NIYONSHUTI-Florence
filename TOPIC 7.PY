class Employee:
    def __init__(self, name, position, shift_time, priority):
        self.name = name         # Name of the employee
        self.position = position # Position of the employee (e.g., Manager, Worker)
        self.shift_time = shift_time  # Time of the shift (e.g., '9:00 AM - 5:00 PM')
        self.priority = priority  # Priority of the employee (lower number means higher priority)

    def __repr__(self):
        return f"{self.name} ({self.position}) - Shift: {self.shift_time} (Priority: {self.priority})"

def insertion_sort(employees):
    """Sort the list of employees based on priority using Insertion Sort"""
    for i in range(1, len(employees)):
        key = employees[i]
        j = i - 1
        while j >= 0 and key.priority < employees[j].priority:
            employees[j + 1] = employees[j]
            j -= 1
        employees[j + 1] = key

def display_schedule(employees):
    """Display all the employees' shifts after sorting"""
    if not employees:
        print("No employees to display.")
        return
    print("Workplace Shift Schedule (Sorted by Priority):")
    for employee in employees:
        print(employee)

# Example Usage:
if __name__ == "__main__":
    # Create a list of employees (unsorted by priority)
    employees = [
        Employee("Alice", "Manager", "9:00 AM - 5:00 PM", 2),
        Employee("Bob", "Assistant", "10:00 AM - 6:00 PM", 1),
        Employee("Charlie", "Worker", "8:00 AM - 4:00 PM", 3),
        Employee("David", "Supervisor", "7:00 AM - 3:00 PM", 0),
        Employee("Eve", "Intern", "11:00 AM - 7:00 PM", 4)
    ]

    print("Before sorting:")
    display_schedule(employees)

    # Sort employees by priority using Insertion Sort
    insertion_sort(employees)

    print("\nAfter sorting:")
    display_schedule(employees)
