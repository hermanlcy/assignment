import random
from mission1 import *

#mission 13's winning condition is really similar to mission9. Only difference is that all four rocket card has to win a round seperately. 
# Which mean people who has rocket card on hand will have the same task card accordingly
#things to implement next
# Mission 44
# first:
# we are restricting the player to dish out the rocket card when they are not running out of the resources on their hand at least in one color
# second:
# mission 44 is the harder version of mission 13, where we need to win 4 round in ascending order
# third
# we need 3 elements
# one -- remember all card on desk that is being played by all players
# two -- limiting the rocket dish out ability, only dish out the card when you run out of your resources (don't lead with rocket), rocket has to be dish out in asceding order 
# three -- check the rocket condition where if rocket condition is 0 then whoever get rocket one can wining a round if he meet the requirements

# mission13 test
total_used_card = []
# rocket_condition = 0
# used_rocket_card = []
def Player_round44(players, leader, num_round, desk, judge_task, num_of_player):
    used_rocket_card = []
    rocket_condition = 0
    Leader_color = ""
    print("------------------ Round %d " % (num_round) + "----------------------")
    num_round += 1
    num_players = len(players)
    players[leader].leader = False

# recording and sorting the leader's hand card based on the length of each color card on hand
    B_count = len(players[leader].B)  
    G_count = len(players[leader].G)  
    Y_count = len(players[leader].Y) 
    P_count = len(players[leader].P)

    all4_Color_dic = {'B': B_count, 'G': G_count, 'Y' : Y_count, 'P' : P_count}
    all4_Color_dic_sorted = [key for (key, value) in sorted(all4_Color_dic.items(), key=lambda key_value: key_value[1])]

    one = all4_Color_dic_sorted[0]
    two = all4_Color_dic_sorted[1]
    three = all4_Color_dic_sorted[2]
    four = all4_Color_dic_sorted[3]
# player 0
# this part did two thing for the round leader:
# first it let the leader judge it's own condition only through the card that is least on his or her hand
# second only dish out rocket card when he don't have anyother card on hand
    print("Player" , leader , "'s hand card : blue ", players[leader].B, "yellow", players[leader].Y, "green", players[leader].G, "pink", players[leader].P, "rocket", players[leader].Rocket)
    if  len(getattr(players[leader], str(one))) != 0: 
        card = Player_card13(players[leader], str(one))
        print("Player " + players[leader].name + " played card: " + card + '\n')
        total_used_card.append(card)
        desk[leader] = card
    elif  len(getattr(players[leader], str(two))) != 0:
        card = Player_card13(players[leader], str(two))
        print("Player " + players[leader].name + " played card: " + card + '\n')
        total_used_card.append(card)
        desk[leader] = card
    elif  len(getattr(players[leader], str(three))) != 0:
        card = Player_card13(players[leader], str(three))
        print("Player " + players[leader].name + " played card: " + card + '\n')
        total_used_card.append(card)
        desk[leader] = card
    elif  len(getattr(players[leader], str(four))) != 0:
        card = Player_card13(players[leader], str(four))
        print("Player " + players[leader].name + " played card: " + card + '\n')
        total_used_card.append(card)
        desk[leader] = card
    elif len(getattr(players[leader], str(one))) == 0 and len(getattr(players[leader], str(two))) == 0  and len(getattr(players[leader], str(three))) == 0  and len(getattr(players[leader], str(four))) == 0 :
        card = Player_card13(players[leader], "Rocket")
        print("Player " + players[leader].name + " played card: " + card + '\n')
        total_used_card.append(card)
        desk[leader] = card


# part 1 end in here

