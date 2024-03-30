class Person:
    """
    Person class
    Class with abstract methods
    """
    def __init__(self):
        pass
    def get_tax_rate(self):
        """
        Abstract method for tax rate
        """
        raise NotImplementedError
    def get_type(self):
        """Abstract method for type of Person"""
        raise NotImplementedError