"""Randomly pick customer and print customer info"""

# Add code starting here
# Hint: remember to import any functions you need from
    # other files or libraries

from random import choice
from melon_customer_raffle import Customer, organize_customer_data

def pick_winner(filepath):
    """ This function will take a costumers list and will return a random winner """

    costumers = organize_customer_data(filepath)
    winner_customer = choice(costumers)

    return "Contact {name} at {email} to notify them they've won".format(
        name=winner_customer.name,
        email=winner_customer.email
        )

def main():
    pick_winner("customers.txt")


if __name__ == '__main__':

    
    

    main()





