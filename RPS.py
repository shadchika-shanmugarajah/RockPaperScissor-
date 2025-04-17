def player(prev_play, opponent_history=[], my_history=[], strategy_state={"strategy": None}):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "P"

    # Strategy identification
    if opponent_history.count("R") >= 0.8 * len(opponent_history):
        strategy_state["strategy"] = "counter_R"
    elif "".join(opponent_history[-3:]) in ["RPS", "PSR", "SRP"]:
        strategy_state["strategy"] = "cycle"
    elif len(opponent_history) >= 4 and len(my_history) >= 3 and opponent_history[-1] == counter_move(my_history[-3]):
        strategy_state["strategy"] = "memory_counter"
    else:
        strategy_state["strategy"] = "frequency"

    if strategy_state["strategy"] == "counter_R":
        move = "P"
    elif strategy_state["strategy"] == "cycle":
        last = opponent_history[-1]
        prediction = {"R": "P", "P": "S", "S": "R"}[last]
        move = counter_move(prediction)
    elif strategy_state["strategy"] == "memory_counter":
        predicted = opponent_history[-3]
        move = counter_move(predicted)
    else:
        most_common = max(set(opponent_history), key=opponent_history.count)
        move = counter_move(most_common)

    my_history.append(move)
    return move

def counter_move(move):
    return {"R": "P", "P": "S", "S": "R"}[move]
