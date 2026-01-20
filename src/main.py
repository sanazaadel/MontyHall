
import random
from typing import Tuple


"""
Monty Hall Problem Simulation   
This module simulates the Monty Hall problem, where a contestant
chooses one of three doors, behind one of which is a car (the prize)
and behind the others are goats. After the initial choice, one of the
non-chosen doors with a goat is revealed, and the contestant has the
option to switch their choice to the remaining unopened door or stay
with their initial choice. The simulation runs multiple trials to
determine the win rates for both strategies: switching and staying. 

Functions:
- monty_hall_game(switch: bool) -> bool:
    Simulates a single round of the Monty Hall game.    
- simulate_monty_hall(num_trials: int) -> Tuple[int, int]:
    Simulates multiple rounds and returns the number of wins for both strategies.
"""


def monty_hall_game(switch: bool) -> bool:
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    initial_choice = random.choice(range(3))
    host_options = [i for i in range(3) if i != initial_choice and doors[i] == 'goat']
    revealed_door = random.choice(host_options)
    if switch:
        final_choice = [i for i in range(3) if i != initial_choice and i != revealed_door][0]
    else:
        final_choice = initial_choice
    return doors[final_choice] == 'car'
    

def simulate_monty_hall(num_trials: int) -> Tuple[int, int]:
    wins_switch = sum(monty_hall_game(True) for _ in range(num_trials))
    wins_stay = sum(monty_hall_game(False) for _ in range(num_trials))
    return wins_switch, wins_stay

if __name__ == "__main__":
    switch_win_rate, stay_win_rate = simulate_monty_hall(1000)
    print(f"Win rate when switching: {switch_win_rate:.2%}")
    print(f"Win rate when staying: {stay_win_rate:.2%}")