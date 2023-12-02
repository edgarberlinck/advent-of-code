from modules.rock_game import Game, score_matching_games, get_total_power_of_minimun_rocks

with open('./files/day-2/input.txt') as file_lines:
    games = file_lines.read().splitlines()

target_game = Game(0, reds = 12, greens = 13, blues = 14)

response_challenge_1 = score_matching_games(games, target_game)

print(response_challenge_1)

response_challenge_2 = get_total_power_of_minimun_rocks(games)

print(response_challenge_2)
