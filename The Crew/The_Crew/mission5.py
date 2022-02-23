import random
import sys
from mission1 import *

avg_value = 2.384

# Commander decide which member is sick, only one member is sick
def decideSick(players, leader, num_of_player):
    print ("-------One of us is sick in bed-------")
    print ("-------Commander is Player%s-------" % leader)
    print ("-------Commander asks everyone how she/he feels-------")

    avg_list = []
    healthy_list = []

    for i in range(num_of_player):
        if players[i].captain == True:
            avg_list.append(sys.maxint)
        else:
            tmp = 0
            count = 0

            #ignore value less than 5 to compute avg value, set 5-9 as 1-5 respectively, set R1, R2, R3 as 10,11,12 respectively
            for j in players[i].B:
                if int(j[1]) >= 5:
                    tmp += int(j[1]) - 4
                count += 1
            for j in players[i].G:
                if int(j[1]) >= 5:
                    tmp += int(j[1]) - 4
                count += 1
            for j in players[i].P:
                if int(j[1]) >= 5:
                    tmp += int(j[1]) - 4
                count += 1
            for j in players[i].Y:
                if int(j[1]) >= 5:
                    tmp += int(j[1]) - 4
                count += 1
            for j in players[i].Rocket:
                tmp += int(j[6]) + 9
                count += 1
            
            avg_list.append(tmp / count)

    bad_count = 0
    chosen_index = -1

    for i in avg_list:
        if i <= avg_value:
            healthy_list.append('bad')
            bad_count += 1
        else:
            healthy_list.append('good')
    
    for i in range(num_of_player):
        print 'Player' + str(i) + ': ' + healthy_list[i]

    if bad_count == 1:
        chosen_index = healthy_list.index('bad')
    elif bad_count == 0:
        chosen_index = healthy_list.index(min(healthy_list))
        print 'Capitan: There is no sick player. I choose Player' + str(chosen_index) + ' as the sick player'
    elif bad_count > 1:
        chosen_index = healthy_list.index(min(healthy_list))
        print 'Captain: More than one sick player. I choose Player' + str(chosen_index) + ' as the sick player'

    return chosen_index


# mission5 test
#Player_round5(players, leader, num_round, desk, num_of_player)
def Player_round5(players, leader, num_round, desk, num_of_player, communicated):
    if num_round == 1:
        sick_player_id = decideSick(players, leader, num_of_player)
        Player_round5_running(players, leader, num_round, desk, num_of_player, sick_player_id, communicated)

#create a new method for Player_round5_running, with a new vairable called 'sick_player_id'
def Player_round5_running(players, leader, num_round, desk, num_of_player, sick_player_id, communicated):
    print("------------------ Round %d " % (num_round) + "----------------------")
    num_round += 1
    mission = 5
    leading_color = ''
    sick_player_appeared = False
    sick_player_card = ''

    print 'players[leader].name = ' + str(players[leader].name)

    if sick_player_id == players[leader].name:
        sick_player_appeared = True

    num_players = len(players)
    players[leader].leader = False
    desk = ['' for i in range(num_of_player)]

    card = random_play_without_rocket_low_priority(players[leader])
    print("\nPlayer " + players[leader].name + " played card: " + card)
    if communicated < num_of_player:
        communicated = communicating(players[leader], mission, num_round, communicated)
    if card in players[leader].communication:
        players[leader].communication = ""
    elif players[leader].communication is not "":
        print("Player " + players[leader].name + " communicating: " + players[leader].communication)

    desk[leader] = card
    leading_color = card[:-1]
    leader = (leader + 1) % num_players  # turn to next player

    if len(card) > 2:
        color = "Rocket"
    else:
        color = card[0]

    for i in range(num_players - 1):
        winner = "x"

        for i in range(len(desk)):
            if len(desk[i]) > len(winner):
                winner = desk[i]
            elif len(desk[i]) == len(winner):
                if len(winner) > 2:
                    if winner[-1] < desk[i][-1]:
                        winner = desk[i]
                else:
                    if desk[i][0] == color and winner[0] != color:
                        winner = desk[i]
                    elif desk[i][0] == color and winner[0] == color:
                        if desk[i][-1] > winner[-1]:
                            winner = desk[i]

        if str(sick_player_id) == str(players[leader].name):
            sick_player_appeared = True

        if sick_player_appeared:
            card, res = Player_card5(winner, sick_player_id, players[leader], sick_player_card, leading_color)

            if res == True:
                sick_player_card = card
        else:
            card = Player_card(players[leader], color)

        desk[leader] = card
        print("\nPlayer " + players[leader].name + " played card: " + card)
        if communicated < num_of_player:
            communicated = communicating(players[leader], mission, num_round, communicated)
        if card in players[leader].communication:
            players[leader].communication = ""
        elif players[leader].communication is not "":
            print("Player " + players[leader].name + " communicating: " + players[leader].communication)
        leader = (leader + 1) % num_players  # turn to next player

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
    print(desk)
    print

    # if the sick member wins one trick, the mission failed
    if players[sick_player_id].leader == True:
        print ("Mission fail---The sick crew member win this trick")
    elif num_round == (40 / num_of_player + 1):
        print ("All mission Complete")
    else:
        num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
        Player_round5_running(players, leader, num_round, desk, num_of_player, sick_player_id, communicated)

def random_play_without_rocket_low_priority(player):
    cards = player.B + player.Y + player.G + player.P

    if len(cards) > 0:
        card = random.choice(cards)

        if card[0] == 'P':
            player.P.remove(card)
        elif card[0] == 'G':
            player.G.remove(card)
        elif card[0] == 'Y':
            player.Y.remove(card)
        else:
            player.B.remove(card)
    else:
        card = random.choice(player.Rocket)
        player.Rocket.remove(card)
    
    return card

# Player_card function ask the player to give a card based on the color condition, cannot used as first card choice in each round
def Player_card5(winner, sick_player_id, player, sick_player_card, leading_color):
    card = ''

    if str(sick_player_id) == str(player.name):
        if winner[0] == 'R':
            if len(player.Rocket) != 0:
                card = player.Rocket[0]

                for i in player.Rocket:
                    if i > card and i < winner:
                        card = i

                player.Rocket.remove(card)
            else:
                if leading_color == winner[:-1]:
                    card = Max_play(player)
                else:
                    if leading_color == 'B' and len(player.B) > 0:
                        card = Max_play_certain_color(player, leading_color)
                    elif leading_color == 'Y' and len(player.Y) > 0:
                        card = Max_play_certain_color(player, leading_color)
                    elif leading_color == 'G' and len(player.G) > 0:
                        card = Max_play_certain_color(player, leading_color)
                    elif leading_color == 'P' and len(player.P) > 0:
                        card = Max_play_certain_color(player, leading_color)
        elif winner[0] == 'B':
            if len(player.B) != 0:
                card = player.B[0]

                for i in player.B:
                    if i > card and i < winner:
                        card = i

                player.B.remove(card)
            else:
                card = Max_play(player)
        elif winner[0] == 'Y':
            if len(player.Y) != 0:
                card = player.Y[0]

                for i in player.Y:
                    if i > card and i < winner:
                        card = i

                player.Y.remove(card)
            else:
                card = Max_play(player)
        elif winner[0] == 'G':
            if len(player.G) != 0:
                card = player.G[0]

                for i in player.G:
                    if i > card and i < winner:
                        card = i

                player.G.remove(card)
            else:
                card = Max_play(player)
        elif winner[0] == 'P':
            if len(player.P) != 0:
                card = player.P[0]

                for i in player.P:
                    if i > card and i < winner:
                        card = i

                player.P.remove(card)
            else:
                card = Max_play(player)
        
        #True means this card is played by sick player
        return card, True
    elif sick_player_card == winner:
        if winner[0] == 'R':
            if len(player.Rocket) != 0:
                card = player.Rocket[-1]

                for i in player.Rocket:
                    if i < card and i > winner:
                        card = i
                
                if card < winner:
                    card = player.Rocket[0]

                player.Rocket.remove(card)
            else:
                if leading_color == winner[:-1]:
                    card = Min_play_Rocket_First(player)
                else:
                    if leading_color == 'B' and len(player.B) > 0:
                        card = Min_play_certain_color(player, leading_color)
                    elif leading_color == 'Y' and len(player.Y) > 0:
                        card = Min_play_certain_color(player, leading_color)
                    elif leading_color == 'G' and len(player.G) > 0:
                        card = Min_play_certain_color(player, leading_color)
                    elif leading_color == 'P' and len(player.P) > 0:
                        card = Min_play_certain_color(player, leading_color)
        elif winner[0] == 'B':
            if len(player.B) != 0:
                card = player.B[-1]

                for i in player.B:
                    if i < card and i > winner:
                        card = i
                
                if card < winner and len(player.Rocket) > 0:
                    card = player.Rocket[0]

                if card in player.B:
                    player.B.remove(card)
                else:
                    player.Rocket.remove(card)
            else:
                if len(player.Rocket) > 0:
                    card = player.Rocket[0]
                else:
                    card = Min_play_Rocket_First(player)
        elif winner[0] == 'Y':
            if len(player.Y) != 0:
                card = player.Y[-1]

                for i in player.Y:
                    if i < card and i > winner:
                        card = i
                
                if card < winner and len(player.Rocket) > 0:
                    card = player.Rocket[0]

                if card in player.Y:
                    player.Y.remove(card)
                else:
                    player.Rocket.remove(card)
            else:
                if len(player.Rocket) > 0:
                    card = player.Rocket[0]
                else:
                    card = Min_play_Rocket_First(player)
        elif winner[0] == 'G':
            if len(player.G) != 0:
                card = player.G[-1]

                for i in player.G:
                    if i < card and i > winner:
                        card = i
                
                if card < winner and len(player.Rocket) > 0:
                    card = player.Rocket[0]

                if card in player.G:
                    player.G.remove(card)
                else:
                    player.Rocket.remove(card)
            else:
                if len(player.Rocket) > 0:
                    card = player.Rocket[0]
                else:
                    card = Min_play_Rocket_First(player)
        elif winner[0] == 'P':
            if len(player.P) != 0:
                card = player.P[-1]

                for i in player.P:
                    if i < card and i > winner:
                        card = i
                
                if card < winner and len(player.Rocket) > 0:
                    card = player.Rocket[0]

                if card in player.P:
                    player.P.remove(card)
                else:
                    player.Rocket.remove(card)
            else:
                if len(player.Rocket) > 0:
                    card = player.Rocket[0]
                else:
                    card = Min_play_Rocket_First(player)
        
        #False means this card is played by healthy player
        return card, False
    else:
        if winner[0] == 'R':
            if len(player.Rocket) != 0:
                card = player.Rocket[0]

                player.Rocket.remove(card)
            else:
                if leading_color == winner[:-1]:
                    card = Min_play_Rocket_First(player)
                else:
                    if leading_color == 'B' and len(player.B) > 0:
                        card = Min_play_certain_color(player, leading_color)
                    elif leading_color == 'Y' and len(player.Y) > 0:
                        card = Min_play_certain_color(player, leading_color)
                    elif leading_color == 'G' and len(player.G) > 0:
                        card = Min_play_certain_color(player, leading_color)
                    elif leading_color == 'P' and len(player.P) > 0:
                        card = Min_play_certain_color(player, leading_color)
        elif winner[0] == 'B':
            if len(player.B) != 0:
                card = player.B[0]

                for i in player.B:
                    if i < card and i > winner:
                        card = i

                player.B.remove(card)
            else:
                card = Min_play_Rocket_First(player)
        elif winner[0] == 'Y':
            if len(player.Y) != 0:
                card = player.Y[0]

                for i in player.Y:
                    if i < card and i > winner:
                        card = i

                player.Y.remove(card)
            else:
                card = Min_play_Rocket_First(player)
        elif winner[0] == 'G':
            if len(player.G) != 0:
                card = player.G[0]

                for i in player.G:
                    if i < card and i > winner:
                        card = i

                player.G.remove(card)
            else:
                card = Min_play_Rocket_First(player)
        elif winner[0] == 'P':
            if len(player.P) != 0:
                card = player.P[0]

                for i in player.P:
                    if i < card and i > winner:
                        card = i

                player.P.remove(card)
            else:
                card = Min_play_Rocket_First(player)

        #True means this card is played by sick player
        return card, False


#used for sick player to choose the certain color card.
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
    


#used for sick player to choose the random card.
def Max_play(player):
    cards = player.B + player.Y + player.G + player.P
    if len(cards) != 0:
        card = cards[0]
        for i in cards:
            if int(i[-1]) > int(card[-1]):
                card = i
    else:
        card = player.Rocket[0]
    
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

#used for healthy player to choose the certain color card.
def Min_play_certain_color(player, color):
    card = ''

    if color == 'B':
        card = player.B[0]
        player.B.remove(card)
    elif color == 'Y':
        card = player.Y[0]
        player.Y.remove(card)
    elif color == 'P':
        card = player.P[0]
        player.P.remove(card)
    else:
        card = player.G[0]
        player.G.remove(card)

    return card

#used for healthy player to choose the Rocket card. If the healthy player does not have rocket card, he/she should play the card with the smallest value
def Min_play_Rocket_First(player):
    cards = player.Rocket
    if len(cards) != 0:
        card = cards[0]
        
    else:
        cards = player.B + player.Y + player.G + player.P
        card = cards[0]

        for i in cards:
            if int(i[-1]) < int(card[-1]):
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

#used for play the card with the smallest value
def Min_play(player):
    cards = player.B + player.Y + player.G + player.P
    if len(cards) != 0:
        card = cards[0]

        for i in cards:
            if int(i[-1]) < int(card[-1]):
                card = i        
    else:
        cards = player.Rocket
        card = cards[0]

    
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
