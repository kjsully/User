class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        
    def display_user_balance(self):
        print(f"User:{self.name},Balance:{self.account_balance}")





guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
kyle = User('Kyle Sullivan', 'kyle@python.com')

guido.make_deposit(200)
guido.make_deposit(200)
guido.make_deposit(200)
guido.make_withdrawal(100)
guido.display_user_balance()

monty.make_deposit(200)
monty.make_deposit(200)
monty.make_withdrawal(100)
monty.make_withdrawal(100)
monty.display_user_balance()

kyle.make_deposit(100000)
kyle.make_withdrawal(100)
kyle.make_withdrawal(100)
kyle.make_withdrawal(100)
kyle.display_user_balance()





