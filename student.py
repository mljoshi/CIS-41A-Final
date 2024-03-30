# Local modules
from person import Person

STUDENT_TAX_RATE = 0.00

class Student(Person):
    """
    Student class

    Contains data on the type of Person it is (a student) and the tax rate for this type of Person
    """
    def __init__(self):
        """
        Constructor for Student class
        Parameters: self (Student) - Current Student object
        Returns: Nothing
        """
        super().__init__()
        self._tax_rate = STUDENT_TAX_RATE

    def get_tax_rate(self):
        """
        This method returns the tax rate for a Student
        Parameters: self (Student) - Current Student object
        Returns: Tax rate for students (float)
        """
        return self._tax_rate
    
    def get_type(self):
        """
        This method returns the type of Person it is
        Parameters: self (Student) - Current Student object
        Returns: Type of Person (string)
        """
        return "Student"