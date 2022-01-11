class User:
    
    bank_name = "First National Dojo"

    def __init__(self , name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received



    def make_withdrawal(self, amount):
        self.account_balance -= amount


    def transfer_money(self, amount, user2):
        self.account_balance -= amount
        user2.account_balance += amount


# this is where class stops


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
phoebe = User("Phoebe Dog", "phoebe@python.com")

print(guido.name)	
print(monty.name)	
print(monty.email)



guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_withdrawal(100)
print(guido.account_balance)

monty.make_deposit(200)
monty.make_deposit(500)
monty.make_withdrawal(12)
monty.make_withdrawal(274)
print(monty.account_balance)

monty.transfer_money(300, guido)
print(guido.account_balance)