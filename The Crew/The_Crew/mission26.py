from mission1 import *

exclude_list = ["B1", "Y1", "G1", "P1"]  # don't dish out these cards unless unavoidable

def Player_round26(players, leader, num_round, desk, judge_task, num_of_player, communicated):
    mission = 26
    print("------------------ Round %d " % (num_round) + "----------------------")

    counterY = 8
    counterG = 8
    counterP = 8
    counterB = 8
    counterR = 4

    if num_round == 1:  # this if condition only work for the first round to eliminate the rocket cards as much as possible

        num_round = num_round + 1
        num_players = len(players)
        players[leader].leader = False
        if counterY == 0 and counterR == 0 and players[leader].task == "Y1":
            card = Player_card(players[leader], "Y")
        elif counterG == 0 and counterR == 0 and players[leader].task == "G1":
           card = Player_card(players[leader], "G")
        elif counterP == 0 and counterR == 0 and players[leader].task == "P1":
            card = Player_card(players[leader], "P")
        elif counterB == 0 and counterR == 0 and players[leader].task == "B1":
            card = Player_card(players[leader], "B")
        else:
            #card = Player_card(players[leader], "Rocket")
            card = dish_player_card_excluding(players[leader], "Rocket", exclude_list)

        print("\nPlayer " + players[leader].name + " played card: " + card)
        if communicated < num_of_player:
            communicated = communicating(players[leader], mission, num_round, communicated)
        if card in players[leader].communication:
            players[leader].communication = ""
        elif players[leader].communication is not "":
            print("Player " + players[leader].name + " communicating: " + players[leader].communication)

        if card[0] == 'Y':
            counterY = counterY - 1
        elif card[0] == 'G':
            counterG = counterG - 1
        elif card[0] == 'P':
            counterP = counterP - 1
        elif card[0] == 'B':
            counterB = counterB - 1
        else:
            counterR = counterR - 1

        desk[leader] = card
        leader = (leader + 1) % num_players  # trun to next player

        if len(card) > 2:
            color = "Rocket"
        else:
            color = card[0]

        for i in range(num_players - 1):
            #card = Player_card(players[leader], color)
            card = dish_player_card_excluding(players[leader], color, exclude_list)
            players[leader].print_detail()
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
        print(players[leader].win_cards)
        print

    else:
        # start from round 2 here

        num_round += 1

        num_players = len(players)
        players[leader].leader = False

        if counterY == 0 and counterR == 0 and players[leader].task == "Y1":
            card = Player_card(players[leader], "Y")
        elif counterG == 0 and counterR == 0 and players[leader].task == "G1":
            card = Player_card(players[leader], "G")
        elif counterP == 0 and counterR == 0 and players[leader].task == "P1":
            card = Player_card(players[leader], "P")
        elif counterB == 0 and counterR == 0 and players[leader].task == "B1":
            card = Player_card(players[leader], "B")
        else:
            #card = dish_player_card_excluding(players[leader], "random", exclude_list)
            #card = Player_card(players[leader], "random")
            card = dish_player_card_excluding(players[leader], "random", exclude_list)
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
            #card = Player_card(players[leader], color)
            card = dish_player_card_excluding(players[leader], color, exclude_list)
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
        print(players[leader].win_cards)
        print()

    # Task Completed checked, if task is completed it will be remove from judge_task
    for single_trick_card in players[leader].win_cards:
        for single_task_card in players[leader].task:
            if single_task_card == single_trick_card:
                print "Task", single_task_card, "Completed"
                players[leader].task.remove(single_task_card)
                judge_task.remove(single_task_card)


    if len(judge_task) != 4:
        print "Therefore 26 Complete"

    else:
        if num_round == (40 / num_of_player + 1):
            print "Not even one task Completed, So Mission 26 fail"
            print "Remaining cards", judge_task
        else:
            # countine until as long as the game is not over
            num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round26(players, leader, num_round, desk, judge_task, num_of_player, communicated)

    if card[0] == 'Y':
        counterY = counterY - 1
    elif card[0] == 'G':
        counterG = counterG - 1
    elif card[0] == 'P':
        counterP = counterP - 1
    elif card[0] == 'B':
        counterB = counterB - 1
    else:
        counterR = counterR - 1


def dish_player_card_excluding(player, color, exclude_list):
    card = ''
    excluded_cards = []
    # temporarily remove the cards to be excluded while choosing from the player's cards
    for i in range(len(exclude_list)):
        excluded_card = exclude_list[i]
        excluded_cards.append(excluded_card)
        if excluded_card in player.Rocket:
            all_cards = player.Rocket + player.B + player.Y + player.G + player.P
            if len(all_cards) > 1:
                player.Rocket.remove(excluded_card)

        elif excluded_card in player.B:
            all_cards = player.Rocket + player.B + player.Y + player.G + player.P
            if len(all_cards) > 1:
                player.B.remove(excluded_card)
        elif excluded_card in player.Y:
            all_cards = player.Rocket + player.B + player.Y + player.G + player.P
            if len(all_cards) > 1:
                player.Y.remove(excluded_card)
        elif excluded_card in player.G:
            all_cards = player.Rocket + player.B + player.Y + player.G + player.P
            if len(all_cards) > 1:
                player.G.remove(excluded_card)
        elif excluded_card in player.P:
            all_cards = player.Rocket + player.B + player.Y + player.G + player.P
            if len(all_cards) > 1:
                player.P.remove(excluded_card)
        else:
            #print("player has no such card")
            if excluded_card in excluded_cards:
                excluded_cards.remove(excluded_card)
    if color == "Rocket":
        if len(player.Rocket) != 0:
            card = random.choice(player.Rocket)
            player.Rocket.remove(card)
        else:
            card = Random_play(player)
    elif color == 'B':
        if len(player.B) != 0:
            card = random.choice(player.B)
            player.B.remove(card)
        else:
            card = Random_play(player)
    elif color == 'Y':
        if len(player.Y) != 0:
            card = random.choice(player.Y)
            player.Y.remove(card)
        else:
            card = Random_play(player)
    elif color == 'G':
        if len(player.G) != 0:
            card = random.choice(player.G)
            player.G.remove(card)
        else:
            card = Random_play(player)
    elif color == 'P':
        if len(player.P) != 0:
            card = random.choice(player.P)
            player.P.remove(card)
        else:
            card = Random_play(player)
    else:
        card = Random_play(player)

    # add the card back to the player's cards
    for i in range(len(excluded_cards)):
        excluded_card = excluded_cards[i]
        if excluded_card[0] == 'R':
            player.Rocket.append(excluded_card)
            player.Rocket.sort()
        elif excluded_card[0] == 'B':
            player.B.append(excluded_card)
            player.B.sort()
        elif excluded_card[0] == 'Y':
            player.Y.append(excluded_card)
            player.Y.sort()
        elif excluded_card[0] == 'G':
            player.G.append(excluded_card)
            player.G.sort()
        elif excluded_card[0] == 'P':
            player.P.append(excluded_card)
            player.P.sort()
        else:
            print()
            #print("invalid card")
    return card
