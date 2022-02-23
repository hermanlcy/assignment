import random
from mission1 import *

# mission 9 & 26's main point is to first limit the 1 card's dish out and eliminate the rocket card first. We need to memerise what card has been
# dished out in order to calculate what are the remaining number in the color of the number 1 card we wanna win.
# for e.g. in order to win with Y1 i need to know when is the point of all the card in Y a part from 1 has
# all been dished out. Then i'm confident to dish out 1 to win (now its a 50 50 win chance)
# So three thing limit : first don't dish out the 1 card when you not confident(meaning Y 2 to 9 has been used)
# :two when you saw a 1 card on desk don't use rocket card if you can (meaning you have other substitution)
# it is best to throw rocket card in frist round (eliminate the rocket card)

# implement two feature next for mission 26
# first unless you are running out the resources don't tag along with any number 1 card when you don't have card to match with the leading suit
# second dish out the number 1 card only when you are confident

# Random_play function ask the player to give a card randomly, it will also be remove in the player class

# mission9 test
def Player_round9(players, leader, num_round, desk, judge_task, num_of_player, communicated):

    mission = 9
    print("------------------ Round %d " % (num_round) + "----------------------")
    counterY = 8
    counterG = 8
    counterP = 8
    counterB = 8
    counterR = 4

    if num_round == 1: # this if condition only work for the first round to eliminate the rocket cards as much as possible

        num_round = num_round + 1
        num_players = len(players)
        players[leader].leader = False
        if counterY == 0 and counterR == 0 and players[leader].task == "Y1":
            card = Player_card(players[leader],"Y")
        elif counterG == 0 and counterR == 0 and players[leader].task == "G1":
            card = Player_card(players[leader],"G")
        elif counterP == 0 and counterR == 0 and players[leader].task == "P1":
            card = Player_card(players[leader],"P")
        elif counterB == 0 and counterR == 0 and players[leader].task == "B1":
            card = Player_card(players[leader],"B")
        else:
            card = Player_card(players[leader],"Rocket")

        print("\nPlayer " + players[leader].name + " played card: " + card)
        if communicated < num_of_player:
            communicated = communicating(players[leader], mission, num_round, communicated)
        if card in players[leader].communication:
            players[leader].communication = ""
        elif players[leader].communication is not "":
            print("Player " + players[leader].name + " communicating: " + players[leader].communication)

        if card[0] == 'Y':
            counterY = counterY -1
        elif card[0] == 'G':
            counterG = counterG -1
        elif card[0] == 'P':
            counterP = counterP -1
        elif card[0] == 'B':
            counterB = counterB -1
        else:
            counterR = counterR -1

        desk[leader] = card
        leader = (leader + 1) % num_players  # trun to next player
        
        if len(card) > 2:
            color = "Rocket"
        else:
            color = card[0]

        for i in range(num_players - 1):
            card = Player_card(players[leader], color)
            desk[leader] = card
            print("\nPlayer " + players[leader].name + " played card: " + card)
            if communicated < num_of_player:
                communicated = communicating(players[leader], mission, num_round, communicated)
            if card in players[leader].communication:
                players[leader].communication = ""
            elif players[leader].communication is not "":
                print("Player " + players[leader].name + " communicating: " + players[leader].communication)
            leader = (leader + 1) % num_players  # trun to next player

        winner = "x"

        for i in range(len(desk)):
            if len(desk[i]) > len(winner):
                winner = desk[i]
                leader = i
            elif len(desk[i]) == len(winner):
                if len(winner) > 2:
                    if winner[-1] < desk[i][-1]:
                        winner = desk[i]
                        leader = i
                else:
                    if desk[i][0] == color and winner[0] != color:
                        winner = desk[i]
                        leader = i
                    elif desk[i][0] == color and winner[0] == color:
                        if desk[i][-1] > winner[-1]:
                            winner = desk[i]
                            leader = i

        players[leader].leader = True
        players[leader].win_cards += desk
        players[leader].win_cards.sort()

        print("\nThis round winner is player " + players[leader].name + '\n')
        print("The won cards are: ")
        print(players[leader].win_cards)
        print

    else:
        #start from round 2 here

        num_round += 1

        num_players = len(players)
        players[leader].leader = False

        if counterY == 0 and counterR == 0 and players[leader].task == "Y1":
            card = Player_card(players[leader],"Y")
        elif counterG == 0 and counterR == 0 and players[leader].task == "G1":
            card = Player_card(players[leader],"G")
        elif counterP == 0 and counterR == 0 and players[leader].task == "P1":
            card = Player_card(players[leader],"P")
        elif counterB == 0 and counterR == 0 and players[leader].task == "B1":
            card = Player_card(players[leader],"B")
        else:
            card = Player_card(players[leader], "random")

        print("\nPlayer " + players[leader].name + " played card: " + card)
        if communicated < num_of_player:
            communicated = communicating(players[leader], mission, num_round, communicated)
        if card in players[leader].communication:
            players[leader].communication = ""
        elif players[leader].communication is not "":
            print("Player " + players[leader].name + " communicating: " + players[leader].communication)
        desk[leader] = card
        leader = (leader + 1) % num_players  # trun to next player

        if len(card) > 2:
            color = "Rocket"
        else:
            color = card[0]

        for i in range(num_players - 1):
            card = Player_card(players[leader], color)
            desk[leader] = card
            print("\nPlayer " + players[leader].name + " played card: " + card)
            if communicated < num_of_player:
                communicated = communicating(players[leader], mission, num_round, communicated)
            if card in players[leader].communication:
                players[leader].communication = ""
            elif players[leader].communication is not "":
                print("Player " + players[leader].name + " communicating: " + players[leader].communication)
            leader = (leader + 1) % num_players  # trun to next player

        winner = "x"

        for i in range(len(desk)):
            if len(desk[i]) > len(winner):
                winner = desk[i]
                leader = i
            elif len(desk[i]) == len(winner):
                if len(winner) > 2:
                    if winner[-1] < desk[i][-1]:
                        winner = desk[i]
                        leader = i
                else:
                    if desk[i][0] == color and winner[0] != color:
                        winner = desk[i]
                        leader = i
                    elif desk[i][0] == color and winner[0] == color:
                        if desk[i][-1] > winner[-1]:
                            winner = desk[i]
                            leader = i

        players[leader].leader = True
        players[leader].win_cards += desk
        players[leader].win_cards.sort()

        print("\nThis round winner is player " + players[leader].name + '\n')
        print("The won cards are: ")
        print(players[leader].win_cards)
        print

    # Task Completed checked, if task is completed it will be remove from judge_task
    for single_trick_card in players[leader].win_cards:
        for single_task_card in players[leader].task:
            if single_task_card == single_trick_card:
                print "Task", single_task_card, "Completed"
                players[leader].task.remove(single_task_card)
                judge_task.remove(single_task_card)

    # print"####################################"

    if len(judge_task) != 4:
        print "Therefore Mission 9 Complete"

    else:
        if num_round == (40 / num_of_player + 1):
            print "Not even one task Completed, So Mission 9 fail"
            print "Remaining cards", judge_task
        else:
            # countine until as long as the game is not over
            num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round9(players, leader, num_round, desk, judge_task, num_of_player, communicated)


    counterY = 8
    counterG = 8
    counterP = 8
    counterB = 8
    counterR = 4

    if card[0] == 'Y':
        counterY = counterY -1
    elif card[0] == 'G':
        counterG = counterG -1
    elif card[0] == 'P':
        counterP = counterP -1
    elif card[0] == 'B':
        counterB = counterB -1
    else:
        counterR = counterR -1
    
   