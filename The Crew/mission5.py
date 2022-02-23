import random
from mission1 import *

# Commander decide which member is sick, only one member is sick
def decideSick(players, leader):
    twoHealthyCondition = ["good", "bad"]
    print ("-------One of us is sick in bed-------")
    print ("-------Commander is Player%s-------" % leader)
    print ("-------Commander asks everyone how she/he feels-------")

    playersExceptLeader = list(players)
    del playersExceptLeader[leader]

    # only one bad
    sickPlayerId = 0
    for i in range(len(playersExceptLeader)):
        playersExceptLeader[i].healthStatus = random.choice(twoHealthyCondition)
        if (playersExceptLeader[i].healthStatus == "bad"):
            sickPlayerId = playersExceptLeader[i].name
            break
    i += 1
    while i < len(playersExceptLeader):
        playersExceptLeader[i].healthStatus = "good"
        i += 1

    for i in range(len(playersExceptLeader)):
        print ("player%s's health status: %s" % (playersExceptLeader[i].name, playersExceptLeader[i].healthStatus))

    print ("-------The sick player is player%s-------" % sickPlayerId)
    print
    return sickPlayerId


# mission5 test
def player_round5(players, leader, num_round, desk, num_of_player):
    sickPlayerId = 0
    if num_round == 1:
        sickPlayerId = decideSick(players, leader)
    print("------------------ Round %d " % (num_round) + "----------------------")
    num_round += 1

    num_players = len(players)
    players[leader].leader = False

    card = Player_card(players[leader], "random")
    print("Player " + players[leader].name + " played card: " + card + '\n')
    desk[leader] = card
    leader = (leader + 1) % num_players  # turn to next player

    if len(card) > 2:
        color = "Rocket"
    else:
        color = card[0]

    for i in range(num_players - 1):
        card = Player_card(players[leader], color)
        desk[leader] = card
        print("Player " + players[leader].name + " played card: " + card + '\n')
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

    print("This round winner is player " + players[leader].name + '\n')
    print("The won cards are: ")
    print(desk)
    print

    # if the sick member wins one trick, the mission failed
    if leader == sickPlayerId:
        print ("Mission fail---The sick crew member win this trick")
    elif num_round == (40 / num_of_player + 1):
        print ("All mission Complete")
    else:
        num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
        player_round5(players, leader, num_round, desk, num_of_player)
