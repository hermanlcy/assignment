
    # print ("track delte: ", track_delete)

    # remove the card from the copy's deck
    if str(round_leader_index) in Copy_hand:
        Copy_hand[str(round_leader_index)].remove(track_delete)
        # print(str(round_leader_index))
        # print(str(round_leader_index))

    print("Else -- blue", players[round_leader_index].B, "yellow", players[round_leader_index].Y, "green", players[round_leader_index].G, "pink", players[round_leader_index].P, "rocket", players[round_leader_index].Rocket)
    print("Player " + players[round_leader_index].name + " played card: " + card + '\n')
    desk[round_leader_index] = card
    total_used_card[n] = card
    n = n + 1

    
    # print (round_leader_index , "before")
    round_leader_index = (round_leader_index + 1) % num_players  # trun to next player

    track = round_leader_index
    # print (round_leader_index , "after")
    # print(card, "efefe")
    if len(card) > 2:
        # print(card, "efefe")
        color = "Rocket"
    else:
        color = card[0]

    for i in range(num_players - 1):  # player 1 & 2
        if round_leader_index == track + 1:
            second_card_thisRound = card

        if (second_card_thisRound == "P9" and players[round_leader_index].P == 0 and players[round_leader_index].Rocket != 0) or (second_card_thisRound == "B9" and players[round_leader_index].B == 0 and players[round_leader_index].Rocket != 0) or (second_card_thisRound == "P9" and players[round_leader_index].P == 0 and players[round_leader_index].Rocket != 0) or (second_card_thisRound == "P9" and players[round_leader_index].P == 0 and players[round_leader_index].Rocket != 0) :
            if "Rocket1" in players[round_leader_index].Rocket: # Second -- wining logic 
                card = "Rocket1"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Rocket.remove("Rocket1")
            elif "Rocket2" in players[round_leader_index].Rocket:
                card = "Rocket2"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Rocket.remove("Rocket2")
            elif "Rocket3" in players[round_leader_index].Rocket:
                card = "Rocket3"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Rocket.remove("Rocket3")
            elif "Rocket4" in players[round_leader_index].Rocket:
                card = "Rocket4"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Rocket.remove("Rocket4")
        elif color == 'P' and len(players[round_leader_index].P) == 0: # First: --wining logic: 
            if "B9" in players[round_leader_index].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].B.remove(card)
            elif "Y9" in players[round_leader_index].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Y.remove(card)
            elif "G9" in players[round_leader_index].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].G.remove(card)
        elif color == 'B' and len(players[round_leader_index].B) == 0:
            if "P9" in players[round_leader_index].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].P.remove(card)
            elif "Y9" in players[round_leader_index].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Y.remove(card)
            elif "G9" in players[round_leader_index].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].G.remove(card)
        elif color == 'G' and len(players[round_leader_index].G) == 0:
            if "P9" in players[round_leader_index].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].P.remove(card)
            elif "Y9" in players[round_leader_index].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].Y.remove(card)
            elif "B9" in players[round_leader_index].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].B.remove(card)
        elif color == 'Y' and len(players[round_leader_index].Y) == 0:
            if "P9" in players[round_leader_index].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].P.remove(card)
            elif "G9" in players[round_leader_index].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].G.remove(card)
            elif "B9" in players[round_leader_index].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[round_leader_index].B.remove(card)
        else:
            card = play16(players[round_leader_index], color)
            desk[round_leader_index] = card
            total_used_card[i] = card
            i = i + 1

        print("Follower -- blue", players[round_leader_index].B, "yellow", players[round_leader_index].Y, "green", players[round_leader_index].G, "pink", players[round_leader_index].P, "rocket", players[round_leader_index].Rocket)
        print("Player " + players[round_leader_index].name + " played card: " + card + '\n')
        round_leader_index = (round_leader_index + 1) % num_players  # trun to next player


    winner = "x"
    flag = False 

    for i in range(len(desk)):
        if len(desk[i]) > len(winner):
            winner = desk[i]
            round_leader_index = i
        elif len(desk[i]) == len(winner):
            if len(winner) > 2:
                if winner[-1] < desk[i][-1]:
                    winner = desk[i]
                    round_leader_index = i
            else:
                if desk[i][0] == color and winner[0] != color:
                    winner = desk[i]
                    round_leader_index = i
                elif desk[i][0] == color and winner[0] == color:
                    if desk[i][-1] > winner[-1]:
                        winner = desk[i]
                        round_leader_index = i

    players[round_leader_index].leader = True
    players[round_leader_index].win_cards += desk
    players[round_leader_index].win_cards.sort()

    print("This round winner is player " + players[round_leader_index].name + '\n')
    print("The won cards are: ")
    print(players[round_leader_index].win_cards)
    print
    #end of part 2