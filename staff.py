# Local modules
from person import Person

STAFF_TAX_RATE = 0.09

class Staff(Person):
    """
    Staff class

    Contains data on the type of Person it is (a staff member) and the tax rate for this type of Person
    """
    def __init__(self):
        """
        Constructor for Staff class
        Parameters: self (Staff) - Current Staff object
        Returns: Nothing
        """
        super().__init__()
        self._tax_rate = STAFF_TAX_RATE

    def get_tax_rate(self):
        """
        This method returns the tax rate for a Staff
        Parameters: self (Staff) - Current Staff object
        Returns: Tax rate for staff (float)
        """
        return self._tax_rate
    
    def get_type(self):
        """
        This method returns the type of Person it is
        Parameters: self (Staff) - Current Staff object
        Returns: Type of Person (string)
        """
        return "Staff member"