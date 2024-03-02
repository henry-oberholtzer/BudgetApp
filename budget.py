class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self) -> str:
    to_string = '{:*^30}\n'.format(self.name)
    for entry in self.ledger:
      amount_str = f' {format(entry["amount"], '.2f')}'
      desc_str = '{:<30}'.format(entry["description"])
      trim_index = 30 - len(amount_str)
      to_string += f'{desc_str[:trim_index]}{amount_str}\n'
    to_string += f'Total: {self._get_balance ()}'
    return to_string
  
  def _deposit(self, amount, description):
    self.ledger.append({"amount": amount, "description": description})
  
  def deposit(self, amount, description=""):
    return self._deposit(amount, description)

  def _withdraw(self, amount, description=""):
    if self._check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False
  
  def withdraw(self, amount, description=""):
    return self._withdraw(amount, description)
  
  def _get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance += entry["amount"]
    return balance

  def get_balance(self):
    return self._get_balance()
  
  def _check_funds(self, amount):
    if amount <= self._get_balance():
      return True
    return False

  def check_funds(self, amount):
    return self._check_funds(amount)
  
  def transfer(self, amount, category):
    if self._check_funds(amount):
      self._withdraw(amount, f'Transfer to {category.name}')
      category.deposit(amount, f'Transfer from {self.name}')
      return True
    return False


def create_spend_chart(categories):
  pass
