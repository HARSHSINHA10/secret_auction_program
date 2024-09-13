# secret_auction_program
Secret Auction Program
 In a blind auction, participants secretly submit their bids, and the highest bidder wins. This project is implemented using Python.

Project Description
The Secret Auction Program allows multiple users to place secret bids, and the highest bid wins. It follows these steps:

Each participant enters their name and bid amount.
After each bid, the screen is cleared to ensure secrecy.
The process continues until no more participants want to place a bid.
The program then announces the highest bidder and their bid amount.
Features
Allows multiple participants to place bids.
Ensures secrecy by clearing the screen after each bid.
Announces the highest bidder at the end of the auction.
How to Run the Program
Clone or download the repository to your local machine.
Make sure you have Python installed on your system.
Run the program using any Python IDE (like PyCharm) or directly from the terminal/command prompt.
Each participant can enter their name and bid when prompted.
After all bids are placed, the program announces the highest bidder.

Example of Running the Program:
Welcome to The Secret Auction Program!
What is your name?: Alice
What is your bidding amount? 150
Is there any other bidder? Yes or no? yes
What is your name?: Bob
What is your bidding amount? 200
Is there any other bidder? Yes or no? no
The winner is Bob with a bid of $200

Files
main.py: Contains the logic for the blind auction.
README.md: Provides an overview of the project.

Requirements:
Python 3.x

Instructions:
Download or clone this repository.
Run main.py.
You can enter your name and bid when prompted.
Once the bidding process is over, the program will announce the winner.
Screen Clearing
The program uses print("\033c", end="") to clear the screen after each bid. This works in most terminals. If this does not work for your environment, you can replace it with print("\n" * 100) to simulate clearing the screen.

License:
This project  is for learning purposes only. Feel free to use, modify, and distribute the code.

