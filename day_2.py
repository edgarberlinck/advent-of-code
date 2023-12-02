from modules.rock_game import Parser, Game, score_matching_games

with open('./files/day-2/input.txt') as file_lines:
    games = file_lines.read().splitlines()

target_game = Game(0, reds = 12, greens = 13, blues = 14)

response = score_matching_games(games, target_game)

print(response)