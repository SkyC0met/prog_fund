import os

quantity = 0
failed = 0
transaction_history = []
current_order_id = 1000

class QuitError(Exception):
  pass

def smart_input(user_input):
  isquit = input(user_input)
  if isquit.lower() == 'quit':
    raise QuitError
  return isquit

def load_inventory():
  global quantity_total, transaction_history, current_order_id

  print('Current orders:\n')
  try:
    with open('orders.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
            parts = line.strip().split(',')
            if len(parts) == 3:
                order_id = int(parts[0].strip())
                qty = int(parts[2].strip())
                
                transaction_history.append(qty)
                quantity_total += qty
                current_order_id = order_id
  except FileNotFoundError:
    pass
  print("\n")

def get_valid_input():
  global failed

  while True:
    print('Enter "Quit" to exit')

    try:
      prod_name = smart_input('Enter Product Name: ')
      quantity = smart_input('Enter Quantity: ')
    except QuitError:
      return 'quit'

    failed += 1
    
    try:
      quantity = int(quantity)
      if quantity >= 0:
        failed -= 1
        return prod_name, quantity
      else:
        print('No negative numbers')
    except ValueError:
      print('Please enter a number')

def process_delivery(prod_name, quantity):
  try:
    with open('orders.txt', 'a') as f:
      order_num = 1000
      f.write(f'1001, {prod_name}, {quantity}\n')
  except FileNotFoundError:
    open('orders.txt', 'x')

def calculate_tax(amount):
  return amount * 0.1

def generate_report(total_units, tax, failed_attempts):
  print(f'Total Units Processed: {total_units}')
  print(f'Total Tax: {tax}')
  print(f'Number of Failed/Rejected Entries: {failed_attempts}')

def main():
  global quantity

  while quantity < 500:
    user_input = get_valid_input()
    if user_input == 'quit':
      tax = calculate_tax(quantity)
      generate_report(quantity, tax, failed)
      break
    else:
      prod_name, quantity = user_input
      process_delivery(quantity, user_input)
  else:
    print('ALERT YOU HAVE EXCEEDED 500 UNITS')

main()