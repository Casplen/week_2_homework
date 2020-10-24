class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def remove_cash(self, amount):
        self.wallet -= amount