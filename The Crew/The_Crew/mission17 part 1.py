import random
from mission1 import *

# mission16 is about not winning any round with any of the 9
# Zero: -- wining logic : 
# If leader has 9 on hand never use 9 as leading card (already implemented) 
# First: --wining logic: 
# If we dont' have matching card to leading suit color then we dish out the 9 on hand that not in the leading suit 
# Second:
# -- losing judgement: If we only have 9 in the leading suit specifically 9 can't be the leading card
# , if 9 is the leading card then we lose the mission (then stop the whole mission) 
# -- winning logic : unless someone has a rocket and able to use that rocket then mission keep going 
# Random_play function ask the player to give a card randomly, it will also be remove in the player class
# Player_card function ask the player to give a card based on the color condition
# Player_card function ask the player to give a card based on the color condition
# logic for mission 17:
# if we have overlap on task and fail_task then we automatically fail the mission
# mission13 test

def Player_round17(players, leader, num_round, desk,total_used_card, judge_task, fail_judge_task, num_of_player):

    for single_trick_card in fail_judge_task:
        for single_task_card in judge_task:
            if single_task_card == single_trick_card:
                print "Task we are picking is impossible to finish", single_task_card, "Therefore Mission 17 failed\n" # Second -- loosing logic
                flag_one = True
                if flag_one == True:
                    exit(0)

    # copy's each's round's leader's hand card into a seperate list (dictionary is the array of list)
    Copy_hand = {} 
    for i in range(num_of_player):
        Copy_hand[str(i)] = players[i].B + players[i].Y + players[i].G + players[i].P +players[i].Rocket
    Copy_hand
    print(Copy_hand)

    track_delete = ""
    
    n = 0
    leader_card_thisRound = ""
    second_card_thisRound = ""
    # Leader_color = ""
    print("------------------ Round %d " % (num_round) + "----------------------")
    num_round += 1
    num_players = len(players)
    players[leader].leader = False

    # if len(players[leader].B) != 0 or len(players[leader].G) != 0 or len(players[leader].Y) != 0 or len(players[leader].P) != 0:
 
    card = play16(players[leader], "random")
    if "P9" in players[leader].task and "P9" not in players[leader].P and "P9" not in total_used_card:
            players[leader].P.append("P9")
    if "B9" in players[leader].task and "B9" not in players[leader].B and "B9" not in total_used_card:
        players[leader].B.append("B9")
    if "Y9" in players[leader].task and "Y9" not in players[leader].Y and "Y9" not in total_used_card:
        players[leader].Y.append("Y9")
    if "G9" in players[leader].task and "G9" not in players[leader].G and "P9" not in total_used_card:
        players[leader].G.append("G9")
        
    track_delete = card # copy the card has beeing played by the leader
    total_used_card[n] = card

    # print ("track delte: ", track_delete)

    # remove the card from the copy's deck
    if str(leader) in Copy_hand:
        Copy_hand[str(leader)].remove(track_delete)
        # print(str(round_leader_index))
        # print(str(round_leader_index))

    print("Else -- blue", players[leader].B, "yellow", players[leader].Y, "green", players[leader].G, "pink", players[leader].P, "rocket", players[leader].Rocket)
    print("Player " + players[leader].name + " played card: " + card + '\n')
    desk[leader] = card
    total_used_card[n] = card
    n = n + 1

    
    # print (round_leader_index , "before")
    leader = (leader + 1) % num_players  # trun to next player

    track = leader
    # print (round_leader_index , "after")
    # print(card, "efefe")
    if len(card) > 2:
        # print(card, "efefe")
        color = "Rocket"
    else:
        color = card[0]

    