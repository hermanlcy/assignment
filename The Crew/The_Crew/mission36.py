import random

# mission 36
def Answer36(player, task):
    color = task[0]
    if color == 'P':
        if int(task[1]) > 7:
            return task in player.P
        else:
            if task in player.P:
                return False
            else:
                if len(player.P) > 0:
                    return int(player.P[-1][-1]) > 7
                else:
                    return False 

    elif color == 'G':
        if int(task[1]) > 7:
            return task in player.G
        else:
            if task in player.G:
                return False
            else:
                if len(player.G) > 0:
                    return int(player.G[-1][-1]) > 7
                else:
                    return False 

    elif color == 'Y':
        if int(task[1]) > 7:
            return task in player.Y
        else:
            if task in player.Y:
                return False
            else:
                if len(player.Y) > 0:
                    return int(player.Y[-1][-1]) > 7
                else:
                    return False  
    else:
        if int(task[1]) > 7:
            return task in player.B
        else:
            if task in player.B:
                return False
            else:
                if len(player.B) > 0:
                    return int(player.B[-1][-1]) > 7
                else:
                    return False 

def Choose_36 (players, judge_task):

    print(judge_task)
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
    