import random

# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hand_player = []
hand_cpu = []
total_score_player = 0
total_score_cpu = 0
cpu_turn = 0
game_ended = 0

# Functions
def you_lose():
    global game_ended
    print(f"You lose! \nPlayer: {hand_player} Total: {total_score_player} CPU: {hand_cpu} Total: {total_score_cpu}")
    game_ended = 1

def you_win():
    global game_ended
    print(f"You win! \nPlayer: {hand_player} Total: {total_score_player} CPU: {hand_cpu} Total: {total_score_cpu}")
    game_ended = 1

def hit(hand):
    card = pick_card()
    hand.append(card)
    return hand

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def pick_card():
    return random.choice(cards)

def initial_hands():
    global hand_player, hand_cpu, total_score_player, total_score_cpu
    hand_player = hit(hand_player)
    hand_player = hit(hand_player)
    hand_cpu = hit(hand_cpu)
    hand_cpu = hit(hand_cpu)
    total_score_player = calculate_score(hand_player)
    total_score_cpu = hand_cpu[0]  # CPU shows only the first card initially
    return

# Initialize hands
initial_hands()

# Game loop
while game_ended == 0:
    print(f"Player hand: {hand_player} Total: {total_score_player}")
    if cpu_turn == 0:
        print(f"CPU hand: [{hand_cpu[0]}, x] Total: {total_score_cpu}")
        player_choice = input("Do you want another card? (yes/no) \n").lower()
        if player_choice == "yes":
            hand_player = hit(hand_player)
            total_score_player = calculate_score(hand_player)
            if total_score_player > 21:
                you_lose()
        elif player_choice == "no":
            cpu_turn = 1
    else:
        total_score_cpu = calculate_score(hand_cpu)
        while total_score_cpu < 17:
            hand_cpu = hit(hand_cpu)
            total_score_cpu = calculate_score(hand_cpu)
            print(f"CPU hand: {hand_cpu} Total: {total_score_cpu}")
        
        if total_score_cpu > 21:
            you_win()
        elif total_score_cpu > total_score_player:
            you_lose()
        elif total_score_cpu < total_score_player:
            you_win()
        else:
            print(f"Draw! \nPlayer: {hand_player} Total: {total_score_player} CPU: {hand_cpu} Total: {total_score_cpu}")
            game_ended = 1
        break
