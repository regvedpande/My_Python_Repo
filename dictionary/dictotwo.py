# 🎯 Simple Support Ticket Tracker using Python Dictionary

# Initialize the ticket database
tickets = {
    101: {"title": "Login Issue", "status": "Open", "priority": "High"},
    102: {"title": "Page Not Loading", "status": "In Progress", "priority": "Medium"},
    103: {"title": "Feature Request", "status": "Closed", "priority": "Low"}
}

# Function to display all tickets
def display_tickets():
    print("\n📋 Current Tickets:")
    for ticket_id, details in tickets.items():
        print(f"ID: {ticket_id} | Title: {details['title']} | Status: {details['status']} | Priority: {details['priority']}")

# Function to update ticket status
def update_status(ticket_id, new_status):
    if ticket_id in tickets:
        tickets[ticket_id]["status"] = new_status
        print(f"✅ Ticket {ticket_id} status updated to '{new_status}'")
    else:
        print(f"❌ Ticket ID {ticket_id} not found.")

# Function to add a new ticket
def add_ticket(ticket_id, title, status, priority):
    if ticket_id not in tickets:
        tickets[ticket_id] = {"title": title, "status": status, "priority": priority}
        print(f"🆕 Ticket {ticket_id} added.")
    else:
        print(f"⚠️ Ticket ID {ticket_id} already exists.")

# Demo usage
display_tickets()
update_status(102, "Resolved")
add_ticket(104, "Database Timeout", "Open", "High")
display_tickets()
