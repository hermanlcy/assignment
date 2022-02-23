import random
# mission (15), 16, 17, 24, 27, (29), (33-37), (40-41), (43-46), (49-50) not update yet
# communicate once per mission
# always communicate ASAP
# to maximize the benefit of communicating
# b/c we don't know when the mission will be completed

# the first priority of choosing the card to communicate
# will always base on the hand task card

# if the choosing card has not been played
# it will show the message in each round

# 1 = communication token fully functional
# 0 = dead zone/ limited (cannot indicate highest/lowest/only one)
# -1 = disable
# -(i) = disrupted i round (i < -1)
usage = [
    1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
    -1, 1, 1, 0, 1, 1, 1, -2, -3, 1,
    0, 1, 1, 1, 0, 1, 1, -3, 0, -2,
    1, 1, 1, 1, 1, 1, 1, -3, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
]


def communicating(player, mission, round, communicated):
    if player.volunteer == True:
        communicated += 1

        return communicated

    cards = player.B + player.G + player.P + player.Y
    round -= 1
    random_pick = []
    if len(player.B) == 1:
        random_pick.append("The only B card " + max(player.B))
    if len(player.B) >= 2:
        random_pick.append("Largest B card " + max(player.B))
        random_pick.append("Smallest B card " + min(player.B))
    if len(player.G) == 1:
        random_pick.append("The only G card " + max(player.G))
    if len(player.G) >= 2:
        random_pick.append("Largest G card " + max(player.G))
        random_pick.append("Smallest G card " + min(player.G))
    if len(player.P) == 1:
        random_pick.append("The only P card " + max(player.P))
    if len(player.P) >= 2:
        random_pick.append("Largest P card " + max(player.P))
        random_pick.append("Smallest P card " + min(player.P))
    if len(player.Y) == 1:
        random_pick.append("The only Y card " + max(player.Y))
    if len(player.Y) >= 2:
        random_pick.append("Largest Y card " + max(player.Y))
        random_pick.append("Smallest Y card " + min(player.Y))

    # communication is not allowed
    if usage[mission - 1] == -1:
        player.communication = "disable"
    # least card has been played
    elif len(cards) == 0:
        player.communication = "no hand card"

    # normal mission
    elif usage[mission - 1] == 1:
        if len(player.task) == 0:
            player.communication = random.choice(random_pick)
            communicated += 1
        elif 'B' in player.task[0] and len(player.B) != 0:
            player.communication = random.choice(random_pick)
            communicated += 1
        elif 'G' in player.task[0] and len(player.G) != 0:
            player.communication = random.choice(random_pick)
            communicated += 1
        elif 'P' in player.task[0] and len(player.P) != 0:
            player.communication = random.choice(random_pick)
            communicated += 1
        elif 'Y' in player.task[0] and len(player.Y) != 0:
            player.communication = random.choice(random_pick)
            communicated += 1
        else:
            player.communication = random.choice(random_pick)
            communicated += 1

    # communication token activate after round #
    elif usage[mission - 1] < -1:
        if round >= abs(usage[mission - 1]):
            if len(player.task) == 0:
                player.communication = random.choice(random_pick)
                communicated += 1
            elif 'B' in player.task[0] and len(player.B) != 0:
                player.communication = random.choice(random_pick)
                communicated += 1
            elif 'G' in player.task[0] and len(player.G) != 0:
                player.communication = random.choice(random_pick)
                communicated += 1
            elif 'P' in player.task[0] and len(player.P) != 0:
                player.communication = random.choice(random_pick)
                communicated += 1
            elif 'Y' in player.task[0] and len(player.Y) != 0:
                player.communication = random.choice(random_pick)
                communicated += 1
            else:
                player.communication = random.choice(random_pick)
                communicated += 1
        else:
            player.communication = "cannot communicate until round %d " % abs(usage[mission - 1])

    # dead zone
    elif usage[mission - 1] == 0:
        no_signal = []
        if len(player.B) == 1:
            no_signal.append(max(player.B))
        if len(player.B) >= 2:
            no_signal.append(max(player.B))
            no_signal.append(min(player.B))
        if len(player.G) == 1:
            no_signal.append(max(player.G))
        if len(player.G) >= 2:
            no_signal.append(max(player.G))
            no_signal.append(min(player.G))
        if len(player.P) == 1:
            no_signal.append(max(player.P))
        if len(player.P) >= 2:
            no_signal.append(max(player.P))
            no_signal.append(min(player.P))
        if len(player.Y) == 1:
            no_signal.append(max(player.Y))
        if len(player.Y) >= 2:
            no_signal.append(max(player.Y))
            no_signal.append(min(player.Y))

        if len(player.task) == 0:
            player.communication = random.choice(no_signal)
            communicated += 1
        elif 'B' in player.task[0] and len(player.B) != 0:
            player.communication = random.choice(no_signal)
            communicated += 1
        elif 'G' in player.task[0] and len(player.G) != 0:
            player.communication = random.choice(no_signal)
            communicated += 1
        elif 'P' in player.task[0] and len(player.P) != 0:
            player.communication = random.choice(no_signal)
            communicated += 1
        elif 'Y' in player.task[0] and len(player.Y) != 0:
            player.communication = random.choice(no_signal)
            communicated += 1
        else:
            player.communication = random.choice(no_signal)
            communicated += 1
    return communicated

def assign_communication_cards(players, current_player_id, num_round, communicated):
    for i in range(len(players)):
        i = i + 1
        communicated = communicating(players[current_player_id], 33, num_round, communicated)
        print("Player " + players[current_player_id].name + " communicating: " + players[current_player_id].communication)
        current_player_id = (current_player_id + 1) % len(players)
