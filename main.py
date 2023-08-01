import os

USERS_FILE = "usersfile.txt" #This file will store admin and user credentials 

TICKETS_FILE = "ticketsfile.txt"

def find_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            for line in file:
                username, password, user_type = line.strip().split(',')
                users[username] = (password, user_type)
    return users

def login_U():
    users = find_users()
    max_attempts = 5
    while max_attempts > 0:
        username = input("please enter here your username: ")
        password = input("Please enter here your password: ")

        if username in users and password == users[username][0]:
            return users[username][1]
        else:
            print("Error <Incorrect Username or Password>")
            max_attempts -= 1

    print("login error <max number of attempts is reached>. ")
    exit()

def ad_menu():
    print("Greetings Admin!!")

def us_menu():
    print("Greetings User!!")

def main():
    user_type = login_U()
    if user_type == "admin":
        ad_menu()
    else:
        us_menu()



class Ticket:
    def tickets_prop(self, ticket_id, event_id, username, timestamp, priority):
        self.ticket_id = ticket_id
        self.event_id = event_id
        self.username = username
        self.timestamp = timestamp
        self.priority = int(priority)

def find_tickets():
    tickets = []
    if os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, "r") as file:
            for line in file:
                ticket_data = line.strip().split(',')
                ticket = Ticket(*ticket_data)
                tickets.append(ticket)
    return tickets

def view_ticket(tickets):
    for ticket in tickets:
        print(
            "Ticket ID: {ticket.ticket_id}, Event ID: {ticket.event_id}, "
            "Username: {ticket.username}, Timestamp: {ticket.timestamp}, Priority: {ticket.priority}"
        )

def main():
    tickets = find_tickets()
    print("Here  is the Ticketing System ")
    while True:
        print("\nMenu:")
        print("1. View all tickets")
        print("2. Sort tickets by priority")
        print("3. Search for tickets by username")
        print("4. Exit")
        choice = input("Please enter your choice: ")

        if choice == "1":
            view_tickets(tickets)
        elif choice == "2":
            sorted_tickets = sorted(tickets, key=lambda ticket: ticket.priority)
            view_tickets(sorted_tickets)
        elif choice == "3":
            search_username = input("Enter your username to search for tickets: ")
            found_tickets = [ticket for ticket in tickets if ticket.username == search_username]
            if found_tickets:
                view_tickets(found_tickets)
            else:
                print("Nothing found for this username: {search_username}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. please try again later..")



def display_Q(tickets):
    event_ticket_count = {}
    for ticket in tickets:
        event_id = ticket.event_id
        event_ticket_count[event_id] = event_ticket_count.get(event_id, 0) + 1
    
    if event_ticket_count:
        max_event_id = max(event_ticket_count, key=event_ticket_count.get)
        print(f"Event ID with the highest number of tickets: {max_event_id}")
    else:
        print("No tickets found in the system.")

def bookTicket(tickets, username):
    ticket_id = len(tickets) + 1
    event_id = input("please emter the event ID for the new ticket: ")
    timestamp = input("please enter the date of the event like (YYYYMMDD): ")
    priority = input("please enter the priority of the ticket: ")
    new_ticket = input(ticket_id, event_id, username, timestamp, priority)
    tickets.append(new_ticket)
    print("Your Ticket is booked successfully!")

def view_tickets(tickets):
    sorted_tickets = sorted(tickets, key=lambda ticket: (ticket.timestamp, ticket.event_id))
    today = datetime.today().strftime('%Y%m%d')
    print("Tickets found in the system (Today, Tomorrow, etc.):")
    for ticket in sorted_tickets:
        if ticket.timestamp >= today:
            print(
                f"Ticket ID: {ticket.ticket_id}, Event ID: {ticket.event_id}, "
                f"Username: {ticket.username}, Date: {ticket.timestamp}, Priority: {ticket.priority}"
            )

def changePriority(tickets, ticket_id):
    found = False
    for ticket in tickets:
        if ticket.ticket_id == ticket_id:
            new_priority = input("what's the new priority for the ticket? ")
            ticket.priority = int(new_priority)
            print("Your Tickets' Priority updated successfully!")
            found = True
            break
    if not found:
        print("No available Ticket.")

def remove_ticket(tickets, ticket_id):
    found = False
    for ticket in tickets:
        if ticket.ticket_id == ticket_id:
            tickets.remove(ticket)
            print("This Ticket  is removed from the system.")
            found = True
            break
    if not found:
        print("No available Ticket.")

def Show_events(tickets):
    today = datetime.today().strftime('%Y%m%d')
    today_events = [ticket for ticket in tickets if ticket.timestamp == today]
    if not today_events:
        print("No events today.")
        return

    today_events.sort(key=lambda ticket: ticket.priority)
    print("Events today are sorted by priority:")
    for event in today_events:
        print(
            f"Ticket ID: {event.ticket_id}, Event ID: {event.event_id}, "
            f"Username: {event.username}, Priority: {event.priority}"
        )

    tickets = [ticket for ticket in tickets if ticket.timestamp != today]
    return tickets

def admin_menu(tickets):
    while True:
        print("\nAdmin Menu:")
        print("1. Display Statistics")
        print("2. Book a Ticket")
        print("3. Display all Tickets")
        print("4. Change Ticket’s Priority")
        print("5. Disable Ticket")
        print("6. Run Events")
        print("7. Exit")
        choice = input("Please enter your choice: ")

        if choice == "1":
            display_Q(tickets)
        elif choice == "2":
            bookTicket(tickets, "admin")
        elif choice == "3":
            View_tickets(tickets)
        elif choice == "4":
            ticket_id = int(input("Enter the ticket ID to change its priority: "))
            changePriority(tickets, ticket_id)
        elif choice == "5":
            ticket_id = int(input("Enter the ticket ID to disable it: "))
            remove_ticket(tickets, ticket_id)
        elif choice == "6":
            tickets = show_events(tickets)
        elif choice == "7":
            print("Exit.")
            break
        else:
            print("Incorrect choice. try again later.")

def user_menu(tickets):
    while True:
        print("\nUser Menu:")
        print("1. Book a Ticket")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_ticket(tickets, "normal_user")
        elif choice == "2":
            print("Saving tickets and exiting...")
            save_tickets(tickets)
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    tickets = find_tickets()
    print("Welcome to the Ticketing System!")

    username = input("Enter your username: ")
    password = input("Enter your password (leave empty for normal user): ")

    if username == "admin" and password == "admin123123":
        admin_menu(tickets)
    else:
        user_menu(tickets)

if __name__ == "__main__":
    from datetime import datetime
    main()
