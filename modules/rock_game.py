class Game:
  def __init__(self, game_id, reds = 0, greens = 0, blues = 0):
    self.game_id = game_id
    self.reds = reds
    self.blues = blues
    self.greens = greens

class Parser:
  def __init__(self, game) -> None:
    self.game_id = int(game[0:game.index(':')][game.index(' '):])
    self.red_stones = []
    self.blue_stones = []
    self.green_stones = []
    self.unknow_plays = {}
    
    rest_of_game = game[game.index(':')+1:]
    for game in rest_of_game.split(';'):
      for stones in game.split(','):
        striped_text = stones.strip()
        rocks = striped_text[:striped_text.index(' ')]
        color = striped_text[striped_text.index(' ')+1:]
        
        if color == 'red':
          self.red_stones.append(int(rocks))
        elif color == 'blue':
          self.blue_stones.append(int(rocks))
        elif color == 'green':
          self.green_stones.append(int(rocks))
        else:
          # hope to not get here
          print('Oh No!')
          self.unknow_plays[color] = int(stones)
  
  def to_game(self):
    return Game(self.game_id, reds = self.get_reds, blues = self.get_blues, greens = self.get_greens)
  
  def matches(self, game: Game) -> bool:
    return (
      len(list(filter(lambda x: x > game.reds, self.red_stones))) == 0 and
      len(list(filter(lambda x: x > game.greens, self.green_stones))) == 0 and
      len(list(filter(lambda x: x > game.blues, self.blue_stones))) == 0 
    )
  
  def get_game_power(self):
    return (
      max(self.red_stones) *
      max(self.blue_stones) *
      max(self.green_stones)
    )

def score_matching_games(game_list, game_reference):
  score = 0
  for game in game_list:
    parsed = Parser(game)
    if parsed.matches(game_reference):
      print('game %s matched' % parsed.game_id)
      score += parsed.game_id
  return score

def batch_parse_games(game_list):
  parsed_list = []
  [parsed_list.append(Parser(x)) for x in game_list]
  return parsed_list

def get_total_power_of_minimun_rocks(game_list):
  return sum([game.get_game_power() for game in batch_parse_games(game_list)])