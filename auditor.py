inventory = 0
failed = 0

while inventory < 500:
  user_input = input('Enter "Quit" to exit \nEnter stock quantity: ')
  if user_input.lower() == 'quit':
    print(f'Total Units Processed: {inventory}')
    print(f'Number of Failed/Rejected Entries: {failed}')
    break
  elif user_input.isdigit():
    if int(user_input) > 0:
      inventory += int(user_input)
      failed -= 1
    else:
      print('No negative numbers')
  else:
    print('Please enter a number')
  print('hello')
  failed += 1
else:
  print('ALERT: Too many units')