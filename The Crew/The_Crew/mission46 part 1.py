import random
from mission1 import *

# mission 46's logic is say who has pink 9 then the person on the left handside will need to winnig all card in pink

# run this mission for 4 times that there is some error but the fifth time we run this it will gives out correct output
# Winning logic
# whoever is the chosen one if he or she are the round leader then they can either dish out any color apart from pink 
# if other player are leader and they don't have big pink card then dish out pink card
# if the chosen one has rocket and he or she can dish out the rocket to win pink card then they should dish out rocket card to win the round
# all other players should trying to dish out pink when the chosen one is dishing out other color apart from pink if they can
# mission9 test
def Player_round46(players, leader, num_round, desk, judge_task, num_of_player):
    chosen_one = 0
    print("------------------ Round %d " % (num_round) + "----------------------")

    if num_round == 1: # this if condition only work for the first round to eliminate the rocket cards as much as possible
        for i in range(len(players)):
            if "P9" in players[i].P:
                if len(players) == 3:
                    if i == 2:
                        chosen_one == 0
                    else:
                        chosen_one == i + 1
                if len(players) == 4:
                    if i == 3:
                        chosen_one == 0
                    else:
                        chosen_one == i + 1
                if len(players) == 5:
                    if i == 4:
                        chosen_one == 0
                    else:
                        chosen_one == i + 1

        num_round = num_round +1
        num_players = len(players)
        players[leader].leader = False
            
        if leader != chosen_one and "P9" not in players[leader].P and "P8" not in players[leader].P and "P7" not in players[leader].P and "P6" not in players[leader].P:
            card = Player_card(players[leader],"P")
        else:
            card = Player_card(players[leader],"random")

        print("Player " + players[leader].name + " played card: " + card + '\n')

        desk[leader] = card
        leader = (leader + 1) % num_players  # trun to next player
        
        if len(card) > 2:
            color = "Rocket"
        else:
            color = card[0]

        for i in range(num_players - 1):
            if i == chosen_one:
                if color == "P" :
                    if len(players[chosen_one].P) == 0 and len(players[chosen_one].Rocket) != 0:
                        card = card = Player_card(players[leader],"Rocket")
            else:
                card = Player_card(players[leader], color)
            desk[leader] = card
            print("Player " + players[leader].name + " played card: " + card + '\n')
            leader = (leader + 1) % num_players  # trun to next player
# end of part 1
       