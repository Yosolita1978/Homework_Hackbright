def find_paid_costumer(filename):
    my_file = open(filename)
    melon_cost = 1.00
    for line in my_file:
        line = line.rstrip()
        words = line.split('|')

        username = words[1]
        amount = int(words[2])
        userpaid = float(words[3])
        
        paid_expected = amount * melon_cost


        if paid_expected < userpaid:
            print username, "paid {:.2f}, expected {:.2f}".format(
                userpaid, paid_expected)
        
        elif paid_expected > userpaid:
            print username, "paid {:.2f}, expected {:.2f}".format(
                userpaid, paid_expected)


find_paid_costumer("customer-orders.txt")

