tickets = []

def create_ticket(title, user, priority):
    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "user": user,
        "priority": priority,
        "status": "OPEN"
    }
    tickets.append(ticket)
    return ticket


def get_tickets():
    return tickets