import unittest

# Local modules
from order import Order
from student import Student
from staff import Staff

class TestOrder(unittest.TestCase):
    
    # Unit tests
    def test_start(self):
        """
        Test the constructor
        """
        curr_order = Order()
        self.assertIsNone(curr_order._person, "Person not None")
        self.assertFalse(curr_order._has_ordered, "Has ordered already")
        self.assertFalse(curr_order._has_ordered, ">0 quantity already")
        self.assertAlmostEqual(curr_order._get_subtotal(), 0.00, "Subtotal not 0")
        self.assertAlmostEqual(curr_order._get_tax(), 0.00, "Tax not 0")
        self.assertAlmostEqual(curr_order.get_total(), 0.00, "Total not 0")
        self.assertEqual(curr_order._items["De Anza Burger"], 0, "De Anza Burger qty not 0")
        self.assertEqual(curr_order._items["Bacon Cheese"], 0, "Bacon Cheese qty not 0")
        self.assertEqual(curr_order._items["Mushroom Swiss"], 0, "Mushroom Swiss not 0")
        self.assertEqual(curr_order._items["Western Burger"], 0, "Western Burger not 0")
        self.assertEqual(curr_order._items["Don Cali Burger"], 0, "Don Cali Burger not 0")
    
    def test_quantities(self):
        """
        Test _update_item method
        """
        curr_order = Order()
        curr_order._update_item("De Anza Burger", 745)
        curr_order._update_item("Bacon Cheese", 5)
        curr_order._update_item("Mushroom Swiss", 146)
        curr_order._update_item("Western Burger", 0)
        curr_order._update_item("Don Cali Burger", 19996)
        curr_order._update_item("De Anza Burger", -325)
        
        self.assertEqual(curr_order._items["De Anza Burger"], 745-325, "De Anza Burger qty off")
        self.assertEqual(curr_order._items["Bacon Cheese"], 5, "Bacon Cheese qty off")
        self.assertEqual(curr_order._items["Mushroom Swiss"], 146, "Mushroom Swiss qty off")
        self.assertEqual(curr_order._items["Western Burger"], 0, "Western Burger qty off")
        self.assertEqual(curr_order._items["Don Cali Burger"], 19996, "Don Cali Burger qty off")
    
    def test_subtotal(self):
        """
        Test _get_subtotal method
        """
        curr_order = Order()
        curr_order._update_item("De Anza Burger", 4)
        curr_order._update_item("Mushroom Swiss", 74)
        expected_subtotal = 4 * 5.25 + 74 * 5.95
        self.assertAlmostEqual(curr_order._get_subtotal(), expected_subtotal, msg="Subtotal incorrect")


    # Integration tests (testing if Person subclasses are operating well with Order class)
    def test_complete_order(self):
        """
        Test a complete order
        """
        curr_order = Order()
        curr_order._update_item("De Anza Burger", 4)
        curr_order._update_item("Bacon Cheese", 1)
        curr_order._update_item("De Anza Burger", -1)
        orderer = Staff()
        curr_order._person = orderer
        expected_subtotal = 3 * 5.25 + 1 * 5.75
        expected_tax = expected_subtotal * 0.09
        expected_total = expected_tax + expected_subtotal
        self.assertAlmostEqual(curr_order._get_subtotal(), expected_subtotal, msg="Subtotal incorrect")
        self.assertAlmostEqual(curr_order._get_tax(), expected_tax, msg="Tax incorrect")
        self.assertAlmostEqual(curr_order.get_total(), expected_total, msg="Total incorrect")
    
    def test_staff_tax(self):
        """
        Test staff tax & rate
        """
        curr_order = Order()
        orderer = Staff()
        curr_order._person = orderer
        curr_order._update_item("De Anza Burger", 7)
        expected_tax_rate = 0.09
        expected_tax = 7 * 5.25 * expected_tax_rate
        self.assertAlmostEqual(curr_order._person.get_tax_rate(), expected_tax_rate, msg="Staff tax rate incorrect")
        self.assertAlmostEqual(curr_order._get_tax(), expected_tax, msg="Staff tax incorrect")
    
    def test_student_tax(self):
        """
        Test student tax & rate
        """
        curr_order = Order()
        orderer = Student()
        curr_order._person = orderer
        curr_order._update_item("De Anza Burger", 7)
        expected_tax_rate = 0.00
        expected_tax = 0.00
        self.assertAlmostEqual(curr_order._person.get_tax_rate(), expected_tax_rate, msg="Student tax rate incorrect")
        self.assertAlmostEqual(curr_order._get_tax(), expected_tax, msg="Student tax incorrect")


if __name__ == "__main__":
    unittest.main()