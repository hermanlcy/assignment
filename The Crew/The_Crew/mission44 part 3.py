
    print(rocket_condition, "testing for rocket","\n")

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

    if len(judge_task) == 0 and judge_order == True:
        print "All mission completed in ascending order, Therefore Mission 44 Complete"
    elif len(judge_task) != 0 and judge_order == False:
        print "Not all mission completed, completed mission are in wrong order, Therefore Mission 44 failed"
    elif len(judge_task) == 0 and judge_order == False:
        print "All 4 four missions completed are in wrong order, Therefore Mission 44 failed"
    else:
        if num_round == (40 / num_of_player + 1):
            print "This is round 13, since Not All four missions are Completed, So Mission 44 failed"
            print "Remaining cards", judge_task
        else:
            # countine until as long as the game is not over
            num_hand = players[-1].P + players[-1].Y + players[-1].G + players[-1].B + players[-1].Rocket
            Player_round44(players, leader, num_round, desk, judge_task, num_of_player)

# part 3 end in here
