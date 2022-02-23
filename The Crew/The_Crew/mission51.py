# this algorithm is applicable to mission 1, 2, 4, 10, 42, 47
import random
from communication import *



# Random_play function ask the player to give a card randomly, it will also be remove in the player class
def Random_play(player):
    cards = player.B + player.Y + player.G + player.P + player.Rocket
    card = random.choice(cards)

    if len(card) > 2:
        player.Rocket.remove(card)
    elif card[0] == 'P':
        player.P.remove(card)
    elif card[0] == 'G':
        player.G.remove(card)
    elif card[0] == 'Y':
        player.Y.remove(card)
    else:
        player.B.remove(card)
    return card

# Player_card function ask the player to give a card based on the color condition
def Player_card(player, color):
    card = ''
    if color == "Rocket":
        if len(player.Rocket) != 0:
            card = random.choice(player.Rocket)
            player.Rocket.remove(card)
        else:
            card = Random_play(player)
    elif color == 'B':
        if len(player.B) != 0:
            card = random.choice(player.B)
            player.B.remove(card)
        else:
            card = Random_play(player)
    elif color == 'Y':
        if len(player.Y) != 0:
            card = random.choice(player.Y)
            player.Y.remove(card)
        else:
            card = Random_play(player)
    elif color == 'G':
        if len(player.G) != 0:
            card = random.choice(player.G)
            player.G.remove(card)
        else:
            card = Random_play(player)
    elif color == 'P':
        if len(player.P) != 0:
            card = random.choice(player.P)
            player.P.remove(card)
        else:
            card = Random_play(player)
    else:
        card = Random_play(player)
    return card





# mission1 is the main function of the whole game operation,
def Player_round51(players, leader, num_round, desk, judge_task, num_of_player, mission):
    result = 0

    Leader_color = ""
    # print("------------------ Round %d " % (num_round) + "----------------------")
    num_round += 1

    num_players = len(players)
    players[leader].leader = False

    card = Player_card(players[leader], "random")
    # print("Player " + players[leader].name + " played card: " + card)

    communicating(players[leader], mission, num_round)
    # print("Player " + players[leader].name + " communicating: " + players[leader].communication + '\n')

    desk[leader] = card
    leader = (leader + 1) % num_players  # trun to next player

    # leader is not the actual leader in here. It's just an i variable to 
    # represent the who has the next turn to play the card

    if len(card) > 2:
        color = "Rocket" #color here is fixed based on the round leader so no issue here
    else:
        color = card[0]

    for i in range(num_players - 1): # 1 -- Y1 2 -- R1 & 3 
        card = Player_card(players[leader], color)
        desk[leader] = card
        # print("Player " + players[leader].name + " played card: " + card)
        communicating(players[leader], mission, num_round)
        # print("Player " + players[leader].name + " communicating: " + players[leader].communication + '\n')
        leader = (leader + 1) % num_players  # turn to next player


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
                # this desk[][] is not 2d array, its comparing the charactor in side on stirng of array
                # with winner's charactor
    players[leader].leader = True
    players[leader].win_cards += desk
    players[leader].win_cards.sort()

    # print("This round winner is player " + players[leader].name + '\n')
    # print("The won cards are: ")
    #print(desk)
    # print(players[leader].win_cards)  # small mistake
    # print

    # Task Completed checked, if task is completed it will be remove from judge_task
    for single_trick_card in players[leader].win_cards:
        for single_task_card in players[leader].task:
            if single_task_card == single_trick_card:
                # print "Task", single_task_card, "Completed"
                players[leader].task.remove(single_task_card)
                judge_task.remove(single_task_card)
                # print judge_task

    # print"####################################"

    if len(judge_task) == 0:
        # print "All mission Complete"
        result = 1
        return result

    else:
        if num_round == (40 / num_of_player + 1):
            # print "Not all task Complete, Mission failed"
            # print "Remaining cards", judge_task
            result = 0
            return result
        else:
            # countine until as long as the game is not over
            num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            result = Player_round51(players, leader, num_round, desk, judge_task, num_of_player, mission)
            return result
