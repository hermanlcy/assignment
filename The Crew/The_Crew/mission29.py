import random
from mission1 import *



def Player_round29(players, leader, num_round, desk, num_of_player, mission, communicated, tricks):

    print("------------------ Round %d " % (num_round) + "----------------------")
    num_round += 1

    num_players = len(players)
    players[leader].leader = False

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

    players[leader].leader = True
    players[leader].win_cards += desk
    players[leader].win_cards.sort()

    print("\nThis round winner is player " + players[leader].name + '\n')
    print("The won cards are: ")
    print(desk)
    print

    tempW = players[leader].name
    temp = tricks[str(tempW)]
    temp1 = temp + 1
    tricks[str(tempW)] = temp1
    print tricks

    trick_win = False
    P1 = -1
    P2 = -1

    for i in range(num_of_player):
        for j in range(num_of_player):
            if tricks[str(i)] - tricks[str(j)] == 2 or tricks[str(j)] - tricks[str(i)] == 2:
                trick_win = True
                if tricks[str(i)] > tricks[str(j)]:
                    P1 = i
                    P2 = j
                else:
                    P2 = i
                    P1 = j


    # print"####################################"

    if trick_win == True:
        print "Trick wining numbers failed, Mission failed"
        print "Player", P1, "won 2 more tricks than Player", P2

    else:
        if num_round == (40 / num_of_player + 1):
            print "Mission Complete"
        else:
            # countine until as long as the game is not over
            num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round29(players, leader, num_round, desk, num_of_player, mission, communicated, tricks)
