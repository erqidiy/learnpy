# remove all the 'cat' item in a peg list
pets = ['dog', 'cat', 'rabbit', 'dog', 'cat', 'goldfish', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
