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

# mission13 test

def Player_round16(players, round_leader_index, num_round, desk,total_used_card, judge_task, num_of_player):

    # if num_of_player == 2:
    #     Copy_origin_0 = players[0].B + players[0].Y + players[0].G + players[0].P +players[0].Rocket
    #     name_0 = "Copy_origin_0"
    #     Copy_origin_1 = players[1].B + players[1].Y + players[1].G + players[1].P +players[1].Rocket
    #     name_1 = "Copy_origin_0"
    # if num_of_player == 3:
    #     Copy_origin_0 = players[0].B + players[0].Y + players[0].G + players[0].P +players[0].Rocket
    #     Copy_origin_1 = players[1].B + players[1].Y + players[1].G + players[1].P +players[1].Rocket
    #     Copy_origin_2 = players[2].B + players[2].Y + players[2].G + players[2].P +players[2].Rocket
    # if num_of_player == 4:
    #     Copy_origin_0 = players[0].B + players[0].Y + players[0].G + players[0].P +players[0].Rocket
    #     Copy_origin_1 = players[1].B + players[1].Y + players[1].G + players[1].P +players[1].Rocket
    #     Copy_origin_2 = players[2].B + players[2].Y + players[2].G + players[2].P +players[2].Rocket
    #     Copy_origin_3 = players[3].B + players[3].Y + players[3].G + players[3].P +players[3].Rocket
    # if num_of_player == 5:
    #     Copy_origin_0 = players[0].B + players[0].Y + players[0].G + players[0].P +players[0].Rocket
    #     Copy_origin_1 = players[1].B + players[1].Y + players[1].G + players[1].P +players[1].Rocket
    #     Copy_origin_2 = players[2].B + players[2].Y + players[2].G + players[2].P +players[2].Rocket
    #     Copy_origin_3 = players[3].B + players[3].Y + players[3].G + players[3].P +players[3].Rocket
    #     Copy_origin_4 = players[4].B + players[4].Y + players[4].G + players[4].P +players[4].Rocket

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
    players[round_leader_index].leader = False

    # if len(players[leader].B) != 0 or len(players[leader].G) != 0 or len(players[leader].Y) != 0 or len(players[leader].P) != 0:
 
    card = play16(players[round_leader_index], "random")
    if "P9" in players[round_leader_index].task and "P9" not in players[round_leader_index].P and "P9" not in total_used_card:
            players[round_leader_index].P.append("P9")
    if "B9" in players[round_leader_index].task and "B9" not in players[round_leader_index].B and "B9" not in total_used_card:
        players[round_leader_index].B.append("B9")
    if "Y9" in players[round_leader_index].task and "Y9" not in players[round_leader_index].Y and "Y9" not in total_used_card:
        players[round_leader_index].Y.append("Y9")
    if "G9" in players[round_leader_index].task and "G9" not in players[round_leader_index].G and "P9" not in total_used_card:
        players[round_leader_index].G.append("G9")
        
    track_delete = card # copy the card has beeing played by the leader
    total_used_card[n] = card


    # end of part 1
