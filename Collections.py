from collections import defaultdict
colours = (
    ('Karl', 'Yellow'),
    ('Lucy', 'Blue'),
    ('David', 'Green'),
    ('Rick', 'Black'),
    ('Jonathen', 'Red'),
    ('kahn', 'Silver'),
    ('Adam smash', 'black'),
)

favorite_colour = defaultdict(list)

for name, color in colours:
    favorite_colour[name].append(color)
    
print(favorite_colour)
######################################
tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['samantha'] = 'blue'
# Works fine
import json
print(json.dumps(some_dict))
#######################################
from collections import Counter
favs = Counter(value for name, value in colours)
print(favs.most_common())