import os

quantity_tt = 0
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

def load_inv():
  global quantity_tt, transaction_history, current_order_id

  print('Current orders:')
  try:
    with open('orders.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
            parts = line.strip().split(',')
            if len(parts) == 3:
                order_id = int(parts[0].strip())
                quantity = int(parts[2].strip())
                
                transaction_history.append(quantity)
                quantity_tt += quantity
                current_order_id = order_id
  except FileNotFoundError:
    pass

def save_inv(total, history):
  with open('inv.txt', 'w') as file:
    file.write(f'Final quantity: {total}\n')
    file.write(f'Transaction history: {history}\n')

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
  global current_order_id
  current_order_id += 1
  try:
    with open('orders.txt', 'a') as file:
      file.write(f'{current_order_id}, {prod_name}, {quantity}\n')
  except FileNotFoundError:
    with open('orders.txt', 'w') as file:
      file.write(f'{current_order_id}, {prod_name}, {quantity}\n')

  print(f'New order added: \n{current_order_id}, {prod_name}, {quantity}')
  print('Order successfully saved to orders.txt')

def calculate_tax(amount):
  return amount * 0.1

def generate_report(total_units, tax, failed_attempts):
  print(f'Total Units Processed: {total_units}')
  print(f'Total Tax: {tax}')
  print(f'Number of Failed/Rejected Entries: {failed_attempts}')

def main():
  global quantity_tt, transaction_history

  load_inv()

  while quantity_tt < 500:
    user_input = get_valid_input()
    if user_input == 'quit':
      tax = calculate_tax(quantity_tt)
      generate_report(quantity_tt, tax, failed)
      save_inv(quantity_tt, transaction_history)
      break
    else:
      prod_name, quantity = user_input
      transaction_history.append(quantity)
      quantity_tt += quantity
      process_delivery(prod_name, quantity)
  else:
    print('ALERT YOU HAVE EXCEEDED 500 UNITS')

main()