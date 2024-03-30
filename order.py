import time
import datetime

# Local modules
from student import Student
from staff import Staff

class Order:
    """
    Order class

    Contains data such as what is on the menu, the costs, etc
    Functionalities include adding a number of items to the order based on input and calculating the total cost of the order and printing the bill
    """
    def __init__(self):
        """
        Constructor for the Order class
        Parameters: self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc
        Returns: Nothing
        """
        self._person = None
        self._items = {"De Anza Burger": 0, "Bacon Cheese": 0, "Mushroom Swiss": 0, "Western Burger": 0, "Don Cali Burger": 0}
        self._has_ordered = False
        self._item_numbers = {1: "De Anza Burger", 2: "Bacon Cheese", 3: "Mushroom Swiss", 4: "Western Burger", 5: "Don Cali Burger"}
        self._price_dict = {"De Anza Burger" : 5.25 , "Bacon Cheese" : 5.75, "Mushroom Swiss" : 5.95, "Western Burger" : 5.95, "Don Cali Burger" : 5.95}
    
    def _check_has_ordered(self):
        """
        This helper method checks if the user has ordered anything (if any quantity is greater than 0)

        Parameters:
        self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc

        Returns: has_ordered (bool) - whether or not the person has ordered anything thus far
        
        """
        has_ordered = False
        for quantity in self._items.values():
            if quantity > 0:
                has_ordered = True
        return has_ordered
    
    def _update_item(self, item, quantity):
        """
        This helper method updates the item and its quantity to the order, or adds it

        Parameters:
        self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc
        item (string) - Name of the corresponding burger
        quantity (int) - Number of those burgers being ordered (or removed from cart)

        Returns: Nothing
        """
        self._items[item] += quantity

    def _delete_item(self, item):
        """
        This helper method deletes an item from the order (sets quantity to 0)

        Parameters:
        self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc
        item (string) - Name of the corresponding burger

        Returns: Nothing
        """
        self._items[item] = 0
    
    def _print_cart(self):
        """
        This helper method prints the current order and quantities

        Parameters:
        self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc
        
        Returns: Nothing
        """
        print("Current cart:")
        empty_cart = True
        for (number, burger) in self._item_numbers.items():
            quantity = self._items[burger]
            if quantity > 0:
                print("#%d %s quantity: %d" % (number, burger, quantity))
                empty_cart = False
        if empty_cart:
            print("Empty")

    def _get_individual_burger_total(self, burger, quantity):
        """
        This helper method gets the individual cost of a quantity of burgers knowing its number

        Parameters:
        self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc
        burger (int) - Number of the corresponding burger number
        quantity (int) - Number of those burgers being ordered

        Returns:
        individual_total (float) - Total cost of the quantity of burgers with burger number burger
        """
        individual_total = self._price_dict[burger] * quantity
        return individual_total
    
    def _get_subtotal(self):
        """
        This helper method gets the subtotal
        
        Parameters: self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc

        Returns: subtotal (float) - Subtotal cost of the order based on the quantities and prices of the items ordered
        """
        subtotal = 0
        for (burger, quantity) in self._items.items():
            subtotal += self._get_individual_burger_total(burger, quantity)
        return subtotal
    
    def _get_tax(self):
        """
        This helper method gets the tax amount
        
        Parameters: self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc

        Returns: tax (float) - Total tax of the order based on the subtotal
        """
        # self._person must be set or an error will occur
        if not self._check_has_ordered():
            return 0
        tax = self._person.get_tax_rate() * self._get_subtotal()
        return tax

    def get_total(self):
        """
        This helper method gets the total
        
        Parameters: self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc

        Returns: total (float) - Total cost of the order based on the subtotal and the tax
        """
        total = self._get_subtotal() + self._get_tax()
        return total
    
    def display_menu(self):
        """
        This method displays the menu
        
        Parameters: self (Order) - Object containing order data such as quantities, type of person ordering (student/staff), etc

        Returns: Nothing
        """
        print("Menu")
        for (burger_number, burger) in self._item_numbers.items():
            print("%d. %s - $%.2f" % (burger_number, burger, self._price_dict[burger])) # Will appear as something like: 1. De Anza Burger - $5.25
            # As of Python version 3.7, dictionaries are ordered, so I will not need to worry about this displaying the menu in an ugly order (though it would still be equally functional)
        print("6. Exit")
        print("7. Delete item")
        print("8. Print current cart")
    
    def get_inputs(self):
        """
        This method takes in as input the types of burgers the user wants to order and how many of them,
        verifying input along the way.
        
        Parameters: self (Order): Object containing order data such as quantities, type of person ordering (student/staff), etc

        Returns: Nothing
        """
        order_number_input = 0

        # Sentinel value is 6
        while(order_number_input != 6):
            invalid_order_input = True
            while(invalid_order_input):
                try:
                    order_number_input = int(input("Enter the burger number you would like to add or update in your order: "))
                    if ((order_number_input >= 1) and (order_number_input <= 8)):
                        invalid_order_input = False
                    else:
                        print("Error, please enter a number between 1 and 8")
                except ValueError:
                    print("Error, please enter a whole number")
            # Order input is validated by this point
            if (order_number_input < 6):
                invalid_quantity_input = True
                while(invalid_quantity_input):
                    try:
                        quantity_input = int(input("What quantity of these would you like? (+ to add, - to remove)? "))
                        if (self._items[self._item_numbers[order_number_input]] + quantity_input >= 0):
                            invalid_quantity_input = False
                            self._update_item(self._item_numbers[order_number_input], quantity_input)
                            if (quantity_input > 0):
                                print("Added %d of #%d %s" % (quantity_input, order_number_input, self._item_numbers[order_number_input]))
                            elif (quantity_input < 0):
                                print("Removed %d of #%d %s" % (-quantity_input, order_number_input, self._item_numbers[order_number_input]))
                            else:
                                print("Changed nothing")
                        else:
                            print("Error, resultant quantity is negative")
                            print("Current quantity ordered of #%d %s: %d" %(order_number_input, self._item_numbers[order_number_input], self._items[self._item_numbers[order_number_input]]))
                    except ValueError:
                        print("Error, please enter a whole number")
            elif (order_number_input == 7):
                invalid_deletion_input = True
                while(invalid_deletion_input):
                    try:
                        deletion_number_input = int(input("Enter the burger number you would like to remove: "))
                        if ((deletion_number_input >= 1) and (deletion_number_input <= 6)):
                            invalid_deletion_input = False
                        else:
                            print("Error, please enter a number between 1 and 6")
                    except ValueError:
                        print("Error, please enter a whole number")
                if (deletion_number_input != 6):
                    self._delete_item(self._item_numbers[deletion_number_input])
                    print("Deleted #%d %s from order" % (deletion_number_input, self._item_numbers[deletion_number_input]))
                else:
                    print("Deleted nothing")
            elif (order_number_input == 8):
                self._print_cart()
        # End of input loop, user has entered 6
        if (self._check_has_ordered()): # If the order number input is 6 but they have ordered something, ask them if they are a student to determine tax rate
            invalid_student_input = True
            while(invalid_student_input):
                is_student_input = input("Are you a student (Y/N)? ")
                if (is_student_input.lower().strip() == "y"):
                    orderer = Student()
                    self._person = orderer
                    invalid_student_input = False
                elif (is_student_input.lower().strip() == "n"):
                    orderer = Staff()
                    self._person = orderer
                    invalid_student_input = False
                else:
                    print('Error, please enter "Y" or "N"')
        else: # In the case that the user does not order anything
            print("Thank you, hope to see you again!")
        

    def print_bill(self):
        """
        This method prints the bill of the order to the screen

        Parameters: self (Order): Object containing order data such as quantities, type of person ordering (student/staff), etc

        Returns: Nothing
        """
        # If they haven't ordered, don't print anything
        if (not self._check_has_ordered()):
            return
        print("-------------------------------")
        print("Bill")
        # Print total of each item ordered
        for (burger, quantity) in self._items.items():
            if quantity > 0: # Don't print anything for items that were not ordered
                if quantity == 1: # Singular case
                    print("1 %s: $%.2f" % (burger, self._get_individual_burger_total(burger, quantity)))
                else: # Plural case
                    print("%d %s's ($%.2f each): $%.2f" % (quantity, burger, self._price_dict[burger], self._get_individual_burger_total(burger, quantity)))
        print("-------------------------------")
        print("Subtotal: $%.2f" % self._get_subtotal())
        print("Tax rate for a %s: %d%%" % (self._person.get_type().lower(), int(100 * self._person.get_tax_rate()))) # Convert float to percent
        print("Tax: $%.2f" % self._get_tax())
        print("-------------------------------")
        print("Total: $%.2f" % self.get_total())
    
    def _get_file_name(self):
        """
        This method picks the file name to be used when saving the order based on the current time and date
        
        Parameters: self (Order): Object containing order data such as quantities, type of person ordering (student/staff), etc

        Returns: file_name (string) - the file name to be used when saving the order
        """
        time_stamp = time.time()
        order_time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H-%M-%S')
        file_name = order_time_stamp + ".txt"
        return file_name
    
    def save_bill(self):
        """
        This method saves the bill of the order to a file whose name is decided by the time and date

        Parameters: self (Order): Object containing order data such as quantities, type of person ordering (student/staff), etc

        Returns: Nothing (writes to file)
        """
        # If they haven't ordered, don't save anything
        if (not self._check_has_ordered()):
            return
        with open(self._get_file_name(), "w") as outfile: 
            print("-------------------------------", file = outfile)
            print("Bill", file = outfile)
            # Print total of each item ordered
            for (burger, quantity) in self._items.items():
                if quantity > 0: # Don't print anything for items that were not ordered
                    if quantity == 1: # Singular case
                        print("1 %s: $%.2f" % (burger, self._get_individual_burger_total(burger, quantity)), file = outfile)
                    else: # Plural case
                        print("%d %s's ($%.2f each): $%.2f" % (quantity, burger, self._price_dict[burger], self._get_individual_burger_total(burger, quantity)), file = outfile)
            print("-------------------------------", file = outfile)
            print("Subtotal: $%.2f" % self._get_subtotal(), file = outfile)
            print("Tax rate for a %s: %d%%" % (self._person.get_type().lower(), int(100 * self._person.get_tax_rate())), file = outfile) # Convert float to percent
            print("Tax: $%.2f" % self._get_tax(), file = outfile)
            print("-------------------------------", file = outfile)
            print("Total: $%.2f" % self.get_total(), file = outfile)