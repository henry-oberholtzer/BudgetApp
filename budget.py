class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self) -> str:
    to_string = '{:*^30}\n'.format(self.name)
    for entry in self.ledger:
      amount = entry["amount"]
      amount_str = f" {amount:.2f}"
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
    return sum([entry["amount"] for entry in self.ledger])
  
  def _get_expenses(self):
    return sum([entry["amount"] for entry in self.ledger if entry["amount"] < 0])
  
  def get_expenses(self):
    return self._get_expenses()

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
  spend_chart = "Percentage spent by category\n"
  total_spent = sum([category.get_expenses() for category in categories])
  percentage_strs = {
    100: '100|',
    90: ' 90|',
    80: ' 80|',
    70: ' 70|',
    60: ' 60|',
    50: ' 50|',
    40: ' 40|',
    30: ' 30|',
    20: ' 20|',
    10: ' 10|',
    0:  '  0|'}
  for category in categories:
    percent = round((category.get_expenses() / total_spent) * 100)
    for percent_str in percentage_strs:
      if percent_str == 0:
        percentage_strs[percent_str] += ' o '
      elif percent >= percent_str:
        percentage_strs[percent_str] += ' o '
      else:
        percentage_strs[percent_str] += '   '
  # get percentages
  spend_chart += ' \n'.join(percentage for percentage in percentage_strs.values()) + ' \n'
  # add dashes
  spend_chart += '    ' + '---'*len(categories) + '-\n'
  # add labels
  name_list = list(cat.name for cat in categories)
  name_iterations = len(max(name_list, key = len))
  for char_index in range(name_iterations):
    spend_chart += '    '
    for name in name_list:
      if char_index < len(name):
        spend_chart += f' {name[char_index]} '
      else:
        spend_chart += '   '
    spend_chart += ' \n'
  return spend_chart.strip('\n')
