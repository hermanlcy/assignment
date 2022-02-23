
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

    else:
        #start from round 2 here

        num_round += 1

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
# end of part 2
       