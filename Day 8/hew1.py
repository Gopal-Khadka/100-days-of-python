from replit import clear
from logo import logo

end = False
bid_dict = {}


def high_bid(bid_record):
  max_bid = 0
  winner = ""

  for bidder in bid_record:
    amt = bid_record[bidder]
    if amt > max_bid:
      max_bid = amt
      winner = bidder
  print(f"The winner is {winner} with bid of ${max_bid}")


print(logo)
while not end:
  user_name = input("Enter your name: ")
  user_bid = int(input("Enter your bid amount: " + "$"))
  bid_dict[user_name] = user_bid

  again = input("Are there more bidders left? " + "Type yes or no \n").lower()
  if again == "no":
    end = True
    high_bid(bid_dict)
  elif again == "yes":
    clear()

  else:
    print("Invalid values entered.")
    end = True
