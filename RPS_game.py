import random

def play(player1, player2, num_games, verbose=False):
    p1_score = 0
    p2_score = 0
    tie_score = 0

    p1_prev = ""
    p2_prev = ""

    for i in range(num_games):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if verbose:
            print(f"Game {i + 1}:")
            print(f"Player 1: {p1_move}  |  Player 2: {p2_move}")

        if p1_move == p2_move:
            tie_score += 1
            if verbose:
                print("Tie!")
        elif (
            (p1_move == "R" and p2_move == "S") or
            (p1_move == "S" and p2_move == "P") or
            (p1_move == "P" and p2_move == "R")
        ):
            p1_score += 1
            if verbose:
                print("Player 1 wins!")
        else:
            p2_score += 1
            if verbose:
                print("Player 2 wins!")

        p1_prev = p1_move
        p2_prev = p2_move

    print("Results:")
    print(f"Player 1: {p1_score} / {num_games}")
    print(f"Player 2: {p2_score} / {num_games}")
    print(f"Ties: {tie_score} / {num_games}")

def quincy(prev_play):
    return "R"

def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        guess = "R"
    else:
        guess = max(set(opponent_history[-5:]), key=opponent_history[-5:].count)

    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[guess]

def kris(prev_play, counter=[0]):
    moves = ["R", "P", "S"]
    play = moves[counter[0] % 3]
    counter[0] += 1
    return play

def abbey(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        guess = "R"
    else:
        guess = opponent_history[-3]

    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[guess]
