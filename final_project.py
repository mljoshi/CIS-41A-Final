# Joshiro Lawrence, Collin Ong, Duong Luu, Huu Tinh Nguyen
# Group: Study and Pray
# 3-22-2024
# CIS 41A Final Part 1 - De Anza Food Court Menu with objects and classes

# Local modules
from order import Order

def main():
    """
    Main function

    No parameters

    Returns nothing
    """
    order = Order()
    order.display_menu()
    order.get_inputs()
    order.print_bill()
    order.save_bill()

    return

# If run as the main program
if __name__ == "__main__":
    main()

"""
Tests
1
Menu
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
6. Exit/end
7. Delete item
8. Print current cart
Enter the burger number you would like to add or update in your order: 1
What quantity of these would you like? (+ to add, - to remove)? 4
Added 4 of #1 De Anza Burger
Enter the burger number you would like to add or update in your order: 2
What quantity of these would you like? (+ to add, - to remove)? 1
Added 1 of #2 Bacon Cheese
Enter the burger number you would like to add or update in your order: 1
What quantity of these would you like? (+ to add, - to remove)? -1
Removed 1 of #1 De Anza Burger
Enter the burger number you would like to add or update in your order: 6
Are you a student (Y/N)? N
-------------------------------
Bill
3 De Anza Burger's ($5.25 each): $15.75
1 Bacon Cheese: $5.75
-------------------------------
Subtotal: $21.50
Tax rate for a staff member: 9%
Tax: $1.93
-------------------------------
Total: $23.43

2
Menu
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
6. Exit
7. Delete item
8. Print current cart
Enter the burger number you would like to add or update in your order: -6
Error, please enter a number between 1 and 8
Enter the burger number you would like to add or update in your order: 0
Error, please enter a number between 1 and 8
Enter the burger number you would like to add or update in your order: ab
Error, please enter a whole number
Enter the burger number you would like to add or update in your order: 2
What quantity of these would you like? (+ to add, - to remove)? -1
Error, resultant quantity is negative
Current quantity ordered of #2 Bacon Cheese: 0
What quantity of these would you like? (+ to add, - to remove)? 1.0
Error, please enter a whole number
What quantity of these would you like? (+ to add, - to remove)? a
Error, please enter a whole number
What quantity of these would you like? (+ to add, - to remove)? 1
Added 1 of #2 Bacon Cheese
Enter the burger number you would like to add or update in your order: 3.
Error, please enter a whole number
Enter the burger number you would like to add or update in your order: 3
What quantity of these would you like? (+ to add, - to remove)? 5
Added 5 of #3 Mushroom Swiss
Enter the burger number you would like to add or update in your order: 7
Enter the burger number you would like to remove: 0 
Error, please enter a number between 1 and 6
Enter the burger number you would like to remove: 7
Error, please enter a number between 1 and 6
Enter the burger number you would like to remove: -1
Error, please enter a number between 1 and 6
Enter the burger number you would like to remove: 1.
Error, please enter a whole number
Enter the burger number you would like to remove: a
Error, please enter a whole number
Enter the burger number you would like to remove: 6
Deleted nothing
Enter the burger number you would like to add or update in your order: 8
Current cart:
#2 Bacon Cheese quantity: 1
#3 Mushroom Swiss quantity: 5
Enter the burger number you would like to add or update in your order: 8.
Error, please enter a whole number
Enter the burger number you would like to add or update in your order: 7
Enter the burger number you would like to remove: 2
Deleted #2 Bacon Cheese from order
Enter the burger number you would like to add or update in your order: 8
Current cart:
#3 Mushroom Swiss quantity: 5
Enter the burger number you would like to add or update in your order: 3
What quantity of these would you like? (+ to add, - to remove)? 1
Added 1 of #3 Mushroom Swiss
Enter the burger number you would like to add or update in your order: 4
What quantity of these would you like? (+ to add, - to remove)? 2
Added 2 of #4 Western Burger
Enter the burger number you would like to add or update in your order: 8
Current cart:
#3 Mushroom Swiss quantity: 6
#4 Western Burger quantity: 2
Enter the burger number you would like to add or update in your order: 6
Are you a student (Y/N)? aba
Error, please enter "Y" or "N"
Are you a student (Y/N)? y
-------------------------------
Bill
6 Mushroom Swiss's ($5.95 each): $35.70
2 Western Burger's ($5.95 each): $11.90
-------------------------------
Subtotal: $47.60
Tax rate for a student: 0%
Tax: $0.00
-------------------------------
Total: $47.60
______________________________________________
Test outputs complete
help(order) shows this
Help on Order in module order object:

class Order(builtins.object)
 |  Order class
 |
 |  Contains data such as what is on the menu, the costs, etc
 |  Functionalities include adding a number of items to the order based on input and calculating the total cost of the order and printing the bill
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Constructor for the Order class
 |      Parameters: self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc
 |      Returns: Nothing
 |
 |  display_menu(self)
 |      This method displays the menu
 |
 |      Parameters: self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc
 |
 |      Returns: Nothing
 |
 |  get_inputs(self)
 |      This method takes in as input the types of burgers the user wants to order and how many of them,
 |      verifying input along the way.
 |
 |      Parameters: self (Order): Object containing order data such as quantities, type of person ordering (student/staff), etc
 |
 |      Returns: Nothing
 |
 |  get_total(self)
 |      This helper method gets the total
 |
 |      Parameters: self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc
 |
 |      Returns: total (float) - Total cost of the order based on the subtotal and the tax
 |
 |  print_bill(self)
 |      This method prints the bill of the order to the screen
 |
 |      Parameters: self (Order): Object containing order data such as quantities, type of person ordering (student/staff), etc
 |
 |      Returns: Nothing
 |
 |  save_bill(self)
 |      This method saves the bill of the order to a file whose name is decided by the time and date
 |
 |      Parameters: self (Order): Object containing order data such as quantities, type of person ordering (student/staff), etc
 |
 |      Returns: Nothing (writes to file)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

"""