import os
import art
import random


def game():
    os.system('cls')
    print(art.logo)
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    computer_hand = []
    dealer_ace = False
    
    for i in range(2): #generating two random cards and then removing them form the deck for the player and computer and check for ace in computer
        player_card = random.choice(cards)
        cards.remove(player_card)
        if player_card == 11 and (sum(player_hand)+11>21):
            player_hand.append(1)
        else:
            player_hand.append(player_card)
        
        computer_card = random.choice(cards)
        cards.remove(computer_card)
        if (dealer_ace == True) and (computer_card == 11):
            computer_hand.append(1)
        elif computer_card == 11:
            dealer_ace = True
            computer_hand.append(computer_card)
        else:
            computer_hand.append(computer_card)
    
        
    # asking user if he wants to hit
    while True:
        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")
        continue_game = input("Type 'y' to hit, type 'n' to pass: ")
        print("")
        if continue_game == 'n':
            if sum(computer_hand) > sum(player_hand):
                print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
                print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
                print("You lose")
                return
            else:
                break
            
        elif continue_game == 'y':
            player_card = random.choice(cards)
            cards.remove(player_card)
            if (sum(player_hand)+11>21) and player_card == 11 and 11 not in player_hand and 1 not in player_hand:
                player_hand.append(1)
            else:
                player_hand.append(player_card)
            
            if sum(player_hand) > 21 and 11 in player_hand and 1 not in player_hand:
                player_hand.remove(11)
                player_hand.append(1)
            
            if sum(player_hand)>21:
                print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
                print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
                print("You busted. You lose.")
                return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            print("")
            
            
            
    while True:   # if the dealer has less than 17 he must hit. i took care of ace
        if sum(computer_hand)>sum(player_hand):
            print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
            print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
            print("You lose")               
            return
        
        if sum(computer_hand) < 17:
            computer_card = random.choice(cards)
            cards.remove(computer_card)
            if dealer_ace == True and computer_card == 11:
                computer_hand.append(1)
            elif computer_card == 11 and (sum(computer_hand)+11)>21:
                computer_hand.append(1)
            else:
                computer_hand.append(computer_card)
            
            if sum(computer_hand)>21:
                print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
                print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
                print("Opponent busted. You win")
                return
            
            if sum(computer_hand)>sum(player_hand):
                print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
                print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
                print("You lose")               
                return
        else:
            break
            
        
    print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
    if sum(player_hand) > sum(computer_hand):
        print("You win")
    else:
        print("It's a draw")
    print("")
    input("Press Enter to continue...")
        
continue_game = ""

while continue_game != 'n':
    continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if continue_game == 'y':
        game()
    


