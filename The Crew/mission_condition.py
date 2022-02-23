class Player:

    def __init__(self, Name):
        self.name = Name
        self.B = []
        self.G = []
        self.P = []
        self.Y = []
        self.Rocket = []
        self.mission = []
        self.win_cards = []
        self.captain = False
        self.leader = False
        self.sick = False

    def Print(self):
        print("Player: " + self.name + '\n' + "hand cards: ")
        print(self.B)
        print(self.G)
        print(self.P)
        print(self.Y)
        print(self.Rocket)
        print("mission: ")
        print(self.mission)
        print("win cards: ")
        print(self.win_cards)
        print("sick or not: ")
        print(self.sick)
        print

player_number = 3
Players = []
for i in range(player_number):
    Players.append(Player("player" + str(i)))

total_task = ["B4", "Y3", "B9", "Y2", "P1", "G7"]
num_priority = ["Y3", "0", "P1", "0", "0", "B9"] # can handle omega
arrow_priority = ["B4", "Y2"]
one_mission = ["B1", "Y1", "G1", "P1"]

Players[0].mission = ["Y3", "Y2"]
Players[1].mission = ["B9", "B4", "P1", "G7"]
Players[2].sick = True

def Mission_complete(total_task, num_priority, arrow_priority, Players, winner, win_cards, task_num):
    global one_mission

    if Players[winner].sick: # sick player cannot win
        print("sick player won")
        return -1

    for i in win_cards:

        for j in range(len(Players)): # if other players won your task card, mission failed
            if j != winner:
                if i in Players[j].mission:
                    print("mission target error")
                    return -1

        if i in Players[winner].mission:
            if i in num_priority:
                if task_num != num_priority.index(i):
                    print("number priority order error")
                    return -1
            else:
                if num_priority[task_num] != "0":
                    print("number priority mission error")
                    return -1
            if i in arrow_priority:
                if i == arrow_priority[0]:
                    arrow_priority.remove(i)
                else:
                    print("arrow priority error")
                    return -1
            if i in one_mission:
                one_mission = []
                return task_num + 1
            task_num += 1
            total_task.remove(i)
    return task_num

win_cards_list = [["Y3", "Y6", "Y5"], ["G7", "G5", "G8"], ["P1", "P3", "P7"], ["B4", "B5", "B8"], ["Y1", "Y4", "G3"]]
winner_list = [0, 1, 1, 1, 0]
task_num = 0

index = 0

while index < 5:
    winner = winner_list[index]
    win_cards = win_cards_list[index]
    task_num = Mission_complete(total_task, num_priority, arrow_priority, Players, winner, win_cards, task_num)
    index += 1
    print(task_num)
    if task_num != -1:
        print(total_task)
        print(arrow_priority)
        print(one_mission)
    else:
        break
