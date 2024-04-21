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
def new_ticket():
    customer = input('What is the customers name?\n')
    issue = input('What is the issue?\n')
    status = input('Is the status open,closed, or pending?\n')
    service_tickets["Ticket003"] = {
        'Customer': customer,
        'Issue': issue,
        'Status': status
    }
    print('New Service Ticket Added!')
    print(service_tickets)

def update_status():
    print(service_tickets)
    ticket_choice = input('What ticket status would you like to update?\n')
    print(ticket_choice)
    new_status = input(f'What is the new status of ticket {ticket_choice}?')
    service_tickets[ticket_choice]['Status'] = new_status
    print('Updated Status!')
    print(service_tickets)

def view_tickets():
    print(service_tickets)
    

guest_selection = int(input("How can we help with your service ticket(s) today? 1.) Open New Service Ticket, 2.)Update Service Ticket Status, 3.) Display all service tickets:"))
if guest_selection == 1:
    new_ticket()
elif guest_selection == 2:
    update_status()
elif guest_selection == 3:
    view_tickets()
else:
    print('Invalid Selection!')