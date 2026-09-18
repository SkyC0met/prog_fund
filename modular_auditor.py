inventory = 0
new_value = 0
failed = 0

def get_valid_input():
  global failed

  while True:
    user_input = input('Enter "Quit" to exit \nEnter stock quantity: ')
    if user_input.lower() == 'quit':
      return 'quit'

    failed += 1
    
    try:
      new_value = int(user_input)
      if new_value >= 0:
        failed -= 1
        return new_value
      else:
        print('No negative numbers')
    except ValueError:
      print('Please enter a number')

def process_delivery(current_total, new_value):
  current_total += int(new_value)
  return current_total

def calculate_tax(amount):
  pass

def generate_report(total_units, failed_attempts):
  print(f'Total Units Processed: {total_units}')
  print(f'Number of Failed/Rejected Entries: {failed_attempts}')

while inventory < 500:
  user_input = get_valid_input()
  if user_input == 'quit':
    generate_report(inventory, failed)
    break
  else:
    inventory = process_delivery(inventory, user_input)