import random

# mission 24
def Answer24(player, task): # Get an answer from a crew
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

def Choose_24 (players, judge_task): # 
    for i in judge_task:
        Yes = []
        for j in players:
            temp = Answer24(j, i)
            print(j.name + " task: " + i)
            print(temp)
            if temp:
                Yes.append(j)
        
        for k in Yes:
            print(k.name)

        if len(Yes) > 0:
            player = random.choice(Yes)
            player.mission.append(i)
            print(player.name + " gets the task\n")
        else:
            player = random.choice(players)
            player.mission.append(i)
            print(player.name + " gets the task\n")
