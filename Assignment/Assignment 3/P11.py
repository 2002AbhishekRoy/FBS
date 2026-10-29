print("This Program Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition.")

ticket = int(input("Enter the ticket per person : "))

a = [45, 65, 26, 8, 20]

for i in a :
    if i > 59:
        discount = (50/100) * ticket
        net_ticket = ticket - discount
        print("Ticket : ", ticket)
        print("Discount : ", discount)
        print("Net Ticket : ", net_ticket)

    elif i < 12:
        discount = (30/100) * ticket
        net_ticket = ticket - discount
        print("Ticket : ", ticket)
        print("Discount : ", discount)
        print("Net Ticket : ", net_ticket)

    else:
        net_ticket = ticket
        print("Net Ticket : ", net_ticket)


    print()


