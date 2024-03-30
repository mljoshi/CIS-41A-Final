# Joshiro Lawrence, Collin Ong, Duong Luu, Huu Tinh Nguyen
# Group: Study and Pray
# 3-22-2024
# CIS 41A Final Part 1 - De Anza Food Court Menu with objects and classes

# Local modules
from order import Order

if  __name__ == "__main__":
    ordering = True
    while ordering:
        order = Order()
        order.display_menu()
        order.get_inputs()
        print("%.2f" % order.get_total())
        order.print_bill()
        order.save_bill()
        help(order)

        continue_input = input('Continue with another order (No: "N", Yes: Any other key)? ')
        if continue_input.upper() == "N":
            print("Finished")
            ordering = False