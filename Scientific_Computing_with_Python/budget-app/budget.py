import math

class Category:
  
  def __init__(self, cat):
    self.category = cat
    self.ledger = list()
  
  def deposit(self, amount, description=''):
    object = {'amount': amount, 'description': description}
    self.ledger.append(object)

  def check_funds(self, amount):
    if self.ledger[0]['amount'] - amount >= 0:
      return True
    else:
      return False
    
  def withdraw(self, amount, description=''):
    object = {'amount': (-1)*amount, 'description': description}
    if self.check_funds(amount):
      self.ledger.append(object)
      return True
    else:
      return False
      
  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i['amount']
    return balance

  def transfer(self, amount, cat):
    if self.check_funds(amount):
      self.withdraw(amount, 'Transfer to ' + cat.category)
      cat.deposit(amount, 'Transfer from ' + self.category)
      return True
    else:
      return False

  def __str__(self):
    lenght = 30
    result = '{:*^{}}\n'.format(self.category, lenght)
    for i in self.ledger:
      lenght = 30
      if len(i['description']) > 23:
        lenght -= 23
      else:
        lenght -= len(i['description'])
      result += '{:.23}{:>{}.2f}\n'.format(i['description'], float(i['amount']), lenght)
    result += 'Total: {}'.format(self.get_balance())
    return result

    
def create_spend_chart(categories):
  result = 'Percentage spent by category\n'
  categories_total_withdraw = list()
  categories_percent = list()
  for i in categories:
    total = 0
    for j in i.ledger:
      if j['amount'] < 0:
        total += j['amount']
    categories_total_withdraw.append((-1)*total)
  for c in categories_total_withdraw:
    percent = c*100/sum(categories_total_withdraw)
    categories_percent.append(math.floor(percent/10)*10)
  for i in range(100, -10, -10):
    result += '{:>3}|'.format(i)
    for percent in categories_percent:
      if percent >= i:
        result += ' o '
      else:
        result += ' '*3
    result += ' \n'
  result += ' '*4 +'-'*10 + '\n'
  name_categ = [cat.category for cat in categories]
  for i in range(max([len(i) for i in name_categ])):
    result += ' '*4
    for name in name_categ:
      if i < len(name):
        result += ' {} '.format(name[i])
      else:
        result += ' '*3
    if i != max([len(i) for i in name_categ]) - 1:
      result += ' \n'
    else:
      result += ' '
  return result
