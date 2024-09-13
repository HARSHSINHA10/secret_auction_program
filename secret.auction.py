logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print(logo)

print("Welcome to The Secret Auction Program!")
auction_going = True



def highest_bidder(bidding_file):
    winner= ""
    highest_amount = 0
    for bidder in bidding_file:
        bid_price = bidding_file[bidder]
        if bid_price >highest_amount:
            highest_amount = bid_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_amount}")
bids = {}

while auction_going:
 user_name = input("What is your name?:")
 bid_price = int(input("What is your bidding amount?:$"))


 bids[user_name] = bid_price
 more_bid_input = input("Is there any other bidder: yes or no?\n").lower()
 if more_bid_input == "no":
     auction_going = False
     highest_bidder(bids)

 elif more_bid_input == "yes":
     print("\n"*1000)
     auction_going = True


