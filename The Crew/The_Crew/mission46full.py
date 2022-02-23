import random
from mission1 import *

# mission 46's logic is say who has pink 9 then the person on the left handside will need to winnig all card in pink

# run this mission for 4 times that there is some error but the fifth time we run this it will gives out correct output
# Winning logic
# whoever is the chosen one if he or she are the round leader then they can either dish out any color apart from pink 
# if other player are leader and they don't have big pink card then dish out pink card
# if the chosen one has rocket and he or she can dish out the rocket to win pink card then they should dish out rocket card to win the round
# all other players should trying to dish out pink when the chosen one is dishing out other color apart from pink if they can
# mission9 test
def Player_round46(players, leader, num_round, desk, judge_task, num_of_player):
    chosen_one = 0
    print("------------------ Round %d " % (num_round) + "----------------------")

    if num_round == 1: # this if condition only work for the first round to eliminate the rocket cards as much as possible
        for i in range(len(players)):
            if "P9" in players[i].P:
                if len(players) == 3:
                    if i == 2:
                        chosen_one == 0
                    else:
                        chosen_one == i + 1
                if len(players) == 4:
                    if i == 3:
                        chosen_one == 0
                    else:
                        chosen_one == i + 1
                if len(players) == 5:
                    if i == 4:
                        chosen_one == 0
                    else:
                        chosen_one == i + 1

        num_round = num_round +1
        num_players = len(players)
        players[leader].leader = False
            
        if leader != chosen_one and "P9" not in players[leader].P and "P8" not in players[leader].P and "P7" not in players[leader].P and "P6" not in players[leader].P:
            card = Player_card(players[leader],"P")
        else:
            card = Player_card(players[leader],"random")

        print("Player " + players[leader].name + " played card: " + card + '\n')

        desk[leader] = card
        leader = (leader + 1) % num_players  # trun to next player
        
        if len(card) > 2:
            color = "Rocket"
        else:
            color = card[0]

        for i in range(num_players - 1):
            if i == chosen_one:
                if color == "P" :
                    if len(players[chosen_one].P) == 0 and len(players[chosen_one].Rocket) != 0:
                        card = card = Player_card(players[leader],"Rocket")
            else:
                card = Player_card(players[leader], color)
            desk[leader] = card
            print("Player " + players[leader].name + " played card: " + card + '\n')
            leader = (leader + 1) % num_players  # trun to next player
# end of part 1
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

        print("This round winner is player " + players[leader].name + '\n')
        print("The won cards are: ")
        print(players[leader].win_cards)
        print

    else:
        #start from round 2 here

        num_round += 1

        num_players = len(players)
        players[leader].leader = False

        if leader != chosen_one and "P9" not in players[leader].P and "P8" not in players[leader].P and "P7" not in players[leader].P and "P6" not in players[leader].P:
            card = Player_card(players[leader],"P")
        else:
            card = Player_card(players[leader],"random")
            
        print("Player " + players[leader].name + " played card: " + card + '\n')

        desk[leader] = card

        leader = (leader + 1) % num_players  # trun to next player

        if len(card) > 2:
            color = "Rocket"
        else:
            color = card[0]

        for i in range(num_players - 1):
            if i == chosen_one:
                if color == "P" :
                    if len(players[chosen_one].P) == 0 and len(players[chosen_one].Rocket) != 0:
                        card = card = Player_card(players[leader],"Rocket")
            else:
                card = Player_card(players[leader], color)
            desk[leader] = card
            print("Player " + players[leader].name + " played card: " + card + '\n')
            leader = (leader + 1) % num_players  # trun to next player
# end of part 2
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

        print("This round winner is player " + players[leader].name + '\n')
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
        print "Therefore Mission 46 Complete"

    else:
        if num_round == (40 / num_of_player + 1):
            print "Not even one task Completed, So Mission 46 fail"
            print "Remaining cards", judge_task
        else:
            # countine until as long as the game is not over
            # num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round46(players, leader, num_round, desk, judge_task, num_of_player)
# end of part 3
