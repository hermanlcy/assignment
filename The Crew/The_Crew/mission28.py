import random
from mission1 import *




def Player_round28(players, leader, num_round, desk, judge_task, num_of_player, priority_list, priority_index, task_index, omage_task, task_number, communicated):

    print("------------------ Round %d " % (num_round) + "----------------------")
    num_round += 1
    mission = 28
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
    print(desk)
    print

    priority_fail = False

    # Task Completed checked, if task is completed it will be remove from judge_task
    for single_trick_card in players[leader].win_cards:
        for single_task_card in players[leader].task:
            if single_task_card == single_trick_card:
                
                print "Task", single_task_card, "Completed"
                players[leader].task.remove(single_task_card)
                judge_task.remove(single_task_card)
                
                if priority_index < len(priority_list):
                    if priority_list[priority_index] == single_task_card:
                         priority_index += 1
                    else:
                        print "Priority FAILURE"
                        priority_fail = True
                elif task_index != task_number and single_task_card == omage_task:
                    print "Omega FAILURE"
                    priority_fail = True
                task_index += 1

    # print"####################################"

    if priority_fail == True:
        print "Task Priority or Omage failed, Mission failed"

    else:
        if len(judge_task) == 0:
            print "All mission Complete"

        else:
            if num_round == (40 / num_of_player + 1):
                print "Not all task Complete, Mission failed"
                print "Remaining cards", judge_task
            else:
                # countine until as long as the game is not over
                num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
                Player_round28(players, leader, num_round, desk, judge_task, num_of_player,
                               priority_list, priority_index, task_index, omage_task, task_number, communicated)
