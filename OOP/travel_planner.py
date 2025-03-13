class Travel:
    def __init__(self, country, month, type):
        self.country = country
        self.month = month
        self.type = type
        self.price = 0


    def trip_info(self):
        if 10 <= self.month <= 3:
            print(f"You are going to {self.country} in the winter! This is a {self.type} trip!")
        elif 3 < self.month < 10:
            print(f"You are going to {self.country} in the summer! This is a {self.type} trip!")
        else:
            print("Invalid input!")





    def calc_cost(self, cost):
        costs = []
        while cost != 0:
           self.price += cost
           costs.append(cost)
           cost = int(input("Enter another cost: "))

        advice = self.advice(self.price)
        inspect = self.list_inspect(costs)
        return advice, inspect


    def advice(self, num):
        if num < 500:
            print("Low budget!")
        elif 500 <= num < 1500:
            print("Take a flight to anywhere...")
        else:
            print("Luxury Trip")



    def list_inspect(self, costs):
        less_than_ten = 0
        for i in costs:
            if i >= 10:
                less_than_ten += 1

        if less_than_ten <= 10:
            self.price += 100
            print(f"Updated price {self.price}")



location = input("Enter a country: ").capitalize()
trip_type = input("Leisure or Business: ").capitalize()
month = input("Enter a month")
test = Travel(location, trip_type, month)


flight_cost = int(input("Enter flight cost: "))
test.calc_cost(flight_cost)




