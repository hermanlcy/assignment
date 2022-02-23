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

    # start of part 2
    for i in range(num_players - 1):  # player 1 & 2
        if leader == track + 1:
            second_card_thisRound = card

        if (second_card_thisRound == "P9" and players[leader].P == 0 and players[leader].Rocket != 0) or (second_card_thisRound == "B9" and players[leader].B == 0 and players[leader].Rocket != 0) or (second_card_thisRound == "P9" and players[leader].P == 0 and players[leader].Rocket != 0) or (second_card_thisRound == "P9" and players[leader].P == 0 and players[leader].Rocket != 0) :
            if "Rocket1" in players[leader].Rocket: # Second -- wining logic 
                card = "Rocket1"
                total_used_card[n] = card
                n = n + 1
                players[leader].Rocket.remove("Rocket1")
            elif "Rocket2" in players[leader].Rocket:
                card = "Rocket2"
                total_used_card[n] = card
                n = n + 1
                players[leader].Rocket.remove("Rocket2")
            elif "Rocket3" in players[leader].Rocket:
                card = "Rocket3"
                total_used_card[n] = card
                n = n + 1
                players[leader].Rocket.remove("Rocket3")
            elif "Rocket4" in players[leader].Rocket:
                card = "Rocket4"
                total_used_card[n] = card
                n = n + 1
                players[leader].Rocket.remove("Rocket4")
        elif color == 'P' and len(players[leader].P) == 0: # First: --wining logic: 
            if "B9" in players[leader].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[leader].B.remove(card)
            elif "Y9" in players[leader].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[leader].Y.remove(card)
            elif "G9" in players[leader].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[leader].G.remove(card)
        elif color == 'B' and len(players[leader].B) == 0:
            if "P9" in players[leader].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[leader].P.remove(card)
            elif "Y9" in players[leader].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[leader].Y.remove(card)
            elif "G9" in players[leader].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[leader].G.remove(card)
        elif color == 'G' and len(players[leader].G) == 0:
            if "P9" in players[leader].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[leader].P.remove(card)
            elif "Y9" in players[leader].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[leader].Y.remove(card)
            elif "B9" in players[leader].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[leader].B.remove(card)
        elif color == 'Y' and len(players[leader].Y) == 0:
            if "P9" in players[leader].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[leader].P.remove(card)
            elif "G9" in players[leader].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[leader].G.remove(card)
            elif "B9" in players[leader].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[leader].B.remove(card)
        else:
            card = play16(players[leader], color)
            desk[leader] = card
            total_used_card[i] = card
            i = i + 1

        print("Follower -- blue", players[leader].B, "yellow", players[leader].Y, "green", players[leader].G, "pink", players[leader].P, "rocket", players[leader].Rocket)
        print("Player " + players[leader].name + " played card: " + card + '\n')
        leader = (leader + 1) % num_players  # trun to next player


    winner = "x"
    flag = False 


    # end of part 2
    
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

    ## Task Completed checked, if task is completed it will be remove from judge_task
    for single_trick_card in players[leader].win_cards:
        for single_task_card in players[leader].task:
            if single_task_card == single_trick_card:
                print "Task", single_task_card, "Completed, Mission 17 continue\n" # Second -- loosing logic
                players[leader].task.remove(single_task_card)
                judge_task.remove(single_task_card)

    for single_trick_card in players[leader].win_cards:
        for single_task_card in players[leader].fail_task:
            if single_task_card == single_trick_card:
                print "Fail_Task", single_task_card, "Completed, Therefore Mission 17 failed\n" # Second -- loosing logic
                flag = True
                if flag == True:
                    exit(0)
                players[leader].fail_task.remove(single_task_card)
                fail_judge_task.remove(single_task_card)

    # print"####################################"

    if len(judge_task) == 0:
        print "Therefore Mission 17 finished"

    else:
        if flag == True:
            print "Mission 17 failed"
        if num_round == (40 / num_of_player + 1) and flag == False:
            print "Mission 17 failed"
            print "Remaining cards", judge_task
        else:
            # countine until as long as the game is not over
            num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round17(players, leader, num_round, desk,total_used_card, judge_task,fail_judge_task, num_of_player)


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