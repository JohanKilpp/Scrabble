letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters,points)}

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  
  for letter in word:
    if letter in letter_to_points:
      point_total +=  letter_to_points.get(letter, 0)
      
  return point_total

brownie_points = score_word("BROWNIE")

print(brownie_points)
  
print(letter_to_points)

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH','EYES', 'MACHINE'], 'lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']  }

player_to_points = {}

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print(player_to_points)
  
def play_word(player,word):
  try:
    upper_word = word.upper()
    player_to_words[player].append(upper_word)
  except KeyError:
    upper_word = word.upper()
    player_to_words[player] = [upper_word]
  print(player_to_words)
  return update_point_totals()
  
 

    

play_word("Johan", "WATER")
play_word("Johan", "braIn")
play_word("Prof Reader", "SNAke")
