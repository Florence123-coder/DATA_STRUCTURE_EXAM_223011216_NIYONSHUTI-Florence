class EmployeeNode:
    def __init__(self, name, position, shift_time):
        self.name = name          # Name of the employee
        self.position = position  # Position of the employee (e.g., Manager, Worker)
        self.shift_time = shift_time  # Time of the shift for the employee
        self.next = None  # Pointer to the next employee node
        self.prev = None  # Pointer to the previous employee node

    def __repr__(self):
        return f"{self.name} ({self.position}) - Shift: {self.shift_time}"

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head of the list
        self.tail = None  # Tail of the list

    def add_employee_at_end(self, name, position, shift_time):
        """Add an employee at the end of the list"""
        new_employee = EmployeeNode(name, position, shift_time)
        if self.head is None:
            # If the list is empty, both head and tail will point to the new employee
            self.head = self.tail = new_employee
        else:
            # Attach the new employee to the end of the list
            self.tail.next = new_employee
            new_employee.prev = self.tail
            self.tail = new_employee
        print(f"Employee {new_employee.name} added at the end.")

    def add_employee_at_start(self, name, position, shift_time):
        """Add an employee at the start of the list"""
        new_employee = EmployeeNode(name, position, shift_time)
        if self.head is None:
            # If the list is empty, both head and tail will point to the new employee
            self.head = self.tail = new_employee
        else:
            # Attach the new employee to the start of the list
            new_employee.next = self.head
            self.head.prev = new_employee
            self.head = new_employee
        print(f"Employee {new_employee.name} added at the start.")

    def remove_employee(self, name):
        """Remove an employee by name"""
        current = self.head
        while current:
            if current.name == name:
                # If the employee is found
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # If it's the head node
                    self.head = current.next
                if current == self.tail:  # If it's the tail node
                    self.tail = current.prev
                print(f"Employee {current.name} removed from the list.")
                return
            current = current.next
        print(f"Employee {name} not found.")

    def display_schedule(self):
        """Display all employees' shifts in the list"""
        if not self.head:
            print("No employees in the list.")
            return
        current = self.head
        print("Workplace Shift Schedule:")
        while current:
            print(current)
            current = current.next

    def display_reverse_schedule(self):
        """Display all employees' shifts in reverse order"""
        if not self.tail:
            print("No employees in the list.")
            return
        current = self.tail
        print("Workplace Shift Schedule (Reverse):")
        while current:
            print(current)
            current = current.prev

# Example Usage:
shift_schedule = DoublyLinkedList()

# Add employees to the shift schedule
shift_schedule.add_employee_at_end("Alice", "Manager", "9:00 AM - 5:00 PM")
shift_schedule.add_employee_at_end("Bob", "Assistant", "10:00 AM - 6:00 PM")
shift_schedule.add_employee_at_start("Charlie", "Worker", "8:00 AM - 4:00 PM")

# Display the current shift schedule
shift_schedule.display_schedule()

# Remove an employee from the list
shift_schedule.remove_employee("Bob")

# Display the updated shift schedule
shift_schedule.display_schedule()

# Display the reverse of the shift schedule
shift_schedule.display_reverse_schedule()
