def get_order_tallies(filename):
    """Return tally of melons by type."""


    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
    filename_data = open(filename)
    for file in filename_data:
        line = file.split("|")
        melon_type = line[1]
        melon_count = int(line[2])
        melon_tallies[melon_type] = melon_tallies[melon_type] + melon_count

    filename_data.close()
    return melon_tallies

def get_revenue_sales(melon_tallies):
    """Return total revenue in sales."""
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0

    print "REVENUE SALES REPORT"


    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue = total_revenue + revenue


        print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)

    return total_revenue


def sales_comparison(orders_file):
    """Compare online and salesperson-generated sales."""

    sales_person_index = 0
    internet_index = 0
    orders = open(orders_file)
    
    

    for file in orders:

        line = file.split("|")

        if line[2] == "ONLINE":
            internet_index = internet_index + float(line[3])
        else:
            sales_person_index = sales_person_index + float(line[3])

    print "SALES DATA"
    print "Salespeople generated ${:,.2f} in revenue.".format(sales_person_index)
    print "Internet sales generated ${:,.2f} in revenue.".format(internet_index)

    if sales_person_index > internet_index:
        print "Guess there's some value to those sales people after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

def main():
    # Get the tallies by melon type
    melon_tallies = get_order_tallies("orders-by-type.txt")

    # Print total revenue report

    get_revenue_sales(melon_tallies)

    print

    # Print online-v-salesperson report
    sales_comparison("orders-with-sales.txt")

if __name__ == '__main__':
    main()