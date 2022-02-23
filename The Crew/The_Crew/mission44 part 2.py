
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
