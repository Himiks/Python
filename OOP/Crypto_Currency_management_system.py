class Crypto:
    def __init__(self, name):
        self.name = name
        self.price = 0

    def __str__(self):
        return f"This is {self.name} a cryptocurrency"

    def __eq__(self, other):
        if isinstance(other, Crypto):
            return self.name == other.name
        return False

    def __add__(self, other):
        if isinstance(other, Crypto):
            combo = self.name + " " + other.name
            return Crypto(combo)
        else:
            return ValueError("Can not perform addition between them")

    def set_price(self, price):
        self.price += price


    def get_price(self):
        if hasattr(self, "price"):
            return self.price
        else:
            print("Prise is not set")

    def calc_value(self, quantity):
        if hasattr(self, "price"):
            return self.price * quantity
        else:
            print("Price is not set!")


class Bitcoin(Crypto):
    def __init__(self):
        super().__init__("Bitcoin")

    def __str__(self):
        return f"Bitcoin is decentralized!"

    def mine(self):
        return f"Mining the next block"


class Ethereum(Crypto):
    def __init__(self):
        super().__init__("Ethereum")

    def __str__(self):
        return f"Ethereum uses smart contracts!"

    def mine(self):
        return f"Mining tokens..."


crypto1 = Crypto("Solana")
crypto2 = Crypto("Cardano")
crypto3 = Crypto("Bitcoin")

bitcoin = Bitcoin()
ether = Ethereum()

print(crypto1)
print(bitcoin == crypto3)

print(ether + crypto2)

ether.set_price(1750)
print(ether.get_price())

