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



    # print ("track delte: ", track_delete)

    # remove the card from the copy's deck
    if str(round_leader_index) in Copy_hand:
        Copy_hand[str(round_leader_index)].remove(track_delete)
        # print(str(round_leader_index))
        # print(str(round_leader_index))

    print("Else -- blue", players[round_leader_index].B, "yellow", players[round_leader_index].Y, "green", players[round_leader_index].G, "pink", players[round_leader_index].P, "rocket", players[round_leader_index].Rocket)
    print("Player " + players[round_leader_index].name + " played card: " + card + '\n')
    desk[round_leader_index] = card
    total_used_card[n] = card
    n = n + 1

    
    # print (round_leader_index , "before")
    round_leader_index = (round_leader_index + 1) % num_players  # trun to next player

    track = round_leader_index
    # print (round_leader_index , "after")
    # print(card, "efefe")
    if len(card) > 2:
        # print(card, "efefe")
        color = "Rocket"
    else:
        color = card[0]

    for i in range(num_players - 1):  # player 1 & 2
        if round_leader_index == track + 1:
            second_card_thisRound = card

        if (second_card_thisRound == "P9" and players[round_leader_index].P == 0 and players[round_leader_index].Rocket != 0) or (second_card_thisRound == "B9" and players[round_leader_index].B == 0 and players[round_leader_index].Rocket != 0) or (second_card_thisRound == "P9" and players[round_leader_index].P == 0 and players[round_leader_index].Rocket != 0) or (second_card_thisRound == "P9" and players[round_leader_index].P == 0 and players[round_leader_index].Rocket != 0) :
            if "Rocket1" in players[round_leader_index].Rocket: # Second -- wining logic 
                card = "Rocket1"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Rocket.remove("Rocket1")
            elif "Rocket2" in players[round_leader_index].Rocket:
                card = "Rocket2"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Rocket.remove("Rocket2")
            elif "Rocket3" in players[round_leader_index].Rocket:
                card = "Rocket3"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Rocket.remove("Rocket3")
            elif "Rocket4" in players[round_leader_index].Rocket:
                card = "Rocket4"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Rocket.remove("Rocket4")
        elif color == 'P' and len(players[round_leader_index].P) == 0: # First: --wining logic: 
            if "B9" in players[round_leader_index].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].B.remove(card)
            elif "Y9" in players[round_leader_index].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Y.remove(card)
            elif "G9" in players[round_leader_index].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].G.remove(card)
        elif color == 'B' and len(players[round_leader_index].B) == 0:
            if "P9" in players[round_leader_index].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].P.remove(card)
            elif "Y9" in players[round_leader_index].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Y.remove(card)
            elif "G9" in players[round_leader_index].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].G.remove(card)
        elif color == 'G' and len(players[round_leader_index].G) == 0:
            if "P9" in players[round_leader_index].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].P.remove(card)
            elif "Y9" in players[round_leader_index].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Y.remove(card)
            elif "B9" in players[round_leader_index].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].B.remove(card)
        elif color == 'Y' and len(players[round_leader_index].Y) == 0:
            if "P9" in players[round_leader_index].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].P.remove(card)
            elif "G9" in players[round_leader_index].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].G.remove(card)
            elif "B9" in players[round_leader_index].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].B.remove(card)
        else:
            card = play16(players[round_leader_index], color)
            desk[round_leader_index] = card
            total_used_card[i] = card
            i = i + 1

        print("Follower -- blue", players[round_leader_index].B, "yellow", players[round_leader_index].Y, "green", players[round_leader_index].G, "pink", players[round_leader_index].P, "rocket", players[round_leader_index].Rocket)
        print("Player " + players[round_leader_index].name + " played card: " + card + '\n')
        round_leader_index = (round_leader_index + 1) % num_players  # trun to next player


    winner = "x"
    flag = False 

    for i in range(len(desk)):
        if len(desk[i]) > len(winner):
            winner = desk[i]
            round_leader_index = i
        elif len(desk[i]) == len(winner):
            if len(winner) > 2:
                if winner[-1] < desk[i][-1]:
                    winner = desk[i]
                    round_leader_index = i
            else:
                if desk[i][0] == color and winner[0] != color:
                    winner = desk[i]
                    round_leader_index = i
                elif desk[i][0] == color and winner[0] == color:
                    if desk[i][-1] > winner[-1]:
                        winner = desk[i]
                        round_leader_index = i

    players[round_leader_index].leader = True
    players[round_leader_index].win_cards += desk
    players[round_leader_index].win_cards.sort()

    print("This round winner is player " + players[round_leader_index].name + '\n')
    print("The won cards are: ")
    print(players[round_leader_index].win_cards)
    print

    # Task Completed checked, if task is completed it will be remove from judge_task
    for single_trick_card in players[round_leader_index].win_cards:
        for single_task_card in players[round_leader_index].task:
            if single_task_card == single_trick_card:
                print "Task", single_task_card, "Completed, Therefore Mission 16 faild\n" # Second -- loosing logic
                flag = True
                if flag == True:
                    exit(0)
                players[round_leader_index].task.remove(single_task_card)
                judge_task.remove(single_task_card)

    # print"####################################"

    if len(judge_task) == 0:
        print "Therefore Mission 13 Faild"

    else:
        if flag == True:
            print "Mission 16 faild"
        if num_round == (40 / num_of_player + 1) and flag == False:
            print "Mission 16 faild"
            print "Remaining cards", judge_task
        else:
            # countine until as long as the game is not over
            num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round16(players, round_leader_index, num_round, desk,total_used_card, judge_task, num_of_player)


def play16(player, color):
    card = ''
    if color == "Rocket":
        if len(player.Rocket) != 0:
            card = random.choice(player.Rocket)
            player.Rocket.remove(card)
        else:
            card = random_play16(player)
    elif color == 'B':
        if len(player.B) != 0:
            card = random.choice(player.B)
            player.B.remove(card)
        else:
            card = random_play16(player)
    elif color == 'Y':
        if len(player.Y) != 0:
            card = random.choice(player.Y)
            player.Y.remove(card)
        else:
            card = random_play16(player)
    elif color == 'G':
        if len(player.G) != 0:
            card = random.choice(player.G)
            player.G.remove(card)
        else:
            card = random_play16(player)
    elif color == 'P':
        if len(player.P) != 0:
            card = random.choice(player.P)
            player.P.remove(card)
        else:
            card = random_play16(player)
    else:
        card = random_play16(player)
    return card

# first reverse the state back to original then implement the tracking variable 
def random_play16(player): # this function adding all missing 9 back
    if "B9" in player.B and "B9" in player.task and len(player.B) >= 2:
        player.B = player.B[:-1]
    if "G9" in player.G and "G9" in player.task and len(player.G) >= 2:
        player.G = player.G[:-1]
    if "P9" in player.P and "P9" in player.task and len(player.P) >= 2:
        player.P = player.P[:-1]
    if "Y9" in player.Y and "Y9" in player.task and len(player.Y) >= 2:
        player.Y = player.Y[:-1]

    cards = player.B + player.Y + player.G + player.P +player.Rocket
    card = random.choice(cards)

    if card[0] == 'P':
        player.P.remove(card)
    elif card[0] == 'G':
        player.G.remove(card)
    elif card[0] == 'Y':
        player.Y.remove(card)
    elif card[0] == 'B':
        player.B.remove(card)
    else:
        player.Rocket.remove(card)
    return card