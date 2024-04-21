# # 3. Python Programming Challenges for Customer Service Data Handling

# # Objective: This assignment is designed to test and enhance your Python programming skills,
# # focusing on real-world applications in customer service data management. 
# # You will practice correcting code, organizing customer data, and implementing a feedback system 
# # using Python dictionaries.

# # Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and 
# # loops by creating a system to track customer service tickets.

# # Problem Statement: Develop a program a function that:
# # Tracks customer service tickets, each with a unique ID, customer name, issue description, 
# # and status (open/closed).
# # Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.

# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

guest_selection = input("How can we help with your service ticket(s) today? 1.) Open New Service Ticket, 2.)Update Service Ticket, 3.) Show Current Status of Service Ticket, 4.) Display all service tickets:")

if guest_selection == 1:
    service_tickets ['Ticket003'] 
    print(service_tickets)