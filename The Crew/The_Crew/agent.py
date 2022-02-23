# unify all the algorithm
from game_engine import report_status
from player import *
from communication import *
from mission1 import *
from mission3 import *
from mission5 import *
from mission6 import *
from mission7 import *
from mission9 import *
from mission12 import *
from mission13 import *
# from mission16full import *
from mission17 import *
from mission24 import *
from mission26 import *
from mission28 import *
from mission29 import *
from mission33 import *
from mission34 import *
from mission36 import *
from mission44Full import *
from mission46full import *
from mission48 import *
from mission51 import *
from priority_omage import *


def agent7PG(mission, num_of_player):
    players = generate_player(num_of_player)
    card_distributing(num_of_player, players)
    # need to run it on each round
    judge_task = task_picking(mission, players)
    # communicating(players, mission)
    for i in range(num_of_player):
        players[i].print_detail()

    # store the cards are played in this round
    desk = ["Unknown" for i in range(num_of_player)]
    total_used_card = ["null" for i in range(40)]  # testing track all the used card
    leader = -1
    num_round = 1
    # find the leader index
    for i in range(len(players)):
        if players[i].leader:
            leader = i

    test_mode = False
    origin = True
    upgrade = False
    communicated = 0

    if mission in [1, 2, 4, 10, 18, 20, 24, 27, 32, 36, 37, 38, 42, 43, 47]:
        if test_mode == False:
            Player_round(players, leader, num_round, desk, judge_task, num_of_player, mission, communicated)
            report_status(players, num_of_player)
        else:
            if origin == True:
                success = 0
                time = 1000
                for i in range(time):
                    players = generate_player(num_of_player)
                    card_distributing1(num_of_player, players)
                    judge_task = task_picking(mission, players)
                    desk = ["Unknown" for i in range(num_of_player)]
                    total_used_card = ["null" for i in range(40)]
                    leader = -1
                    num_round = 1
                    for i in range(len(players)):
                        if players[i].leader:
                            leader = i

                    temp = Player_round51(players, leader, num_round, desk, judge_task, num_of_player,
                                          mission, communicated)
                    if temp == 1:
                        success += temp
                result = float(success) / time * 100
                print ("------Success rate of 1000 tests:-------")
                print("%.1f" % result + "%")

    if mission in [3, 8, 11, 15, 19, 21, 23, 31, 40]:  # 3,8,(11),15,19,(21),[23],31,[36],[40]
        priority_index = 0
        priority_list = priority_define(judge_task, mission)
        if mission == 23:
            temp = priority_list
            priority_list = priority_exchange(temp)
        if mission == 40:
            temp = priority_list
            priority_list = priority_exchange1(temp, judge_task)
        Player_round3(players, leader, num_round, desk, judge_task, num_of_player,
                      priority_list, priority_index, mission, communicated)
        report_status(players, num_of_player)

    if mission in [6, 14, 22, 25, 30, 35, 39, 45, 49]:  # (6),(14),22,(25),(30),35,(39),45,49
        priority_index = 0
        priority_list = priority_define(judge_task, mission)
        Player_round6(players, leader, num_round, desk, judge_task, num_of_player,
                      priority_list, priority_index, mission, communicated)
        report_status(players, num_of_player)

    if mission == 5:
        Player_round5(players, leader, num_round, desk, num_of_player, communicated)
        report_status(players, num_of_player)

    if mission == 7:
        task_index = 0
        omage_task = omage_define(judge_task)
        task_number = len(judge_task)
        Player_round7(players, leader, num_round, desk, judge_task, num_of_player,
                      task_index, omage_task, task_number, communicated)
        report_status(players, num_of_player)

    if mission == 9:
        Player_round9(players, leader, num_round, desk, judge_task, num_of_player, communicated)
        report_status(players, num_of_player)

    if mission == 12:  # draft
        task_index = 0
        omage_task = omage_define(judge_task)
        task_number = len(judge_task)
        Player_round12(players, leader, num_round, desk, judge_task, num_of_player,
                       task_index, omage_task, task_number, communicated)
        report_status(players, num_of_player)

    if mission == 13:
        Player_round13(players, leader, num_round, desk, judge_task, num_of_player, communicated)
        report_status(players, num_of_player)

    # if mission == 16:
    #     Player_round16(players, leader, num_round, desk, total_used_card, judge_task, num_of_player)  # testing
    #     report_status(players, num_of_player)

    if mission == 17:
        Player_round17(players, leader, num_round, desk, total_used_card, judge_task, fail_judge_task,
                       num_of_player)  # testing
        report_status(players, num_of_player)

    if mission == 26:
        Player_round26(players, leader, num_round, desk, judge_task, num_of_player, communicated)
        report_status(players, num_of_player)

    if mission == 28:
        priority_index = 0
        task_index = 0
        priority_list = priority_define(judge_task, mission)
        omage_task = priority_omage_define(judge_task, priority_list)
        task_number = len(judge_task)
        Player_round28(players, leader, num_round, desk, judge_task, num_of_player,
                       priority_list, priority_index, task_index, omage_task, task_number, communicated)
        report_status(players, num_of_player)

    if mission == 29:
        tricks = {}
        for i in range(num_of_player):
            tempP = str(i)
            tricks[tempP] = 0
        print "Wining tricks:"
        print tricks
        Player_round29(players, leader, num_round, desk, num_of_player, mission, communicated, tricks)
        report_status(players, num_of_player)

    if mission == 33:
        volunteer_index = decide_volunteer(players)
        assign_communication_cards(players, leader, num_round, communicated)
        communicated = communicated + len(players)
        Player_round33(players, leader, num_round, desk, communicated, volunteer_index)
        report_status(players, num_of_player)

    if mission == 34:
        Player_round34(players, leader, num_round, 0)
        report_status(players, num_of_player)

    if mission == 36:
        priority_index = 0
        priority_list = priority_define(judge_task, mission)
        Player_round3(players, leader, num_round, desk, judge_task, num_of_player,
                      priority_list, priority_index, mission, communicated)
        report_status(players, num_of_player)

    if mission == 44:
        Player_round44(players, leader, num_round, desk, judge_task, num_of_player)
        report_status(players, num_of_player)

    if mission == 46:
        Player_round46(players, leader, num_round, desk, judge_task, num_of_player)
        report_status(players, num_of_player)

    if mission == 48:
        last_round = 40 / len(players)
        task_index = 0
        omage_task = omage_define(judge_task)
        task_number = len(judge_task)
        Player_round48(players, leader, num_round, desk, judge_task, num_of_player,
                       task_index, omage_task, task_number, last_round, communicated)
        report_status(players, num_of_player)