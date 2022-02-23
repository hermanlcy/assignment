import random

Large_card = [  'B1','B2','B3','B4','B5','B6','B7','B8','B9',
                'G1','G2','G3','G4','G5','G6','G7','G8','G9',
                'R1','R2','R3','R4','R5','R6','R7','R8','R9',
                'Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9',
                'Rocket1','Rocket2','Rocket3','Rocket4',
                ]

class Player:

    def __init__(self, Name):
        self.name = Name
        self.B = []
        self.G = []
        self.R = []
        self.Y = []
        self.Rocket = []
        self.mission = []
        self.win_cards = []
        self.captain = False
        self.leader = False

    def Print(self):
        print("Player: " + self.name + '\n' + "hand cards: ")
        print(self.B)
        print(self.G)
        print(self.R)
        print(self.Y)
        print(self.Rocket)
        print("mission: ")
        print(self.mission)
        print("win cards: ")
        print(self.win_cards)
        print

def AssignHandCard(player1, cards):
    for i in cards:
        if len(i) > 2:
            player1.Rocket.append(i)
            if i == "Rocket4":
                player1.captain = True
                player1.leader = True
        elif i[0] == 'R':
            player1.R.append(i)
        elif i[0] == 'G':
            player1.G.append(i)
        elif i[0] == 'Y':
            player1.Y.append(i)
        else:
            player1.B.append(i)
    player1.B.sort()
    player1.Y.sort()
    player1.G.sort()
    player1.R.sort()
    player1.Rocket.sort()

random.shuffle(Large_card)

player_number = 3
Players = []
for i in range(player_number):
    Players.append(Player("player" + str(i)))

individual_card = 40/player_number

for i in range(player_number):
    player_card = Large_card[i*individual_card:(i+1)*individual_card]
    if player_number == 3 and i == 0:
        player_card.insert(0, Large_card[-1])
        player_card.sort()
        AssignHandCard(Players[i], player_card)
    else:
        player_card.sort()
        AssignHandCard(Players[i], player_card)

Players[0].Print()
Players[1].Print()
Players[2].Print()

def Random_play(player):
    cards = player.B + player.Y + player.G + player.R
    if len(cards) != 0:
        card = random.choice(cards)
    else:
        card = random.choice(player.Rocket)

    if len(card) > 2:
        player.Rocket.remove(card)
    elif card[0] == 'R':
        player.R.remove(card)
    elif card[0] == 'G':
        player.G.remove(card)
    elif card[0] == 'Y':
        player.Y.remove(card)
    else:
        player.B.remove(card)
    return card

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
    elif color == 'R':
        if len(player.R) != 0:
            card = random.choice(player.R)
            player.R.remove(card)
        else:
            card = Random_play(player)
    else:
        card = Random_play(player)

    return card
    
# Players[0].Print()
# card = Player_card(Players[0], 'Unknown')
# print(Players[0].name + " played card: " + card + '\n')
# Players[0].Print()

desk = ["Unknow" for i in range(player_number)] # store the cards are played in this round
leader = -1
num_round = 1

for i in range(len(Players)): # find the leader index
    if Players[i].leader == True:
        leader = i

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

    num_hand = Players[-1].R + Players[-1].Y + Players[-1].G + Players[-1].B + Players[-1].Rocket
    if len(num_hand) != 0:
        Player_round(Players, leader, num_round) 

Player_round(Players, leader, num_round)

Players[0].Print()
Players[1].Print()
Players[2].Print()
