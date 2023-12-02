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
          self.unknow_plays[color] = int(stones)
          
  def get_reds(self):
    return sum(self.red_stones)
  
  def get_greens(self):
    return sum(self.green_stones)
  
  def get_blues(self):
    return sum(self.blue_stones)
  
  def to_game(self):
    return Game(self.game_id, reds = self.get_reds, blues = self.get_blues, greens = self.get_greens)
  
  def matches(self, game: Game) -> bool:
    return (
      self.get_reds() <= game.reds and 
      self.get_blues() <= game.blues and 
      self.get_greens() <= game.greens
    )
  

def score_matching_games(game_list, game_reference):
  score = 0
  for game in game_list:
    parsed = Parser(game)
    if parsed.matches(game_reference):
      print('game %s matched' % parsed.game_id)
      score += parsed.game_id
  return score

