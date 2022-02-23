import random


# mission 27
# Commander decides one player should take all the three task cards.
# Commander can decide whether he take the tasks because he know his own cards
def Answer(player, task):  # Get an answer from a crew
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

def Choose_27(Players, total_task):
    captain = -1
    trash = []
    for i in range(len(Players)):
        trash.append(i)

    for i in range(len(Players)):
        if Players[i].captain:
            captain = i  # index of captain
            trash.remove(captain)
            print("captain is NO." + str(captain))
            print(trash)
    count = 0
    for i in total_task:
        temp = Answer(Players[captain], i)
        if temp:
            count += 1
    if count >= 2:
        for i in total_task:
            Players[captain].mission.append(i)
        print("captain handles the task")
    else:
        player = random.choice(trash)
        Players[player].mission.append(i)
        print(Players[player].name + " handles the task")
