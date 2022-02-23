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



    leader = (leader + 1) % num_players  # trun to next player
    if len(card) > 2:
        color = "Rocket"
    else:
        color = card[0]

# this does one thing let the follower in the round
# only dish out rocket card based on the rocket condition, if they can they will try to win the round
    for i in range(num_players - 1):  # player 1 & 2
        print("Player" , leader , "'s hand card : blue ", players[leader].B, "yellow", players[leader].Y, "green", players[leader].G, "pink", players[leader].P, "rocket", players[leader].Rocket)
        card = Player_card(players[leader], color)
        total_used_card.append(card)
        desk[leader] = card
        print("Player " + players[leader].name + " played card: " + card + '\n')
        leader = (leader + 1) % num_players  # trun to next player

    # testing purpose just to print out all desk card
    for i in range(len(total_used_card)):
        print(total_used_card[i])

    correct_order = []
    temp = []
    judge_order = True
    # update the rocket condition
    for i in range(len(total_used_card)):
        if len(total_used_card[i]) > 2:
            temp.append(total_used_card[i])

    counter = 0

    for i in temp:
            counter = counter + 1

    if counter == 1:
        correct_order = ["Rocket1"]
        # if correct_order != temp:
        #     judge_order = False
    elif counter == 2:
        correct_order = ["Rocket1","Rocket2"]
        if correct_order != temp:
            judge_order = False
    elif counter == 3:
        correct_order = ["Rocket1","Rocket2","Rocket3"]
        if correct_order != temp:
            judge_order = False
    elif counter == 4:
        correct_order = ["Rocket1","Rocket2","Rocket3","Rocket4"]
        if correct_order != temp:
            judge_order = False
    
    # sort the card in asceding order
    temp.sort()

    if len(temp) != 0:
        sub_str = temp[-1]
    # print(temp) # testing
    if rocket_condition == 0 and len(temp) != 0:
        used_rocket_card = temp
        rocket_condition = sub_str[-1]
    if len(used_rocket_card) == 1 and len(temp) > len(used_rocket_card):
        used_rocket_card = temp
        rocket_condition = sub_str[-1]
    if len(used_rocket_card) == 2 and len(temp) > len(used_rocket_card):
        used_rocket_card = temp
        rocket_condition = sub_str[-1]
    if len(used_rocket_card) == 3 and len(temp) > len(used_rocket_card):
        used_rocket_card = temp
        rocket_condition = sub_str[-1]

    # correct_order = ["Rocket1","Rocket2","Rocket3","Rocket4"]


# part 2 end in here


    print(rocket_condition, "testing for rocket","\n")

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

    if len(judge_task) == 0 and judge_order == True:
        print "All mission completed in ascending order, Therefore Mission 44 Complete"
    elif len(judge_task) != 0 and judge_order == False:
        print "Not all mission completed, completed mission are in wrong order, Therefore Mission 44 failed"
    elif len(judge_task) == 0 and judge_order == False:
        print "All 4 four missions completed are in wrong order, Therefore Mission 44 failed"
    else:
        if num_round == (40 / num_of_player + 1):
            print "This is round 13, since Not All four missions are Completed, So Mission 44 failed"
            print "Remaining cards", judge_task
        else:
            # countine until as long as the game is not over
            num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round44(players, leader, num_round, desk, judge_task, num_of_player)

# part 3 end in here
