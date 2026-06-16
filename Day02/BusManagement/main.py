from bus import input_bus

from revenue import calculate_revenue
from revenue import calculate_empty_seats

from report import print_report


def main():

    plate, route, seats, sold_tickets, ticket_price = input_bus()

    revenue = calculate_revenue(
        sold_tickets,
        ticket_price
    )

    empty_seats = calculate_empty_seats(
        seats,
        sold_tickets
    )

    print_report(
        plate,
        route,
        seats,
        sold_tickets,
        empty_seats,
        ticket_price,
        revenue
    )


if __name__ == "__main__":
    main()