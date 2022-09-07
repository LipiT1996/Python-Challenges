"""
Excercise 7: an improvised lottery
"""

import random
lottery_number = set(random.sample(range(22), 6))

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
top_player = players[0]

for i in players:
  matched_number = len(i["numbers"].intersection(lottery_number))
  if matched_number > len(top_player["numbers"].intersection(lottery_number)):
    top_player = i
winning = 100 **len(top_player["numbers"].intersection(lottery_number))

print(f"{top_player['name']} has won {winning}")