from c4 import *
from game_tree import *
from last_minute_player import *
from input_player import *
from heuristic_player import *
from global_functions import *

# change these variables

game_type = ['heuristic', 'last minute']
num_games_if_no_human = 1

# don't change below

human_is_playing = 'input' in game_type
num_games = 1 if human_is_playing else num_games_if_no_human

score = {game_type[0]: 0, game_type[1]: 0, 'tie': 0}

for i in range(2):

    if human_is_playing and i > 0: continue

    for j in range(num_games):

        if human_is_playing and j > 0: continue

        print(f'Running game {j + i*num_games_if_no_human + 1}...')

        players = []
        for player in game_type:
            if player == 'last minute': players.append(LastMinutePlayer())
            if player == 'input':       players.append(InputPlayer())
            if player == 'heuristic':   players.append(HeuristicPlayer(4))

        if i % 2 == 1: players = players[::-1]        

        game = Connect4(players, show_board = human_is_playing)
        game.run_to_completion()

        winner_map = {
            1: game_type[i],
            2: game_type[1 - i],
            'tie': 'tie'
        }

        score[winner_map[game.winner]] += 1

print(score)