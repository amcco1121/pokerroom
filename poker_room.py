import random
#For flush function
import collections

starting_balance = 1000

print()
print()
print()
print("Welcome to the poker room!")
print()
print("Your starting balance is: ",starting_balance)
print()
print("GOOD LUCK!")

def main(balance):
   players = 1
   print()
   print()
   print()
   bet = input("What is your bet? (Enter Q to quit)  ")
   if bet == "Q":
      return ("Thank you for playing!")
   print()
   print()
   #Shuffles the deck for the new hand
   new_deck = shuffle()
   #Below statement to see shuffled deck
   #print(("Shuffled Deck: "),new_deck)
   #Deals out the amount of cards to the user
   hand = deal(new_deck)
   print()
   #Shows hand written out -- Created to be more visible than raw numbers
   print("Your Hand: ",pretty_cards(hand))
   print()
   your_5 = (show_cards(hand))
   print()
   print()
   #Extracts all the numbers
   numbers_list = (numbers_package(your_5))
   hand = hand_identifier(numbers_list,your_5)
   print ("Result: "+hand)
   print()
   payout = payout_calculator(bet,hand)
   print ("You win: ",payout)
   print()
   bankroll = bankroll_calculator(balance,payout)
   print ("Current Balance: ",bankroll)
   print() 
   new_balance = bankroll
   main(new_balance)


def shuffle():
   deck = []
   for i in range(1,53,1):
      deck.append(int(i))
   random.shuffle(deck)
   return deck

def deal(new_deck):
   your_hand = []
   your_hand.append(new_deck[0])
   your_hand.append(new_deck[1])
   your_hand.append(new_deck[2])
   your_hand.append(new_deck[3])
   your_hand.append(new_deck[4])
   return your_hand

def show_cards(your_hand):
   your_cards = []
   for i in your_hand:
      suit = suit_decide(i)
      number = number_decide(i,suit)
      your_cards.append(str(number))
      your_cards.append(str(suit))
   return your_cards

def pretty_cards(your_hand):
   pretty_cards = []
   for i in your_hand:
      suit = suit_decide(i)
      number = number_decide(i,suit)
      pretty_cards.append(str(number)+" "+str(suit))
   return pretty_cards


def suit_decide(card):
   if card <= 13:
      return "Clubs"
   elif card <= 26:
      return "Spades"
   elif card <= 39:
      return "Diamonds"
   elif card <= 52:
      return "Hearts"
   else:
      return ("ERROR")

def number_decide(number,suit):
   if suit == "Clubs":
      if number == 11:
         return "Jack of"
      elif number == 12:
         return "Queen of"
      elif number == 13:
         return "King of"
      elif number == 1:
         return "Ace of"
      else:
         return number-0
   elif suit == "Spades":
      if number == 24:
         return "Jack of"
      elif number == 25:
         return "Queen of"
      elif number == 26:
         return "King of"
      elif number == 14:
         return "Ace of"
      else:
         return number-13
   elif suit == "Diamonds":
      if number == 37:
         return "Jack of"
      elif number == 38:
         return "Queen of"
      elif number == 39:
         return "King of"
      elif number == 27:
         return "Ace of"
      else:
         return number -26
   elif suit == "Hearts":
      if number == 50:
         return "Jack of"
      elif number == 51:
         return "Queen of"
      elif number == 52:
         return "King of"
      elif number == 40:
         return "Ace of"
      else:
         return number -39

#True if there is a flush
def flush_identifier(your_5):
   counter=collections.Counter(your_5)
   #print(counter.values())--to confirm function
   #print(max(counter.values()))--to confirm function
   if max(counter.values()) == 5:
      return True
   else:
      return False

#your_5=List of only the suits
def numbers_package(your_5):
   numbers_list = []
   numbers_list.append(your_5[0])
   numbers_list.append(your_5[2])
   numbers_list.append(your_5[4])
   numbers_list.append(your_5[6])
   numbers_list.append(your_5[8])
   return(numbers_list)

def pair_identifier(numbers_list):
   counter=collections.Counter(numbers_list)
   if 2 in (counter.values()):
      return True
   else:
      return False

def three_of_a_kind_indetifier(numbers_list):
   counter=collections.Counter(numbers_list)
   if 3 in (counter.values()):
      return True
   else:
      return False

def four_of_a_kind_identifier(numbers_list):
   counter=collections.Counter(numbers_list)
   if 4 in (counter.values()):
      return True
   else:
      return False

def hand_identifier(numbers_list,your_5):
   if pair_identifier(numbers_list) == True:
      return "Pair"
   elif three_of_a_kind_indetifier(numbers_list) == True:
      return "3 of a Kind"
   elif four_of_a_kind_identifier(numbers_list) == True:
      return "4 of a Kind"
   elif flush_identifier(your_5) == True:
      return "Flush"
   else:
      return "No Winning Hand"

def payout_calculator(bet,hand):
   if hand == "Pair":
      return (int(bet)*1)
   elif hand == "3 of a Kind":
      return (int(bet)*4)
   elif hand == "4 of a Kind":
      return (int(bet)*50)
   elif hand == "Flush":
      return (int(bet)*5)
   else:
      return (-int(bet))

def bankroll_calculator(starting_balance,payout):
   return (int(starting_balance) + int(payout))



   

main(starting_balance)
