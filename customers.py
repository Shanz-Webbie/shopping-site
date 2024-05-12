"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self,first_name, last_name, email_address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password

    def __repr__(self):
        return