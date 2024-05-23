# Define your functions
def coffee_bot():
  print("Welcome to the Jocal cafe!")

  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))

  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n")
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()
    # get_size()

def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_drink_type():
  res = input("What type of drink are you after today?\n[a] Latte\n[b] Espresso\n[c] Iced Coffee\n")
  
  if res == 'a':
    return order_latte()
  elif res == 'b':
    return 'Espresso, 3 a day will keep the sleep away'
  elif res == 'c':
    return 'Iced Coffee to keep you cool today in the hot Canberra weather!'
  else:
    print_missed_order()
    return get_drink_type()
    get_drink_type()

def print_missed_order():
  print("It looks like you have not ordered yet, would you be interested in a Jocal special?")
  print("Special is the first coffee is free!")

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] Full Cream milk \n[b] Oat milk \n[c] Soy milk \n')
  if res == 'a':
    return 'Latte'
  elif res == 'b':
    return 'Oat milk Latte'
  elif res == 'c':
    return 'Soy milk Latte'
  else:
    print_message()
    return order_latte()
    # order_latte()


coffee_bot()

# TESTING MY GIT PUSH on GIT Coffeee.py Joey
 

# size = input(get_size()