import random


num_of_Token = [0,0,2,0,0,2,0,3,0,0,
                1,0,0,3,4,0,0,0,1,0,
                2,4,5,0,2,0,0,1,0,3,
                3,0,0,0,3,2,0,0,3,3,
                0,0,0,0,3,0,0,0,3,0
               ]



def priority_define(judge_task, mission): 

    NPN = num_of_Token[mission-1]        #NPN: number priority number
    print "Token number", NPN
    priority_tasks = random.sample(judge_task, NPN)
    random.shuffle(priority_tasks)
    priority_list = priority_tasks


    print("------------------ Priority list -------------------------------")
    print priority_list
    return priority_list


def priority_omage_define(judge_task, priority_list): 
    temp = priority_list[0]
    judge_task.remove(temp)
    temp1 = random.sample(judge_task, 1)
    judge_task.append(temp)
    omage_task = temp1[0]


    print("------------------ Omage Task -------------------------------")
    print omage_task
    return omage_task

def omage_define(judge_task): 
    temp = random.sample(judge_task, 1)
    omage_task = temp[0]



    print("------------------ Omage Task -------------------------------")
    print omage_task
    return omage_task




def priority_exchange(priority_list): 
    print "Exchange Two Tokens"
    temp = random.sample(priority_list, 2)
    temp1 = temp[0]
    temp2 = temp[1]
    N1 = priority_list.index(temp1)
    N2 = priority_list.index(temp2)
    priority_list[N1], priority_list[N2] = priority_list[N2], priority_list[N1]
    print("--------------New Priority list -------------------------------")
    print priority_list
    return priority_list

def priority_exchange1(priority_list, all_task): 
    print "Change one Tokens to a unchosen task"
    temp1 = random.sample(priority_list, 1)
    temp11 = temp1[0]
    N1 = priority_list.index(temp11)
    other_task =  [i for i in priority_list + all_task if i not in priority_list or i not in all_task]
    temp2 = random.sample(other_task, 1)
    temp22 = temp2[0]
    priority_list[N1] = temp22
    print("--------------New Priority list -------------------------------")
    print priority_list
    return priority_list

