    # start of part 2
    for i in range(num_players - 1):  # player 1 & 2
        if leader == track + 1:
            second_card_thisRound = card

        if (second_card_thisRound == "P9" and players[leader].P == 0 and players[leader].Rocket != 0) or (second_card_thisRound == "B9" and players[leader].B == 0 and players[leader].Rocket != 0) or (second_card_thisRound == "P9" and players[leader].P == 0 and players[leader].Rocket != 0) or (second_card_thisRound == "P9" and players[leader].P == 0 and players[leader].Rocket != 0) :
            if "Rocket1" in players[leader].Rocket: # Second -- wining logic 
                card = "Rocket1"
                total_used_card[n] = card
                n = n + 1
                players[leader].Rocket.remove("Rocket1")
            elif "Rocket2" in players[leader].Rocket:
                card = "Rocket2"
                total_used_card[n] = card
                n = n + 1
                players[leader].Rocket.remove("Rocket2")
            elif "Rocket3" in players[leader].Rocket:
                card = "Rocket3"
                total_used_card[n] = card
                n = n + 1
                players[leader].Rocket.remove("Rocket3")
            elif "Rocket4" in players[leader].Rocket:
                card = "Rocket4"
                total_used_card[n] = card
                n = n + 1
                players[leader].Rocket.remove("Rocket4")
        elif color == 'P' and len(players[leader].P) == 0: # First: --wining logic: 
            if "B9" in players[leader].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[leader].B.remove(card)
            elif "Y9" in players[leader].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[leader].Y.remove(card)
            elif "G9" in players[leader].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[leader].G.remove(card)
        elif color == 'B' and len(players[leader].B) == 0:
            if "P9" in players[leader].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[leader].P.remove(card)
            elif "Y9" in players[leader].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[leader].Y.remove(card)
            elif "G9" in players[leader].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[leader].G.remove(card)
        elif color == 'G' and len(players[leader].G) == 0:
            if "P9" in players[leader].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[leader].P.remove(card)
            elif "Y9" in players[leader].Y:
                card = "Y9"
                total_used_card[n] = card
                n = n + 1
                players[leader].Y.remove(card)
            elif "B9" in players[leader].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[leader].B.remove(card)
        elif color == 'Y' and len(players[leader].Y) == 0:
            if "P9" in players[leader].P:
                card = "P9"
                total_used_card[n] = card
                n = n + 1
                players[leader].P.remove(card)
            elif "G9" in players[leader].G:
                card = "G9"
                total_used_card[n] = card
                n = n + 1
                players[leader].G.remove(card)
            elif "B9" in players[leader].B:
                card = "B9"
                total_used_card[n] = card
                n = n + 1
                players[leader].B.remove(card)
        else:
            card = play16(players[leader], color)
            desk[leader] = card
            total_used_card[i] = card
            i = i + 1

        print("Follower -- blue", players[leader].B, "yellow", players[leader].Y, "green", players[leader].G, "pink", players[leader].P, "rocket", players[leader].Rocket)
        print("Player " + players[leader].name + " played card: " + card + '\n')
        leader = (leader + 1) % num_players  # trun to next player


    winner = "x"
    flag = False 


    # end of part 2