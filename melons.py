"""This file should have our order classes in it."""

import random 

class AbstractMelonOrder(object):
    """ Docstring here """

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
                
    def get_total(self):
        """Calculate price."""

        # ???? huh? AbstractMelonOrder.get_base_price()    

        if self.species == "Christmas melons":
            base_price = 7.5   

        total = (1 + self.tax) * self.qty * base_price
        return total

    def get_base_price(self):

        base_price = random.randint(5, 9)
        return base_price

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    tax = 0.08
    order_type = "domestic"

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes"""

    #   super(DomesticMelonOrder, self).__init__(species, qty)
       


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty) 
        self.country_code = country_code
        
        
   
    def get_total(self):
        """Calculate price."""

        flat_fee = 3    

        total =  super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += flat_fee

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder): 
    """Government melon orders"""

    passed_inspection = False
    tax = 0

    def inspect_melons(self): 

        self.passed_inspection = True