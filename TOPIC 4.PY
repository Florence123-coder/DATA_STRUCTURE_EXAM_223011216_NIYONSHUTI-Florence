import heapq

class Order:
    def __init__(self, order_id, employee_name, shift_time, priority):
        self.order_id = order_id            # Unique order identifier
        self.employee_name = employee_name  # Name of the employee requesting the shift
        self.shift_time = shift_time        # Shift time for the employee
        self.priority = priority            # Priority of the order (lower is higher priority)

    def __lt__(self, other):
        """Comparison function to define order in the heap based on priority"""
        return self.priority < other.priority

    def __repr__(self):
        return f"Order {self.order_id} - {self.employee_name} (Priority: {self.priority}, Shift: {self.shift_time})"

# Create a fixed-size min-heap for tracking orders
class OrderQueue:
    def __init__(self, max_size):
        self.max_size = max_size  # Maximum size of the heap (fixed number of orders)
        self.heap = []  # Min-heap to store orders

    def add_order(self, order):
        """Add an order to the heap, removing the least important order if heap is full"""
        if len(self.heap) < self.max_size:
            heapq.heappush(self.heap, order)
            print(f"Order {order.order_id} added: {order}")
        else:
            # If heap is full, pop the least important order and add the new order
            removed_order = heapq.heappop(self.heap)
            heapq.heappush(self.heap, order)
            print(f"Order {order.order_id} added: {order}. Removed least important order: {removed_order}")

    def get_orders(self):
        """Return all orders in the heap"""
        return self.heap

    def process_order(self):
        """Process (pop) the order with the highest priority (lowest priority number)"""
        if self.heap:
            order = heapq.heappop(self.heap)
            print(f"Processing order: {order}")
        else:
            print("No orders to process.")

# Example: Managing orders with a fixed number of slots
order_queue = OrderQueue(max_size=3)

# Creating orders
order1 = Order(order_id=1, employee_name="Alice", shift_time="9:00 AM", priority=1)
order2 = Order(order_id=2, employee_name="Bob", shift_time="10:00 AM", priority=2)
order3 = Order(order_id=3, employee_name="Charlie", shift_time="11:00 AM", priority=3)
order4 = Order(order_id=4, employee_name="David", shift_time="12:00 PM", priority=1)

# Add orders to the heap
order_queue.add_order(order1)
order_queue.add_order(order2)
order_queue.add_order(order3)
order_queue.add_order(order4)

# Display remaining orders in the heap
print("\nRemaining Orders in the Queue (Heap):")
for order in order_queue.get_orders():
    print(order)

# Process an order (pop the highest priority order)
order_queue.process_order()

# Display remaining orders after processing
print("\nRemaining Orders after Processing:")
for order in order_queue.get_orders():
    print(order)

