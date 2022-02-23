import random
from mission1 import *

#mission 13's winning condition is really similar to mission9. Only difference is that all four rocket card has to win a round seperately. 
# Which mean people who has rocket card on hand will have the same task card accordingly

#things to implement next

# implement two feature next for mission 26
# first unless you are running out the resources don't tag along with any number 1 card when you don't have card to match with the leading suit
# second dish out the number 1 card only when you are confident

#implemented
# we are restricting the player to dish out the rocket card when they are not running out of the resources

# Random_play function ask the player to give a card randomly, it will also be remove in the player class

# mission13 test
def Player_round13(players, leader, num_round, desk, judge_task, num_of_player, communicated):

    print("------------------ Round %d " % (num_round) + "----------------------")
    num_round += 1
    mission = 13
    num_players = len(players)
    players[leader].leader = False

    if len(players[leader].B) != 0 or len(players[leader].G) != 0 or len(players[leader].Y) != 0 or len(players[leader].P) != 0:
        card = Player_card13(players[leader], "random")
        print("\nPlayer " + players[leader].name + " played card: " + card)
        if communicated < num_of_player:
            communicated = communicating(players[leader], mission, num_round, communicated)
        if card in players[leader].communication:
            players[leader].communication = ""
        elif players[leader].communication is not "":
            print("Player " + players[leader].name + " communicating: " + players[leader].communication)
        desk[leader] = card
    else:
        card = Player_card(players[leader], "Rocket")
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

    for i in range(num_players - 1):  # player 1 & 2
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

    if len(judge_task) == 0:
        print "Therefore Mission 13 Complete"

    else:
        if num_round == (40 / num_of_player + 1):
            print "Not All task Completed, So Mission 13 fail"
            print "Remaining cards", judge_task
        else:
            # countine until as long as the game is not over
            num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round13(players, leader, num_round, desk, judge_task, num_of_player, communicated)

