
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

    # Task Completed checked, if task is completed it will be remove from judge_task
    for single_trick_card in players[leader].win_cards:
        for single_task_card in players[leader].task:
            if single_task_card == single_trick_card:
                print "Task", single_task_card, "Completed"
                players[leader].task.remove(single_task_card)
                judge_task.remove(single_task_card)

    # print"####################################"

    if len(judge_task) == 0:
        print "Therefore Mission 46 Complete"

    else:
        if num_round == (40 / num_of_player + 1):
            print "Not even one task Completed, So Mission 46 fail"
            print "Remaining cards", judge_task
        else:
            # countine until as long as the game is not over
            # num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round46(players, leader, num_round, desk, judge_task, num_of_player)
# end of part 3
