import random

large_card = [
    'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
    'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
    'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9',
    'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9',
    'Rocket1', 'Rocket2', 'Rocket3', 'Rocket4',
]

def test(num, task, index):
    print 'Test' + str(num) + ':'
    print '\tTask:' + str(task)
    print '\tBad index: ' + str(index)
    get_pass_condition(task, index)

def get_pass_condition(task, index):
    if len(task[index]) > 2:
        for i in task:
            if len(i) > 2 and int(i[-1]) > int(task[index][-1]):
                print '\tSick player did not win the trick. Test passed!'
                break
            elif task[index] == i:
                pass
            else:
                print '\tMission failed!'
                break
    else:
        for i in task:
            if len(i) > 2:
                print '\tSick player did not win the trick. Test passed!'
                break
            #e.g. B1, B4
            elif i[0] == task[index][0] and int(i[1]) > int(task[index][1]):
                print '\tSick player did not win the trick. Test passed!'
                break
            elif index != 0 and i[0] != task[index][0]:
                print '\tSick player did not win the trick. Test passed!'
                break
            elif task[index] == i:
                pass
            else:
                print '\tMission failed!'
                break

if __name__ == '__main__':
    for i in range(1, 6):
        task_list = []

        for j in range(5):
            ele = random.choice(large_card)

            if ele not in task_list:
                task_list.append(ele)
    
        index = random.randint(0, len(task_list) - 1)

        test(i, task_list, index)
