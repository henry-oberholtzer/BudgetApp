class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description=""):
    self.ledger.append({"amount": -amount, "description": description})

  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance += entry["amount"]
    return balance

  def transfer(self, amount, category):
    pass

  def check_funds(self, amount):
    pass

  





def create_spend_chart(categories):
  pass
