class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def remove_cash(self, amount):
        self.wallet -= amount

    def cheer(self):
        return "Woo!"