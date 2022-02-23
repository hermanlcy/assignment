
    # Task Completed checked, if task is completed it will be remove from judge_task
    for single_trick_card in players[round_leader_index].win_cards:
        for single_task_card in players[round_leader_index].task:
            if single_task_card == single_trick_card:
                print "Task", single_task_card, "Completed, Therefore Mission 16 failed\n" # Second -- loosing logic
                flag = True
                if flag == True:
                    exit(0)
                players[round_leader_index].task.remove(single_task_card)
                judge_task.remove(single_task_card)

    # print"####################################"

    if len(judge_task) == 0:
        print "Therefore Mission 13 Failed"

    else:
        if flag == True:
            print "Mission 16 failed"
        if num_round == (40 / num_of_player + 1) and flag == False:
            print "Mission 16 failed"
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
