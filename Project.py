############################################################
# ICS34U
# Vishva Madu
# Card Game Blackjack
# Apr 9, 2021
############################################################

# To know the rules of Blackjack, read the proposal of the CAT
# This card game is designed to simulate the physical game of Blackjack and be playable in a coded program

import random

money = 100

#Modular code 
def Option(money):
  if money > 0:
    option = input("Enter option [PLAY AGAIN = P+<ENTER>, QUIT = Q+<ENTER> ]: " + "\n")
    play_agian = 'P'
    quit = 'Q'
    if option == play_agian:
      print("-----------------------------------")
      print("New Game" + "\n")
      Blackjack(money) #return to start of program
    elif option == quit:
      print("Thanks for Playing!")
      exit() #ends program
    elif option != play_agian and quit:
      Option() #restarts function when invaild charcter
  else:
    print("You have no more money left to play!")
    exit()

# Created Standard Deck of 52 cards (excluding Joker Cards) in a dictionary (name = key, number = value)

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}

class Card:      
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return self.rank + ' of ' + self.suit

class Deck:          
  def __init__(self):
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    card = self.deck.pop()
    return card

class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0
  def add_card(self, card):
    self.cards.append(card)
    self.value += values[card.rank]
    

# Blackjack(money) function runs the whole program and returns the new value of money after winning losing or tieing a bet

def Blackjack(money):
  
  # Input your bet using number characters only and uses if-else statement / operators to ensure amount bet is not beyond money in account
  print("Money in your account: $", money)
  print()
  print("Use Only Number Characters When Inputing Bet")
  a = 1
  while a == 1:
    try:
      bet = float(input("Enter your bet: $"))
    except:
      Blackjack(money)
    else:
      bet = float(bet)
    if ((bet <= money) and (bet > 0)):
      print()
      a += 1
    else:
      print("Enter a bet less than or equal to money in account") 
      print()
  
  
  # Dealing Cards Method - deals starting 2 cards to the player and dealer in two lists (one contains the name of cards, the other contains the values) a dictionary is created to keep track of all cards drawn in the game

  deck = Deck()
  deck.shuffle()

  print("Dealing Player Cards ..." + '\n')

  player = Hand()

  player.add_card(deck.deal())
  player.add_card(deck.deal())

  player_counter = 0
  print("Player's cards are:")
  for i in player.cards:
    print(player.cards[player_counter])
    player_counter += 1
  print("Player's total hand value:", player.value)
  print()

  # Card Check Method - checks for duplicate cards drawn and makes program draw another card that is not a duplicate from the dictionary containing the cards drawn for player and dealer

  dealer = Hand()

  print("Dealing Dealer Cards ..." + '\n')

  dealer.add_card(deck.deal())
  dealer.add_card(deck.deal())
    
  print("Dealer's cards are:")
  print(dealer.cards[0])
  print("Unknown Card")
  print()
  
  # Player Choices Method - player inputs choice to draw a card, stand and double down, an if-else statement compares input with choices to see if one of them matches under a while loop for next choices after a draw (stand and double-down stop loop)
  
  counter = 1
  while counter == 1:

    draw = "1"
    stand = "2"
    double_down = "3"

    print("Use Only Number Characters When Inputing Choice")
    choice = (input("Player enter choice: [draw = 1, stand = 2, double_down = 3]" + "\n"))
        
    m = 1
    while m == 1:
      if choice == "1" or "2" or "3":
        m += 1
      else:
        choice = (input("Player enter choice: [draw = 1, stand = 2, double_down = 3]" + "\n"))
      
    # An invaild number enter repeats loop asking player to enter choice agian

    if draw == choice:
      print("Drawing Card" + '\n')
      player.add_card(deck.deal())
      
      player_counter = 0
      print("Player's cards are:")
      for i in player.cards:
        print(player.cards[player_counter])
        player_counter += 1
      print("Player's total hand value:", player.value)
      print()

    elif stand == choice:
      print("Stand" + "\n")
      counter += 1

    elif double_down == choice:
      print("Double Down" + '\n')
      bet = bet*2 
      print("New bet: $",bet)
      print("Drawing Card" + '\n')
      player.add_card(deck.deal())
      
      player_counter = 0
      print("Player's cards are:")
      for i in player.cards:
        print(player.cards[player_counter])
        player_counter += 1
      print("Player's total hand value:", player.value)
      print()
      counter += 1

    # Player's Standings with Player_Hand_Value Method - when the player is done drawing cards or cannot draw anymore, the value of the hand is being compared with conditions to see if one of them matches 

    # Play Agian or Quit Option Function - when the player gets a bust before dealer reveals cards or when finshed a game through the possible outcomes, the player has a choice to play agian or quit (same method idea used when choosing to draw, stand or double down)

    if player.value > 21:
      print("Player is Bust!")
      money = money - bet
      Option(money)
      counter += 1

   # Revealing Dealer's Starting Cards Method - if the player is <=21 after done drawing cards, the dealer will reveal his starting cards when choosing to stand, double down or on 21
      
    elif player.value < 21:
      print("Player's total hand value:", player.value)
      print()
      if choice == stand or choice == double_down:
        dealer_counter = 0
        print("Dealer's cards are:")
        for i in dealer.cards:
          print(dealer.cards[dealer_counter])
          dealer_counter += 1
        print("Dealer's total hand value:", dealer.value)
        print()

    elif player.value == 21:
      print("Blackjack!" + '\n')
      dealer_counter = 0
      print("Dealer's cards are:")
      for i in dealer.cards:
        print(dealer.cards[dealer_counter])
        dealer_counter += 1
      print("Unknown Card")
      print("Dealer's total hand value:", dealer.value)
      print()
      counter += 1
      
    
  # Dealer Attempting to Beat Player Method - When the player is done drawing cards and is below 21 or on 21, the dealer will draw if cards if needed to beat the value of player's hand value, if-conditions are placed to stop dealer from drawing cards if he is above 21,on 21 or beated player's hand while <= 21

  count = 1
  while count == 1:

    if dealer.value <= player.value <= 21:
      print()
      print("Drawing Card")
     
      dealer.add_card(deck.deal())

      dealer_counter = 0
      print("Dealer's cards are:")
      for i in dealer.cards:
        print(dealer.cards[dealer_counter])
        dealer_counter += 1
      print("Dealer's total hand value:", dealer.value)
      print()
        
    # Win, Lose or Tie and Bet/Money Impact Method - Base on the outcome of the dealer's hand value, the player will win, lose or tie which affects the player's bet (profit or loss) and the new amount of money in the account for next game

    if dealer.value > 21:
      print("Dealer is Bust!")
      print("Player Wins!" + "\n")
      money = money + (bet*2) # bet doubles when you win
      Option(money)
      
    elif dealer.value > player.value <= 21:
      print("The House Wins!" + "\n")
      money = money - bet # bet is subtarcted from money when you lose
      Option(money)
      

    elif dealer.value == 21 and player.value == 21:
      print("Blackjack Tie!" + "\n")
      money = money # money remains the same from start of game when you tie (bet returns)
      Option(money)

Blackjack(money) #calls Blackjack(money) function allowing program to run
