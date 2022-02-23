from mission1 import *

# Player_card function ask the player to give a card based on the color condition
def Player_card34(player, color, max_wins):
    card = ''
    if color == "Rocket":
        if len(player.Rocket) != 0:
            if player.wins == max_wins:
                card = player.Rocket[0]
                player.Rocket.remove(card)
            else:
                card = player.Rocket[-1]
                player.Rocket.remove(card)
        else:
            card = Random_play(player)
    elif color == 'B':
        if len(player.B) != 0:
            if player.wins == max_wins:
                card = player.B[0]
                player.B.remove(card)
            else:
                card = player.B[-1]
                player.B.remove(card)
        else:
            card = Random_play(player)
    elif color == 'Y':
        if len(player.Y) != 0:
            if player.wins == max_wins:
                card = player.Y[0]
                player.Y.remove(card)
            else:
                card = player.Y[-1]
                player.Y.remove(card)
        else:
            card = Random_play(player)
    elif color == 'G':
        if len(player.G) != 0:
            if player.wins == max_wins:
                card = player.G[0]
                player.G.remove(card)
            else:
                card = player.G[-1]
                player.G.remove(card)
        else:
            card = Random_play(player)
    elif color == 'P':
        if len(player.P) != 0:
            if player.wins == max_wins:
                card = player.P[0]
                player.P.remove(card)
            else:
                card = player.P[-1]
                player.P.remove(card)
        else:
            card = Random_play(player)
    else:
        if player.captain and player.wins == 0:
            cards = player.B + player.Y + player.G + player.P
            cards.sort(key=lambda x: x[-1])
            card = cards[-1]
            if card[0] == 'B':
                player.B.remove(card)
            elif card[0] == 'Y':
                player.Y.remove(card)
            elif card[0] == 'G':
                player.G.remove(card)
            elif card[0] == 'P':
                player.P.remove(card)
        else:    
            card = Random_play(player)
    return card

def CheckWinNum(Players, max_wins):
    for i in Players:
        if max_wins - i.wins == 2:
            return True
    return False   

def Player_round34(Players, leader, num_round, max_wins):

    print("Round %d: "%(num_round))

    player_number = len(Players)
    Players[leader].leader = False
    desk = ["Unknow" for i in range(player_number)] # store the cards are played in this round

    card = Player_card34(Players[leader], "random", max_wins)
    print(Players[leader].name + " played card: " + card + '\n')
    desk[leader] = card
    leader = (leader + 1) % player_number # trun to next player


    if len(card) > 2:
        color = "Rocket"
    else:
        color = card[0]
    
    for i in range(player_number-1):
        card = Player_card34(Players[leader], color, max_wins)
        desk[leader] = card
        print(Players[leader].name + " played card: " + card + '\n')
        leader = (leader + 1) % player_number # trun to next player

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

    Players[leader].leader = True
    Players[leader].win_cards += desk
    Players[leader].win_cards.sort()
    Players[leader].wins += 1 # The number of the player won round plus 1
    print("This round winner is " + Players[leader].name + '\n')
    print("The winned cards are: ")
    print(desk)
    print
    if Players[leader].wins > max_wins: # check whether this player won 2 more rounds than others
        max_wins = Players[leader].wins
        if CheckWinNum(Players, max_wins):
            print("A crew should not won 2 more rounds than others.")
            return False

    num_hand = Players[-1].P + Players[-1].Y + Players[-1].G + Players[-1].B + Players[-1].Rocket
    # check whether the captain won the first round 
    if num_round == 1 or num_round == 40/player_number:
        if Players[leader].captain != True:
            print("The captain has to win the first and the last round.")
            return False
    if len(num_hand) != 0:
        num_round += 1
        Player_round34(Players, leader, num_round, max_wins)
