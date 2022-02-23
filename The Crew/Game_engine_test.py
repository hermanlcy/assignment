import random




Large_card = [  
                {"ID": "B1L", "Color": "Blue", "Value": 1, "Match": "B1S", "Owner": 0}, 
                {"ID": "B2L", "Color": "Blue", "Value": 2, "Match": "B2S", "Owner": 0}, 
                {"ID": "B3L", "Color": "Blue", "Value": 3, "Match": "B3S", "Owner": 0}, 
                {"ID": "B4L", "Color": "Blue", "Value": 4, "Match": "B4S", "Owner": 0}, 
                {"ID": "B5L", "Color": "Blue", "Value": 5, "Match": "B5S", "Owner": 0}, 
                {"ID": "B6L", "Color": "Blue", "Value": 6, "Match": "B6S", "Owner": 0}, 
                {"ID": "B7L", "Color": "Blue", "Value": 7, "Match": "B7S", "Owner": 0}, 
                {"ID": "B8L", "Color": "Blue", "Value": 8, "Match": "B8S", "Owner": 0}, 
                {"ID": "B9L", "Color": "Blue", "Value": 9, "Match": "B9S", "Owner": 0}, 

                {"ID": "G1L", "Color": "Green", "Value": 1, "Match": "G1S", "Owner": 0}, 
                {"ID": "G2L", "Color": "Green", "Value": 2, "Match": "G2S", "Owner": 0}, 
                {"ID": "G3L", "Color": "Green", "Value": 3, "Match": "G3S", "Owner": 0}, 
                {"ID": "G4L", "Color": "Green", "Value": 4, "Match": "G4S", "Owner": 0}, 
                {"ID": "G5L", "Color": "Green", "Value": 5, "Match": "G5S", "Owner": 0}, 
                {"ID": "G6L", "Color": "Green", "Value": 6, "Match": "G6S", "Owner": 0}, 
                {"ID": "G7L", "Color": "Green", "Value": 7, "Match": "G7S", "Owner": 0}, 
                {"ID": "G8L", "Color": "Green", "Value": 8, "Match": "G8S", "Owner": 0}, 
                {"ID": "G9L", "Color": "Green", "Value": 9, "Match": "G9S", "Owner": 0}, 

                {"ID": "P1L", "Color": "Pink", "Value": 1, "Match": "P1S", "Owner": 0}, 
                {"ID": "P2L", "Color": "Pink", "Value": 2, "Match": "P2S", "Owner": 0}, 
                {"ID": "P3L", "Color": "Pink", "Value": 3, "Match": "P3S", "Owner": 0}, 
                {"ID": "P4L", "Color": "Pink", "Value": 4, "Match": "P4S", "Owner": 0}, 
                {"ID": "P5L", "Color": "Pink", "Value": 5, "Match": "P5S", "Owner": 0}, 
                {"ID": "P6L", "Color": "Pink", "Value": 6, "Match": "P6S", "Owner": 0}, 
                {"ID": "P7L", "Color": "Pink", "Value": 7, "Match": "P7S", "Owner": 0}, 
                {"ID": "P8L", "Color": "Pink", "Value": 8, "Match": "P8S", "Owner": 0}, 
                {"ID": "P9L", "Color": "Pink", "Value": 9, "Match": "P9S", "Owner": 0}, 

                {"ID": "Y1L", "Color": "Yellow", "Value": 1, "Match": "Y1S", "Owner": 0}, 
                {"ID": "Y2L", "Color": "Yellow", "Value": 2, "Match": "Y2S", "Owner": 0}, 
                {"ID": "Y3L", "Color": "Yellow", "Value": 3, "Match": "Y3S", "Owner": 0}, 
                {"ID": "Y4L", "Color": "Yellow", "Value": 4, "Match": "Y4S", "Owner": 0}, 
                {"ID": "Y5L", "Color": "Yellow", "Value": 5, "Match": "Y5S", "Owner": 0}, 
                {"ID": "Y6L", "Color": "Yellow", "Value": 6, "Match": "Y6S", "Owner": 0}, 
                {"ID": "Y7L", "Color": "Yellow", "Value": 7, "Match": "Y7S", "Owner": 0}, 
                {"ID": "Y8L", "Color": "Yellow", "Value": 8, "Match": "Y8S", "Owner": 0}, 
                {"ID": "Y9L", "Color": "Yellow", "Value": 9, "Match": "Y9S", "Owner": 0}, 

                {"ID": "R1", "Color": "Rocket", "Value": 10, "Match": "None", "Owner": 0}, 
                {"ID": "R2", "Color": "Rocket", "Value": 11, "Match": "None", "Owner": 0}, 
                {"ID": "R3", "Color": "Rocket", "Value": 12, "Match": "None", "Owner": 0}, 
                {"ID": "R4", "Color": "Rocket", "Value": 13, "Match": "None", "Owner": 0}]

Small_card = ["B1S", "B2S", "B3S", "B4S", "B5S", "B6S", "B7S", "B8S", "B9S"
            , "G1S", "G2S", "G3S", "G4S", "G5S", "G6S", "G7S", "G8S", "G9S"
            , "P1S", "P2S", "P3S", "P4S", "P5S", "P6S", "P7S", "P8S", "P9S"
            , "Y1S", "Y2S", "Y3S", "Y4S", "Y5S", "Y6S", "Y7S", "Y8S", "Y9S"]    


# print "All Large card:"
# print(Large_card)


#####################################################################################################
# print '#############################################################################################'
#####################################################################################################

#Large_card = ['B1L', 'B3L', 'B6L', 'G2L', 'G4L', 'G7L', 'G9L', 'P1L', 'P3L', 'P8L', 'P9L', 'R4', 'Y5L', 'Y6L', 'B2L', 'B8L', 'G1L', 'G5L', 'G6L', 'P5L', 'P7L', 'Y1L', 'Y2L', 'Y4L', 'Y7L', 'Y8L', 'Y9L', 'B4L', 'B5L', 'B7L', 'B9L', 'G3L', 'G8L', 'P2L', 'P4L', 'P6L', 'R1', 'R2', 'R3', 'Y3L']


random.shuffle(Large_card)
# print "Random cards:"
# print(Large_card)

#####################################################################################################
# print '#############################################################################################'
#####################################################################################################

player_number= 3
# player = 4
# print 'Player: ',player_number
individual_card = 40/player_number
# print 'Individaul card number: ', individual_card

#####################################################################################################
# print '#############################################################################################'
#####################################################################################################

assigned_card = []
for i in range(player_number):
    player_card = Large_card[i*individual_card:(i+1)*individual_card]
    if player_number == 3 and i == 0:
        # print Large_card[-1]
        player_card.insert(0, Large_card[-1])
        player_card.sort()
        assigned_card.append(player_card)
    else:
        player_card.sort()
        assigned_card.append(player_card)
    
# print 'Assigned_card:' 
#print assigned_card 
# print('\n'.join(map(str, assigned_card)))

#####################################################################################################
# print '#############################################################################################'
#####################################################################################################

player_INFO = []
for i in range(player_number):
    temp = {"Player_ID": i + 1, "Cards": assigned_card[i], "Mission_cards": [], "Captain": False, "Round_turn": i + 1, "Completed_mission": [], "trick_win_cards":[]}
    player_INFO.append(temp)

#print player_INFO
# print('\n'.join(map(str, player_INFO)))

#####################################################################################################
# print '#############################################################################################'
#####################################################################################################

for single_player in player_INFO:
    temp_card = single_player["Cards"]
    if {"ID": "R4", "Color": "Rocket", "Value": 13, "Match": "None", "Owner": 0}in temp_card:
        captain = player_INFO.index(single_player)
        # print 'Rocket 4 is in player' 
        # print captain + 1 
        single_player["Captain"] = True
        # print single_player

#####################################################################################################
# print '#############################################################################################'
#####################################################################################################

crew = player_INFO[:captain]
captain_team = player_INFO[captain:]
# print crew
# print captain_team
player_reorder_INFO = captain_team + crew
# print reorder_card
for single_player in player_reorder_INFO:
    single_player["Round_turn"] = player_reorder_INFO.index(single_player) + 1
# print('\n'.join(map(str, player_reorder_INFO)))

#####################################################################################################
# print '#############################################################################################'
#####################################################################################################

task_number = 1
task = random.sample(Small_card, task_number)
# print(task)   

#####################################################################################################
# print '#############################################################################################'
#####################################################################################################

assigned_task = []
for i in range(player_number):
    assigned_task.append([])

judge_task = []


task_index = 0



while task_index < task_number:

    choice = random.choice(task)

    assigned_task[task_index%player_number].append(choice)

    judge_task.append(choice)

    player_reorder_INFO[task_index%player_number]["Mission_cards"].append(choice)

    task.remove(choice)

    task_index +=1

# print 'Assigned_task:'
# print assigned_task
# print judge_task


#####################################################################################################
# print '#############################################################################################'
#####################################################################################################

for single_player in player_reorder_INFO:
    temp_card = single_player["Cards"]
    for single_card in temp_card:
        single_card["Owner"] = single_player["Player_ID"]


#####################################################################################################
print ('#############################################################################################')
#####################################################################################################

print('\n'.join(map(str, player_reorder_INFO)))

#####################################################################################################
print ('#############################################################################################')
#####################################################################################################

trick = []
#for i in range(1):
for i in range(40/player_number):
    print ("Round", i + 1, ":")
    for single_player in player_reorder_INFO:
        if single_player["Round_turn"] == 1:
            player_option = single_player["Cards"]
            leader_card = random.choice(player_option)
            player_option.remove(leader_card)
            single_player["Cards"] = player_option
            trick.append(leader_card)
        else:
            player_option = single_player["Cards"]
            follow_card = random.choice(player_option)
            player_option.remove(follow_card)
            single_player["Cards"] = player_option
            trick.append(follow_card)

    print('\n'.join(map(str, trick)))

    ###############################################

    cards_value = []
    for card in trick:
        cards_value.append(card["Value"])
    print (cards_value) 
    max_value = max(cards_value)
    print (max_value)

    for card in trick:
        if card["Value"] == max_value:
            winner = card["Owner"]
    
    print ("Player", winner, "win the trick")

    for single_player in player_reorder_INFO:
        if single_player["Player_ID"] == winner:
            single_player["trick_win_cards"].extend(trick)

    ##############################################
    print ('#######################################')
    ##############################################

    print('\n'.join(map(str, player_reorder_INFO)))

    ##############################################
    print ('#######################################')
    ##############################################

    for single_player in player_reorder_INFO:
        # print single_player
        # print single_player["trick_win_cards"]
        for single_trick_card in single_player["trick_win_cards"]:
            for single_mission_card in single_player["Mission_cards"]:
                if single_trick_card["Match"] == single_mission_card:
                    print ("Mission"), single_mission_card, "Completed"
                    judge_task.remove(single_mission_card)


    ##############################################
    print ('#######################################')
    ##############################################

    if len(judge_task) == 0:
        print ("All mission Complete")
        break

    if i == (40/player_number - 1):
        print ("Not all mission Complete, mission fail")
        break

    trick = []

    



























