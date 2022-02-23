import random
import copy
from mission24 import *
from mission36 import *

# large_card include 40 cards, task_card include 36 task cards
large_card = [
    'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', # B9 = 8
    'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', # G9 = 17
    'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', # P9 = 26
    'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9',
    'Rocket1', 'Rocket2', 'Rocket3', 'Rocket4',
]

task_card = large_card[:36] # this should be 35 instead of 36

# track number of task on mission(i)
num_of_task = [1, 2, 2, 3, 0, 3, 3, 3, 0, 4, #each row has 10 mission
               4, 4, 0, 4, 4, 0, 2, 5, 5, 2, # logic for mission 16 is if we are able to finish all the round game without winning any round with 9
               5, 5, 5, 6, 6, 0, 3, 6, 0, 6,
               6, 7, 0, 0, 7, 7, 4, 8, 8, 8,
               0, 9, 9, 0, 9, 0, 10, 3, 10, 0
               ]


# Player class includes all the attributes,
# all attributes can be print easily by typing Players[i].print_detail()
class Player:
    def __init__(self, Name):
        self.name = Name
        self.B = []
        self.G = []
        self.P = []
        self.Y = []
        self.Rocket = []
        self.task = []
        self.fail_task = ["Y9","B9","P9","G9"]
        self.win_cards = []
        self.captain = False
        self.leader = False
        self.communication = ""
        self.communication_card = ""
        # -2: not_initialised, -1: the smallest card, 0: only 1 card, 1: the biggest card
        self.communication_card_pos = -2
        self.wins = 0
        self.volunteer = False
        self.wintime = 0

    def print_detail(self):
        print("-----------------Player " + self.name + " cards------------------")
        print("Blue card: %s" % self.B)
        print("Green card: %s" % self.G)
        print("Pink card: %s" % self.P)
        print("Yellow card: %s" % self.Y)
        print("Rocket card: %s" % self.Rocket)
        print("task: %s" % self.task)
        if len(self.win_cards) > 0:
            print("win cards: %s" % self.win_cards)
        # if len(self.communication) > 0:
        #     print("communication card: " + self.communication)
        print


# generate player (AI)
def generate_player(num_of_player):
    players = []
    for i in range(num_of_player):
        players.append(Player(str(i)))
    return players


# distributing 40 cards to each player
def card_distributing(num_of_player, players):
    print ("-------------------------------------------------")
    print ("---------------card distributing-----------------")
    print ("-------------------------------------------------\n")
    random.shuffle(large_card)
    individual_card = 40 / num_of_player
    # player 0 will have 14 cards when there are 3 players
    for i in range(num_of_player):
        player_card = large_card[i * individual_card:(i + 1) * individual_card]
        if num_of_player == 3 and i == 0:
            player_card.insert(0, large_card[-1])
            player_card.sort()
            sort_hand_card(players[i], player_card)
        else:
            player_card.sort()
            sort_hand_card(players[i], player_card)

def card_distributing1(num_of_player, players):
    # print ("-------------------------------------------------")
    # print ("---------------card distributing-----------------")
    # print ("-------------------------------------------------\n")
    random.shuffle(large_card)
    individual_card = 40 / num_of_player
    # player 0 will have 14 cards when there are 3 players
    for i in range(num_of_player):
        player_card = large_card[i * individual_card:(i + 1) * individual_card]
        if num_of_player == 3 and i == 0:
            player_card.insert(0, large_card[-1])
            player_card.sort()
            sort_hand_card(players[i], player_card)
        else:
            player_card.sort()
            sort_hand_card(players[i], player_card)


# sort hand card in each color and find the captain
def sort_hand_card(player, cards):
    for i in cards:
        if len(i) > 2:
            player.Rocket.append(i)
            if i == "Rocket4":
                player.captain = True # this stay for the whole mission
                player.leader = True # this stay for only first round
        elif i[0] == 'P':
            player.P.append(i)
        elif i[0] == 'G':
            player.G.append(i)
        elif i[0] == 'Y':
            player.Y.append(i)
        else:
            player.B.append(i)
    player.B.sort()
    player.Y.sort()
    player.G.sort()
    player.P.sort() 
    player.Rocket.sort()
    # asending order to sort 5 type of card each of array

# number of task distributing according to the mission number
def task_picking(mission, players):
    random.shuffle(task_card)
    total_task = num_of_task[mission - 1]

    judge_task = []
    # no preference pick for now, implement condition later
    

    # if mission == 9 or mission == 26:
    #     for i in range(len(players)):
    #             if "B1" in players[i].B:
    #                 players[i].task.append("B1")
    #                 judge_task.append("B1")
    #             if "G1" in players[i].G:
    #                 players[i].task.append("G1")
    #                 judge_task.append("G1")
    #             if "P1" in players[i].P:
    #                 players[i].task.append("P1")
    #                 judge_task.append("P1")
    #             if "Y1" in players[i].Y:
    #                 players[i].task.append("Y1")
    #                 judge_task.append("Y1")
    # elif mission == 16:
    #     for i in range(len(players)):
    #             if "Y9" in players[i].Y:
    #                 players[i].task.append("Y9")
    #                 judge_task.append("Y9")
    #             if "G9" in players[i].G:
    #                 players[i].task.append("G9")
    #                 judge_task.append("G9")
    #             if "B9" in players[i].B:
    #                 players[i].task.append("B9")
    #                 judge_task.append("B9")
    #             if "P9" in players[i].P:
    #                 players[i].task.append("P9")
    #                 judge_task.append("P9")   
    # elif mission == 46:
    #     chosen_one = 0
    #     for i in range(len(players)):
    #         if "P9" in players[i].P:
    #             if len(players) == 3:
    #                 if i == 2:
    #                     chosen_one == 0
    #                 else:
    #                     chosen_one == i + 1
    #             if len(players) == 4:
    #                 if i == 3:
    #                     chosen_one == 0
    #                 else:
    #                     chosen_one == i + 1
    #             if len(players) == 5:
    #                 if i == 4:
    #                     chosen_one == 0
    #                 else:
    #                     chosen_one == i + 1
    #     players[chosen_one].task.append("P1")
    #     judge_task.append("P1")
    #     players[chosen_one].task.append("P2")
    #     judge_task.append("P2")
    #     players[chosen_one].task.append("P3")
    #     judge_task.append("P3")
    #     players[chosen_one].task.append("P4")
    #     judge_task.append("P4")
    #     players[chosen_one].task.append("P5")
    #     judge_task.append("P5")
    #     players[chosen_one].task.append("P6")
    #     judge_task.append("P6")
    #     players[chosen_one].task.append("P7")
    #     judge_task.append("P7")
    #     players[chosen_one].task.append("P8")
    #     judge_task.append("P8")
    #     players[chosen_one].task.append("P9")
    #     judge_task.append("P9")
    # elif mission == 13 or 44:
    #     for i in range(len(players)):
    #             if "Rocket1" in players[i].Rocket:
    #                 players[i].task.append("Rocket1")
    #                 judge_task.append("Rocket1")
    #             if "Rocket2" in players[i].Rocket:
    #                 players[i].task.append("Rocket2")
    #                 judge_task.append("Rocket2")
    #             if "Rocket3" in players[i].Rocket:
    #                 players[i].task.append("Rocket3")
    #                 judge_task.append("Rocket3")
    #             if "Rocket4" in players[i].Rocket:
    #                 players[i].task.append("Rocket4")
    #                 judge_task.append("Rocket4")     
    # elif mission == 17:
    #     for i in range(total_task):
    #         players[i%len(players)].task.append(task_card[i])  # use moudule to correct this task card distribution -- most important change
    #         judge_task.append(task_card[i])  
    if mission == 20:
        temp = players[:]
        for i in players:
            if i.captain:
                temp.remove(i)
        
        length = len(temp)
        player = temp[random.choice(range(length))]
        for i in range(2):
            player.task.append(task_card[i])
            judge_task.append(task_card[i])
    elif mission == 24:
        for i in range(total_task):
            judge_task.append(task_card[i])
        # print(judge_task)
        for i in judge_task:
            Yes = []
            for j in range(len(players)):
                temp = Answer24(players[j], i)
                # print(j.name + " task: " + i)
                # print(temp)
                if temp:
                    Yes.append(j)
            # for k in Yes:
            #     print(k)
            if len(Yes) > 0:
                idx = random.choice(Yes)
                players[idx].task.append(i)
                # print(players[idx].name + " takes the task: " + i )
                # print(players[idx].name + " now has the tasks: ")
                # print(players[idx].task)
            else:
                idx = random.choice(range(len(players)))
                players[idx].task.append(i)
                # print(players[idx].name + " takes the task: " + i)
                # print(players[idx].name + " now has the tasks: ")
                # print(players[idx].task)
    elif mission == 27:
        player = players[random.choice(range(len(players)))]
        print "-------Player %s takes all the three tasks--------\n" % player.name
        for i in range(3):
            player.task.append(task_card[i])
            judge_task.append(task_card[i])
    elif mission == 36:
        captain = -1
        trash = []
        for i in range(len(players)):
            trash.append(i)

        for i in range(len(players)):
            if players[i].captain:
                captain = i # index of captain
                trash.remove(captain)
                print("captain is NO." + str(captain))
                print(trash)

        for i in judge_task:
            temp = Answer36(players[captain], i)
            if temp:
                players[captain].mission.append(i)
                print("captain handles the task")
            else:
                player = random.choice(trash)
                players[player].mission.append(i)
                print(players[player].name + " handles the task")
    elif mission == 37:
        temp = players[:]
        for i in players:
            if i.captain:
                temp.remove(i)

        length = len(temp)
        player = temp[random.choice(range(length))]
        print "-------Player %s takes all the four tasks--------\n" % player.name
        for i in range(4):
            player.task.append(task_card[i])
            judge_task.append(task_card[i])
    elif mission == 43:
        temp = players[:]
        for i in players:
            if i.captain:
                temp.remove(i)
        length = len(temp)
        for i in range(9):
            player = temp[random.choice(range(length))]
            player.task.append(task_card[i])
            judge_task.append(task_card[i])
    elif mission == 32:
        print "total_task:" + str(total_task)
        Y_count = 0
        G_count = 0
        B_count = 0
        P_count = 0

        for i in range(total_task):
            if task_card[i][0] == 'Y':
                Y_count = Y_count + 1
            elif task_card[i][0] == 'G':
                G_count = G_count + 1
            elif task_card[i][0] == 'B':
                B_count = B_count + 1
            elif task_card[i][0] == 'P':
                P_count = P_count + 1

        tmp_players = copy.deepcopy(players)

        for i in range(total_task):
            append_to_capital = False
            # if player is capital, he / she should judge if he / she has this color's big point card
            for j in range(len(players)):
                if players[j].captain:
                    if task_card[i][0] == 'Y':
                        if tmp_players[j].Y:
                            if int(tmp_players[j].Y[-1][1]) >= 10 - Y_count:
                                del(tmp_players[j].Y[-1])
                                players[j].task.append(task_card[i])
                                judge_task.append(task_card[i])
                                append_to_capital = True
                    elif task_card[i][0] == 'G':
                        if tmp_players[j].G:
                            if int(tmp_players[j].G[-1][1]) >= 10 - G_count:
                                del(tmp_players[j].G[-1])
                                players[j].task.append(task_card[i])
                                judge_task.append(task_card[i])
                                append_to_capital = True
                    elif task_card[i][0] == 'B':
                        if tmp_players[j].B:
                            if int(tmp_players[j].B[-1][1]) >= 10 - B_count:
                                del(tmp_players[j].B[-1])
                                players[j].task.append(task_card[i])
                                judge_task.append(task_card[i])
                                append_to_capital = True
                    elif task_card[i][0] == 'P':
                        if tmp_players[j].P:
                            if int(tmp_players[j].P[-1][1]) >= 10 - P_count:
                                del(tmp_players[j].P[-1])
                                players[j].task.append(task_card[i])
                                judge_task.append(task_card[i])
                                append_to_capital = True
                    
            # append task to non-capital player
            if append_to_capital == False:
                temp = players[:]

                for j in players:
                    if j.captain:
                        temp.remove(j)
                
                length = len(temp)
                player = temp[random.choice(range(length))]
                player.task.append(task_card[i])
                judge_task.append(task_card[i])
                
    else:
        for i in range(total_task): 
            players[i%len(players)].task.append(task_card[i])  # use moudule to correct this task card distribution -- most important change
            judge_task.append(task_card[i])


    for player in players:
        player.task.sort()
    return judge_task
