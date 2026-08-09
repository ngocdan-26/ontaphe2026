import re

raw_tickets = [
    {
        "ticket_id": "TCK001",
        "movie": "Avengers: Endgame",
        "price": 120000,
        "seat": "A12",
        "status": "booked"
    },
    {
        "ticket_id": " tck002 ",
        "movie": "Spider-man: No Way Home",
        "price": 150000,
        "seat": "B05",
        "status": "available"
    },
    {
        "ticket_id": "TCK003",
        "movie": "The Batman",
        "price": 130000,
        "seat": "C08",
        "status": "booked"
    },
    {
        "ticket_id": "TCK004",
        "movie": "Superman: Legacy",
        "price": 140000,
        "seat": "D10",
        "status": "cancelled"
    },
    {
        "ticket_id": "TCK005",
        "movie": "Ironman: Rise of Technovore",
        "price": 160000,
        "seat": "E15",
        "status": "booked"
    }
]


def clean_and_validate_tickets(tickets):
    result = []

    pattern = r"^TCK\d{3,}$"

    for ticket in tickets:
        code = ticket["ticket_id"].strip().upper()

        if re.match(pattern, code):
            ticket["ticket_id"] = code
            result.append(ticket)

    return result


def search_tickets(tickets, max_price, status=None):
    result = []

    for ticket in tickets:
        if ticket["price"] <= max_price:
            if status is None:
                result.append(ticket)
            elif ticket["status"] == status:
                result.append(ticket)

    return result


def sort_tickets_by_price_asc(tickets):
    n = len(tickets)

    for i in range(n):
        for j in range(0, n - i - 1):
            if tickets[j]["price"] > tickets[j + 1]["price"]:
                tickets[j], tickets[j + 1] = tickets[j + 1], tickets[j]

    return tickets