class App:
    def __init__(self, users, storage, username):
        self.users = users
        self.storage = storage
        self.username = username


    def login(self):
        if self.username == "owner" and self.users >= 1:
            print(f"Welcome {self.username}")
            print(f"Your storage: {self.storage}")
        else:
            print("You are not a user!")


    def check_upgrade(self):
        if self.users >= self.storage:
            upgrade_amt = int(input("Upgrade amount: "))
            self.storage += upgrade_amt
        else:
            print(f"You still have: {self.storage - self.users}")


    def increase_capacity(self, number):
        self.storage += number
        print(f"Updated storage: {self.storage}")



product_one = App(35, 256, "owner")
product_one.login()
product_one.increase_capacity(50)

product_two = App(56, 200, "Anton")
product_two.login()
product_two.increase_capacity(60)
product_two.check_upgrade()