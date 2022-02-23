from mission1 import *
from mission5 import *
import copy

# get the biggest card (without Rocket)
# if this player has more than one biggest cards, 
# choose one of them
def get_biggest_nr_card(player):
    biggest_nr_card = ""
    biggest_point = -1
    card_pos = -2
    card = ""

    if player.Y and int(player.Y[-1][-1]) > biggest_point:
        if len(player.Y) == 1:
            biggest_nr_card = "The only Y card " + player.Y[-1]
            card_pos = 0
        else:
            biggest_nr_card = "Largest Y card " + player.Y[-1]
            card_pos = 1
        
        card = player.Y[-1]
        biggest_point = int(player.Y[-1][-1])

    if player.G and int(player.G[-1][-1]) > biggest_point:
        if len(player.G) == 1:
            biggest_nr_card = "The only G card " + player.G[-1]
            card_pos = 0
        else:
            biggest_nr_card = "Largest G card " + player.G[-1]
            card_pos = 1

        card = player.G[-1]
        biggest_point = int(player.G[-1][-1])

    if player.B and int(player.B[-1][-1]) > biggest_point:
        if len(player.B) == 1:
            biggest_nr_card = "The only B card " + player.B[-1]
            card_pos = 0
        else:
            biggest_nr_card = "Largest B card " + player.B[-1]
            card_pos = 1
        
        card = player.B[-1]
        biggest_point = int(player.B[-1][-1])

    if player.P and int(player.P[-1][-1]) > biggest_point:
        if len(player.P) == 1:
            biggest_nr_card = "The only P card " + player.P[-1]
            card_pos = 0
        else:
            biggest_nr_card = "Largest P card " + player.P[-1]
            card_pos = 1
        
        card = player.P[-1]
        biggest_point = int(player.P[-1][-1])
    
    return biggest_nr_card, card, card_pos

# decide volunteer method
def decide_volunteer(players):
    count_list = []
    # if a player has no Rocket and has only one 9-point card, he/she should be the volunteer
    # capitan should not be the volunteer
    for i in players:
        # 9-point card
        count = 0

        # calculate count
        if i.Y and int(i.Y[-1][-1]) == 9:
            count = count + 1
        if i.B and int(i.B[-1][-1]) == 9:
            count = count + 1
        if i.G and int(i.G[-1][-1]) == 9:
            count = count + 1
        if i.P and int(i.P[-1][-1]) == 9:
            count = count + 1
        if i.Rocket:
            count = -1
        
        count_list.append(count)

    # get the value of how many count the value is one
    value_one_count = 0

    for i in count_list:
        if i == 1:
            value_one_count = value_one_count + 1

    # judge if value_one_count == 0 / 1 / > 1
    if value_one_count == 1:
        volunteer_index = -1

        for i in range(len(players)):
            # print result
            if count_list[i] == 1:
                print "Player", players[i].name, ":", "Yes"
                players[i].volunteer = True
                c, cc, ccp = get_biggest_nr_card(players[i])
                players[i].communication = c
                players[i].communication_card = cc
                players[i].communication_card_pos = ccp
                volunteer_index = i
            else:
                print "Player", players[i].name, ":", "No"
        
        print "Capiton: Only one player chooses to be the volunteer. Player", volunteer_index, "is the volunteer\n"
        return int(players[i].name)

    if value_one_count == 0:
        temp = players[:]
        
        for i in temp:
            if i.captain:
                temp.remove(i)
        
        length = len(temp)
        player = temp[random.choice(range(length))]
        player.volunteer = True
        c, cc, ccp = get_biggest_nr_card(player)
        player.communication = c
        player.communication_card = cc
        player.communication_card_pos = ccp
        print "Capiton: No player choose to be the volunteer. I choose player", player.name, "as the volunteer\n"

        return int(player.name)

    temp = []

    for i in range(len(players)):
        if count_list[i] == 1:
            temp.append(players[i])
    
    length = len(temp)
    player = temp[random.choice(range(length))]
    player.volunteer = True
    c, cc, ccp = get_biggest_nr_card(player)
    player.communication = c
    player.communication_card = cc
    player.communication_card_pos = ccp
    print "Capiton: More than one players choose to be the volunteer. I choose player", player.name, "as the volunteer\n"

    return int(player.name)


# Player_card function ask the player to give a card based on the color condition
def Player_card(player, color):
    card = ''
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
    return card

# get volunteer's communication beacon
def get_volunteer_communication_beacon(players):
    for i in players:
        if i.volunteer == True:
            return i.communication_card
    
    return "No volunteer"

# choose a card a little bit greater than current card
# if not have current color, play Rocket card
def Greater_min_play_certain_color(player, color, given_card):
    card = ''

    if color == 'B':
        if player.B:
            card = player.B[-1]
            for i in range(len(player.B)):
                if int(player.B[i][-1]) > int(given_card[-1]):
                    card = player.B[i]
                    break
                else:
                    # cannot win, so just play the minimum card in this color
                    card = player.B[0]

            player.B.remove(card)
        else:
            card = Min_play_Rocket_First(player)
    elif color == 'G':
        if player.G:
            card = player.G[-1]
            for i in range(len(player.G)):
                if int(player.G[i][-1]) > int(given_card[-1]):
                    card = player.G[i]
                    break
                else:
                    # cannot win, so just play the minimum card in this color
                    card = player.G[0]
                    
            player.G.remove(card)
        else:
            card = Min_play_Rocket_First(player)
    elif color == 'P':
        if player.P:
            card = player.P[-1]
            for i in range(len(player.P)):
                if int(player.P[i][-1]) > int(given_card[-1]):
                    card = player.P[i]
                    break
                else:
                    # cannot win, so just play the minimum card in this color
                    card = player.P[0]
                    
            player.P.remove(card)
        else:
            card = Min_play_Rocket_First(player)
    elif color == 'Y':
        if player.Y:
            card = player.Y[-1]
            for i in range(len(player.Y)):
                if int(player.Y[i][-1]) > int(given_card[-1]):
                    card = player.Y[i]
                    break
                else:
                    # cannot win, so just play the minimum card in this color
                    card = player.Y[0]
                    
            player.Y.remove(card)
        else:
            card = Min_play_Rocket_First(player)
    else:
        if player.Rocket:
            defeat_volunteer = False
            card = player.Rocket[-1]
            for i in range(len(player.Rocket)):
                if int(player.Rocket[i][-1]) > int(given_card[-1]):
                    card = player.Rocket[i]
                    defeat_volunteer = True
                    break
            
            if defeat_volunteer == True:
                player.Rocket.remove(card)
            else:
                card = Min_play_Rocket_First(player)
        else:
            if color == 'B':
                if player.B:
                    card = Min_play_certain_color(player, 'B')
                else:
                    card = Min_play(player)
            elif color == 'G':
                if player.G:
                    card = Min_play_certain_color(player, 'G')
                else:
                    card = Min_play(player)
            elif color == 'P':
                if player.P:
                    card = Min_play_certain_color(player, 'P')
                else:
                    card = Min_play(player)
            else:
                if player.Y:
                    card = Min_play_certain_color(player, 'Y')
                else:
                    card = Min_play(player)

    return card

# choose a card a little bit greater than current card
# if not have current color, play Rocket card
def Less_max_play_certain_color(player, color, given_card):
    card = ''

    if color == 'B':
        if player.B:
            card = player.B[0]
            for i in range(len(player.B)):
                if int(player.B[i][-1]) < int(given_card[-1]):
                    card = player.B[i]
                    break
                else:
                    # cannot win, so just play the maximum card in this color
                    card = player.B[-1]

            player.B.remove(card)
        else:
            card = Min_play_Rocket_First(player)
    elif color == 'G':
        if player.G:
            card = player.G[0]
            for i in range(len(player.G)):
                if int(player.G[i][-1]) < int(given_card[-1]):
                    card = player.G[i]
                    break
                else:
                    # cannot win, so just play the minimum card in this color
                    card = player.G[-1]
                    
            player.G.remove(card)
        else:
            card = Min_play_Rocket_First(player)
    elif color == 'P':
        if player.P:
            card = player.P[0]
            for i in range(len(player.P)):
                if int(player.P[i][-1]) < int(given_card[-1]):
                    card = player.P[i]
                    break
                else:
                    # cannot win, so just play the minimum card in this color
                    card = player.P[-1]
                    
            player.P.remove(card)
        else:
            card = Min_play_Rocket_First(player)
    elif color == 'Y':
        if player.Y:
            card = player.Y[0]
            for i in range(len(player.Y)):
                if int(player.Y[i][-1]) < int(given_card[-1]):
                    card = player.Y[i]
                    break
                else:
                    # cannot win, so just play the minimum card in this color
                    card = player.Y[-1]
                    
            player.Y.remove(card)
        else:
            card = Min_play_Rocket_First(player)
    else:
        if player.Rocket:
            defeat_volunteer = False
            card = player.Rocket[0]
            for i in range(len(player.Rocket)):
                if int(player.Rocket[i][-1]) < int(given_card[-1]):
                    card = player.Rocket[i]
                    defeat_volunteer = True
                    break
            
            if defeat_volunteer == True:
                player.Rocket.remove(card)
            else:
                card = Min_play_Rocket_First(player)
        else:
            if color == 'B':
                if player.B:
                    card = Max_play_certain_color(player, 'B')
                else:
                    card = Max_play(player)
            elif color == 'G':
                if player.G:
                    card = Max_play_certain_color(player, 'G')
                else:
                    card = Max_play(player)
            elif color == 'P':
                if player.P:
                    card = Max_play_certain_color(player, 'P')
                else:
                    card = Max_play(player)
            else:
                if player.Y:
                    card = Max_play_certain_color(player, 'Y')
                else:
                    card = Max_play(player)

    return card


# player the biggest card in a color (without Rocket)
def Max_play_certain_color(player, color):
    card = ''

    if color == 'B':
        card = player.B[-1]
        player.B.remove(card)
    elif color == 'Y':
        card = player.Y[-1]
        player.Y.remove(card)
    elif color == 'P':
        card = player.P[-1]
        player.P.remove(card)
    else:
        card = player.G[-1]
        player.G.remove(card)

    return card

#used for tried to not play certain color card.
def Min_no_play_cartain_color(player, color):
    card = ''
    cards = []

    if color == 'B':
        cards = player.Y + player.G + player.P
    elif color == 'Y':
        cards = player.B + player.G + player.P
    elif color == 'G':
        cards = player.Y + player.B + player.P
    elif color == 'P':
        cards = player.Y + player.G + player.B
    
    if cards:
        card = random.choice(cards)

        if card[0] == 'B':
            player.B.remove(card)
        elif card[0] == 'Y':
            player.Y.remove(card)
        elif card[0] == 'P':
            player.P.remove(card)
        elif card[0] == 'G':
            player.G.remove(card)
    else:
        if color == 'B' and player.B:
            card = player.B[0]
            player.B.remove(card)
        elif color == 'Y' and player.Y:
            card = player.Y[0]
            player.Y.remove(card)
        elif color == 'P' and player.P:
            card = player.P[0]
            player.P.remove(card)
        elif color == 'G' and player.G:
            card = player.G[0]
            player.G.remove(card)
        else:
            card = player.Rocket[0]
            player.Rocket.remove(card)

    return card

def get_current_winner_and_card(cards_played_in_this_round, current_player_id_list):
    winner_index = -1
    current_player_id_list_index = -1
    card = ""

    for i in range(len(current_player_id_list)):
        if i == 0:
            winner_index = current_player_id_list[0]
            card = cards_played_in_this_round[0]
            current_player_id_list_index = 0
        else:
            if len(cards_played_in_this_round[current_player_id_list_index]) == 2:
                # rocket
                if len(cards_played_in_this_round[i]) > 2:
                    winner_index = current_player_id_list[i]
                    card = cards_played_in_this_round[i]
                    current_player_id_list_index = i
                elif cards_played_in_this_round[current_player_id_list_index][0] == cards_played_in_this_round[i][0]:
                    if int(cards_played_in_this_round[current_player_id_list_index][1]) < int(cards_played_in_this_round[i][1]):
                        winner_index = current_player_id_list[i]
                        card = cards_played_in_this_round[i]
                        current_player_id_list_index = i
            else:
                if len(cards_played_in_this_round[i]) > 2:
                    if int(cards_played_in_this_round[current_player_id_list_index][-1]) < int(cards_played_in_this_round[i][-1]):
                        winner_index = current_player_id_list[i]
                        card = cards_played_in_this_round[i]
                        current_player_id_list_index = i

    return winner_index, card

#used for healthy player to choose the Rocket card. If the healthy player does not have rocket card, he/she should play the card with the smallest value
def Max_play_Rocket_First(player):
    cards = player.Rocket
    card = ""
    point = -1
    if len(cards) != 0:
        card = cards[0]
        
    else:
        cards = player.B + player.Y + player.G + player.P
        card = cards[0]

        for i in cards:
            if int(i[-1]) > int(card[-1]):
                card = i

    if len(card) > 2:
        player.Rocket.remove(card)
    elif card[0] == 'P':
        player.P.remove(card)
    elif card[0] == 'G':
        player.G.remove(card)
    elif card[0] == 'Y':
        player.Y.remove(card)
    else:
        player.B.remove(card)
    
    return card

# the first round of the game let the volunteer win, 
# then let the volunteer loss
# capiton cannot be the volunteer (Rocket 4 must win)
# if the volunteer loss more than 1 round, game failed
def Player_round33(players, current_player_id, num_round, desk, communicated, volunteer_index):
    print("------------------ Round %d " % (num_round) + "----------------------")
    num_round += 1
    card = ""
    volunteer_communication_beacon = get_volunteer_communication_beacon(players)
    # record if volunteer played card
    volunteer_played = False
    cards_played_in_this_round = []
    current_player_id_list = []

    players[current_player_id].leader = False

    # lost this game
    if players[current_player_id].volunteer == False and players[current_player_id].wintime == 0:
        if len(volunteer_communication_beacon) == 2:
            if volunteer_communication_beacon[0] == 'B':
                if players[current_player_id].B and int(volunteer_communication_beacon[1]) > int(players[current_player_id].B[0][1]):
                    card = Min_play_certain_color(players[current_player_id], 'B')
                else:
                    card = Min_no_play_cartain_color(players[current_player_id], 'B')
            elif volunteer_communication_beacon[0] == 'Y':
                if players[current_player_id].Y and int(volunteer_communication_beacon[1]) > int(players[current_player_id].Y[0][1]):
                    card = Min_play_certain_color(players[current_player_id], 'Y')
                else:
                    card = Min_no_play_cartain_color(players[current_player_id], 'Y')
            elif volunteer_communication_beacon[0] == 'G':
                if players[current_player_id].G and int(volunteer_communication_beacon[1]) > int(players[current_player_id].G[0][1]):
                    card = Min_play_certain_color(players[current_player_id], 'G')
                else:
                    card = Min_no_play_cartain_color(players[current_player_id], 'G')
            else:
                if players[current_player_id].P and int(volunteer_communication_beacon[1]) > int(players[current_player_id].P[0][1]):
                    card = Min_play_certain_color(players[current_player_id], 'P')
                else:
                    card = Min_no_play_cartain_color(players[current_player_id], 'P')
        else:
            card = Min_play(players[current_player_id])
    elif players[current_player_id].volunteer == True and players[current_player_id].wintime == 0:
        if len(players[current_player_id].communication_card) == 2:
            card = players[current_player_id].communication_card

            if card[0] == 'P':
                players[current_player_id].P.remove(card)
            elif card[0] == 'G':
                players[current_player_id].G.remove(card)
            elif card[0] == 'Y':
                players[current_player_id].Y.remove(card)
            elif card[0] == 'B':
                players[current_player_id].B.remove(card)
        else:
            card = Max_play(players[current_player_id])
    else:
        card = Player_card(players[current_player_id], "random")
    
    cards_played_in_this_round.append(card)
    current_player_id_list.append(current_player_id)
    
    if current_player_id == volunteer_index:
        volunteer_played = True
    
    current_winner_id = current_player_id

    # card = Player_card(players[current_player_id], "random")

    print("Player " + players[current_player_id].name + " played card: " + card)

    if communicated < len(players):
        communicated = communicating(players[current_player_id], 33, num_round, communicated)
    if card in players[current_player_id].communication:
        players[current_player_id].communication = ""
        players[current_player_id].communication_card = ""
        players[current_player_id].communication_card_pos = -2
    elif players[current_player_id].communication is not "":
        print("Player " + players[current_player_id].name + " communicating: " + players[current_player_id].communication)

    desk[current_player_id] = card
    current_player_id = (current_player_id + 1) % len(players)  # trun to next player

    # leader is not the actual leader in here. It's just an i variable to 
    # represent the who has the next turn to play the card

    if len(card) > 2:
        color = "Rocket" #color here is fixed based on the round leader so no issue here
    else:
        color = card[0]
    
    color0 = color

    for i in range(len(players) - 1):
        # card = Player_card(players[current_player_id], color)
        if players[current_player_id].volunteer == True and players[volunteer_index].wintime == 1:
            if volunteer_played and winner_index == volunteer_index:
                card = Less_max_play_certain_color(players[current_player_id], color0, win_card)

        elif players[current_player_id].volunteer == False and players[volunteer_index].wintime == 0:
            if color == 'B':
                if players[current_player_id].B:
                    card = Min_play_certain_color(players[current_player_id], 'B')
                else:
                    card = Min_play(players[current_player_id])
            elif color == 'G':
                if players[current_player_id].G:
                    card = Min_play_certain_color(players[current_player_id], 'G')
                else:
                    card = Min_play(players[current_player_id])
            elif color == 'P':
                if players[current_player_id].P:
                    card = Min_play_certain_color(players[current_player_id], 'P')
                else:
                    card = Min_play(players[current_player_id])
            elif color == 'Y':
                if players[current_player_id].Y:
                    card = Min_play_certain_color(players[current_player_id], 'Y')
                else:
                    card = Min_play(players[current_player_id])
            else:
                card = Min_play_Rocket_First(players[current_player_id])
        elif players[current_player_id].volunteer == True and players[volunteer_index].wintime == 0:
            if color == 'B':
                if players[current_player_id].B:
                    card = Max_play_certain_color(players[current_player_id], 'B')
                else:
                    # cannot win, so play a min card of other color
                    card = Min_play(players[current_player_id])
            elif color == 'G':
                if players[current_player_id].G:
                    card = Max_play_certain_color(players[current_player_id], 'G')
                else:
                    # cannot win, so play a min card of other color
                    card = Min_play(players[current_player_id])
            elif color == 'P':
                if players[current_player_id].P:
                    card = Max_play_certain_color(players[current_player_id], 'P')
                else:
                    # cannot win, so play a min card of other color
                    card = Min_play(players[current_player_id])
            elif color == 'Y':
                if players[current_player_id].Y:
                    card = Max_play_certain_color(players[current_player_id], 'Y')
                else:
                    # cannot win, so play a min card of other color
                    card = Min_play(players[current_player_id])
            else:
                card = Min_play_Rocket_First(players[current_player_id])
        elif players[current_player_id].volunteer == False and players[volunteer_index].wintime == 1:
            winner_index, win_card = get_current_winner_and_card(cards_played_in_this_round, current_player_id_list)

            if volunteer_played and winner_index == volunteer_index:
                card = Greater_min_play_certain_color(players[current_player_id], color0, win_card)
            elif volunteer_played and winner_index != volunteer_index:
                if color == 'B':
                    if players[current_player_id].B:
                        card = Min_play_certain_color(players[current_player_id], 'B')
                    else:
                        card = Min_play(players[current_player_id])
                elif color == 'G':
                    if players[current_player_id].G:
                        card = Min_play_certain_color(players[current_player_id], 'G')
                    else:
                        card = Min_play(players[current_player_id])
                elif color == 'P':
                    if players[current_player_id].P:
                        card = Min_play_certain_color(players[current_player_id], 'P')
                    else:
                        card = Min_play(players[current_player_id])
                elif color == 'Y':
                    if players[current_player_id].Y:
                        card = Min_play_certain_color(players[current_player_id], 'Y')
                    else:
                        card = Min_play(players[current_player_id])
                else:
                    card = Min_play_Rocket_First(players[current_player_id])
            else:
                card = Player_card(players[current_player_id], color)
        
        if current_player_id == volunteer_index:
            volunteer_played = True
        
        if len(color) > 2:
            color = "Rocket"

        desk[current_player_id] = card
        cards_played_in_this_round.append(card)
        current_player_id_list.append(current_player_id)
        print("Player " + players[current_player_id].name + " played card: " + card)
        if communicated < len(players):
            communicated = communicating(players[current_player_id], 33, num_round, communicated)
        if card in players[current_player_id].communication:
            players[current_player_id].communication = ""
            players[current_player_id].communication_card = ""
            players[current_player_id].communication_card_pos = -2
        elif players[current_player_id].communication is not "":
            print("Player " + players[current_player_id].name + " communicating: " + players[current_player_id].communication)

        current_player_id = (current_player_id + 1) % len(players)  # turn to next player


    winner = "x"

    for i in range(len(desk)):
        if len(desk[i]) > len(winner):
            winner = desk[i]
            current_player_id = i
        elif len(desk[i]) == len(winner):
            if len(winner) > 2:
                if winner[-1] < desk[i][-1]:
                    winner = desk[i]
                    current_player_id = i
            else:
                if desk[i][0] == color and winner[0] != color:
                    winner = desk[i]
                    current_player_id = i
                elif desk[i][0] == color and winner[0] == color:
                    if desk[i][-1] > winner[-1]:
                        winner = desk[i]
                        current_player_id = i
                # this desk[][] is not 2d array, its comparing the charactor in side on stirng of array
                # with winner's charactor
    players[current_player_id].leader = True
    players[current_player_id].win_cards += desk
    players[current_player_id].win_cards.sort()
    players[current_player_id].wintime = players[current_player_id].wintime + 1

    print("This round winner is player " + players[current_player_id].name + '\n')
    print("The won cards are: ")
    #print(desk)
    print(players[current_player_id].win_cards)  # small mistake
    print

    # if in final round the volunteer won exactly 1 round, mission Complete
    if players[volunteer_index].wintime > 1:
        print "Volunteer won twice"
        print "Mission failed"

        return
        
    if num_round == (40 / len(players) + 1):
        print "Win exactly 1 round for volunteer"
        print "Mission Complete"
    else:
        Player_round33(players, current_player_id, num_round, desk, communicated, volunteer_index)
