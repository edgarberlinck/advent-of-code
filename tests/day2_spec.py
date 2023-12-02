import unittest
from modules.rock_game import Parser, Game, score_matching_games

class PuzzleGame(unittest.TestCase):
  def setUp(self) -> None:
    self.expected_game = {
      'red': 12,
      'green': 13,
      'blue': 14
    }
    self.game = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    self.parsed_game = Parser(self.game)
  
  def test_game_obj(self):
    game = Game(0, reds = 12, greens = 13, blues = 14)
    
    self.assertEqual(game.reds, 12)
    self.assertEqual(game.greens, 13)  
    self.assertEqual(game.blues, 14)
    
  def test_game_parser(self):
    self.assertEqual(self.parsed_game.game_id, 1)
    self.assertEqual(self.parsed_game.red_stones, [4, 1])
    self.assertEqual(self.parsed_game.blue_stones, [3, 6])
    self.assertEqual(self.parsed_game.green_stones, [2, 2])
  
  def test_total_of_stones(self):
    self.assertEqual(self.parsed_game.get_reds(), 5)
    self.assertEqual(self.parsed_game.get_greens(), 4)
    self.assertEqual(self.parsed_game.get_blues(), 9)
    
  def test_game_possibility(self):
    self.assertTrue(self.parsed_game.matches(Game(1, reds = 12, greens = 13, blues = 14)))
    self.assertFalse(self.parsed_game.matches(Game(1, reds = 1, greens = 13, blues = 14)))
    self.assertTrue(self.parsed_game.matches(Game(1, reds = 5, greens = 4, blues = 9)))
  
  def test_resolution(self):
    games = (
      'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
      'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
      'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
      'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
      'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    )
    score = score_matching_games(games, Game(1, reds=12, greens=13, blues=14))
    self.assertEqual(score, 8)

    
    

   