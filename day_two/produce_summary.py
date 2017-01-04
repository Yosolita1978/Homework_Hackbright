def print_report(filename):
    my_file = open(filename)
    for line in my_file:
        line = line.rstrip()
        words = line.split('|')
        melon = words[0]
        count = words[1]
        amount = words[2]
        print "Delivered {} {}s for total of ${}".format(
            count, melon, amount)
    
    my_file.close()
    
    

print "Day 1"
print_report("um-deliveries-20140519.txt")

print "Day 2"
print_report("um-deliveries-20140520.txt")

print "Day 3"
print_report("um-deliveries-20140521.txt")


