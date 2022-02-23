import random


# Large_card include 40 cards, Task_card include 36 task cards
Large_card = [  'B1','B2','B3','B4','B5','B6','B7','B8','B9',
                'G1','G2','G3','G4','G5','G6','G7','G8','G9',
                'P1','P2','P3','P4','P5','P6','P7','P8','P9',
                'Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9',
                'Rocket1','Rocket2','Rocket3','Rocket4',
                ]
Task_card = Large_card[:36]

# Player class includes all the attributes, all attributes can be print easily by typing Players[i].Print()
class Player:

    def __init__(self, Name):
        self.name = Name
        self.B = []
        self.G = []
        self.P = []
        self.Y = []
        self.Rocket = []
        self.task = []
        self.win_cards = []
        self.captain = False
        self.leader = False

    def Print(self):
        print("Player: " + self.name + '\n' + "hand cards: ")
        print(self.B)
        print(self.G)
        print(self.P)
        print(self.Y)
        print(self.Rocket)
        print("task: ")
        print(self.task)
        print("win cards: ")
        print(self.win_cards)
        print

# Resort_Hand_Card function not only resort the cards by color, but also includes the function of determining the captain
def Resort_Hand_Card(player, cards):
    for i in cards:
        if len(i) > 2:
            player.Rocket.append(i)
            if i == "Rocket4":
                player.captain = True
                player.leader = True
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

# Shuffling the cards
random.shuffle(Large_card)

# Define the player numbers, works for 2-5 players
player_number = 3
Players = []
for i in range(player_number):
    Players.append(Player("player" + str(i)))

# Number of cards per player
individual_card = 40/player_number

# Assign average cards for each player, player 0 will have 14 cards when there are 3 players
for i in range(player_number):
    player_card = Large_card[i*individual_card:(i+1)*individual_card]
    if player_number == 3 and i == 0:
        player_card.insert(0, Large_card[-1])
        player_card.sort()
        Resort_Hand_Card(Players[i], player_card)
    else:
        player_card.sort()
        Resort_Hand_Card(Players[i], player_card)

# Players[0].Print()
# Players[1].Print()
# Players[2].Print()

print ('#############################################################################################')
print ("Assign 40 cards to each players:")
print
for i in range(player_number):
    Players[i].Print()


print ('#############################################################################################')

# Define the task numbers, works for 1-9 tasks
task_number = 2
task_list = random.sample(Task_card, task_number)
print (task_number, "task(s) selected")


print ('#############################################################################################')

# Resort_task_Card function not only resort the cards
def Resort_task_Card(player, cards):
    for i in cards:
        player.task.append(i)
    player.task.sort()

# Each player should choose one task one by one
assigned_task = []
for i in range(player_number):
    assigned_task.append([])

judge_task = []
task_index = 0

while task_index < task_number:
    choice = random.choice(task_list)
    assigned_task[task_index%player_number].append(choice)
    judge_task.append(choice)
    task_list.remove(choice)
    task_index +=1

# print 'Assigned_task:'
# print assigned_task
# print judge_task

# Assign the chosen tasks to each player
for i in range(player_number):
    player_task_card = assigned_task[i]
    print (player_task_card)
    Resort_task_Card(Players[i], player_task_card)

# Players[0].Print()
# Players[1].Print()
# Players[2].Print()

print ("Assign the chosen tasks to each player")
for i in range(player_number):
    Players[i].Print()



print ('#############################################################################################')


# Random_play function ask the player to give a card randomly, it will also be remove in the player class
def Random_play(player):
    cards = player.B + player.Y + player.G + player.P
    if len(cards) != 0:
        card = random.choice(cards)
    else:
        card = random.choice(player.Rocket)

    if len(card) > 2:
        player.Rocket.remove(card)
    elif card[0] == 'P':
        player.P.remove(card)
    elif card[0] == 'G':
        player.G.remove(card)
    elif card[0] == 'Y':
        player.Y.remove(card)
    else:
        player.B.remove(card)
    return card

# Player_card function ask the player to give a card based on the color condition
def Player_card(player, color):
    card = ''
    if color == "Rocket":
        if len(player.Rocket) != 0:
            card = random.choice(player.Rocket)
            player.Rocket.remove(card)
        else:
            card = Random_play(player)
    elif color == 'B':
        if len(player.B) != 0:
            card = random.choice(player.B)
            player.B.remove(card)
        else:
            card = Random_play(player)
    elif color == 'Y':
        if len(player.Y) != 0:
            card = random.choice(player.Y)
            player.Y.remove(card)
        else:
            card = Random_play(player)
    elif color == 'G':
        if len(player.G) != 0:
            card = random.choice(player.G)
            player.G.remove(card)
        else:
            card = Random_play(player)
    elif color == 'P':
        if len(player.P) != 0:
            card = random.choice(player.P)
            player.P.remove(card)
        else:
            card = Random_play(player)
    else:
        card = Random_play(player)

    return card
    
# Players[0].Print()
# card = Player_card(Players[0], 'Unknown')
# print(Players[0].name + " played card: " + card + '\n')
# Players[0].Print()

# store the cards are played in this round
desk = ["Unknow" for i in range(player_number)]
leader = -1
num_round = 1

# find the leader index
for i in range(len(Players)):
    if Players[i].leader == True:
        leader = i

# Player_round is the main function of the whole game operation,
def Player_round(Players, leader, num_round):

    print("Round %d: "%(num_round))
    num_round += 1

    num_players = len(Players)
    Players[leader].leader = False

    card = Player_card(Players[leader], "random")
    print(Players[leader].name + " played card: " + card + '\n')
    desk[leader] = card
    leader = (leader + 1) % num_players # trun to next player


    if len(card) > 2:
        color = "Rocket"
    else:
        color = card[0]
    
    for i in range(num_players-1):
        card = Player_card(Players[leader], color)
        desk[leader] = card
        print(Players[leader].name + " played card: " + card + '\n')
        leader = (leader + 1) % num_players # trun to next player

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
        
    Players[leader].leader = True
    Players[leader].win_cards += desk
    Players[leader].win_cards.sort()

    print("This round winner is " + Players[leader].name + '\n')
    print("The winned cards are: ")
    print(desk)
    print


    #Task Completed checked, if task is completed it will be remove from judge_task
    for single_trick_card in Players[leader].win_cards:
        for single_task_card in Players[leader].task:
            if single_task_card == single_trick_card:
                print ("Task", single_task_card, "Completed")
                Players[leader].task.remove(single_task_card)
                judge_task.remove(single_task_card)
                # print judge_task
            
    print("####################################")

    if len(judge_task) == 0:
        print ("All mission Complete")

    else:
        if num_round == (40/player_number + 1):
            print ("Not all task Complete, Mission fail")
            print ("Remaining cards", judge_task)
        else:
            # countine until as long as the game is not over
            num_hand = Players[-1].P + Players[-1].Y + Players[-1].G + Players[-1].B + Players[-1].Rocket
            Player_round(Players, leader, num_round)

    # num_hand = Players[-1].P + Players[-1].Y + Players[-1].G + Players[-1].B + Players[-1].Rocket
    # if len(num_hand) != 0:
    #     Player_round(Players, leader, num_round)


print ("Game start")

Player_round(Players, leader, num_round)


print ('#############################################################################################')


# Players[0].Print()
# Players[1].Print()
# Players[2].Print()

print ("Player status after the game is over:")

for i in range(player_number):
    Players[i].Print()
