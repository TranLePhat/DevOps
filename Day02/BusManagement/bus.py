def input_bus():

    plate = input("License Plate: ")

    route = input("Route: ")

    seats = int(input("Total Seats: "))

    while True:

        sold_tickets = int(input("Sold Tickets: "))

        if sold_tickets <= seats:
            break

        print("Error: Sold tickets cannot exceed total seats.")

    ticket_price = float(input("Ticket Price: "))

    return plate, route, seats, sold_tickets, ticket_price