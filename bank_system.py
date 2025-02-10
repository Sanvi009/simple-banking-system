total_amount = 0

def deposit():
  while True:
    global total_amount
    ask = input("How much would you like to deposit? :")
    if ask.isdigit():
      ask = int(ask)
      total_amount += ask
      print(f"{ask}$ has deposited to your account")
      break
    else:
      print("please enter ammount only ( no symbol )")

def withdraw():
  global total_amount
  while True:
    ask = input("how much you want to withdraw :")
    if ask.isdigit():
      ask = int(ask)
      if ask < total_amount:
        total_amount -= ask
        print(f"{ask}$ has withdrawn from your account")
        break
      else:
        print(" you don't have enough money to withdraw")
        break
    else:
      print("enter ammount only ( no symbol )")
      


def check_balance():
  global total_amount
  print(f"your current balance is {total_amount}$")
  

def home():
  
  
  while True:
    print("_______wellcome to bank of python_______\n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Quit")
    ask = input("what would you like to do :")
    if ask == "1":
      deposit()
    elif ask == "2":
      withdraw()
    elif ask == "3":
      check_balance()
    elif ask == "4":
      print("Thank you for using bank of python")
      break
    else:
      print("please enter a valid number")


home()
