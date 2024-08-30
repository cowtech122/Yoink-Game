import random
# print(random.randint(1,5))

# Setting the class of the prey
class Critter:
  def __init__(self, name, difficulty):
    self.name = name
    self.difficulty = difficulty * 10 - 9
    self.score = difficulty ** 2

# Methods for catching a critter
  def can_yoink(self):
    global total_score
    global collection
    yoink_score = random.randint(1,100)
    if yoink_score >= self.difficulty - pred.ability:
      print('You successfully yoinked the {critter}!'.format(critter=self.name))
      total_score += self.score
      collection.append(self.name)
    else:
      pred.fingers -= 1
      print(pred.bad_try())
      
  def use_bait(self):
    global total_score
    global collection
    yoink_score = random.randint(1,100)
    print('Bait was used to increase catch by 20%')
    if yoink_score >= self.difficulty - pred.ability - 20:
      print('You successfully yoinked the {critter}!'.format(critter=self.name))
      total_score += self.score
      collection.append(self.name)
    else:
      pred.fingers -= 1
      print(pred.bad_try())


# Setting a class of predator
class Catcher:
    def __init__(self, name, ability, fingers, bait = 1):
        self.name = name
        self.ability = ability
        self.fingers = fingers
        self.bait = bait

    def __repr__(self):
        return 'You have chosen {catcher} who has catch +{ability}, {chances} misses, and {bait} bait.'.format(catcher=self.name, ability=self.ability, chances=self.fingers, bait=self.bait)

    def bad_try(self):
        if self.name == 'guy':
            if self.fingers != 1:
               return 'You missed the yoink, the {critter} got one of your fingers. You have {numb} fingers left.'.format(critter=target.name, numb=self.fingers)
            else:
                return 'You missed the yoink, the {critter} got one of your fingers. You have {numb} finger left.'.format(critter=target.name, numb=self.fingers)
        if pred.name == 'cheetah':
            if self.fingers != 1:
                return 'You missed the yoink, the {critter} got away. You have {numb} attempts left.'.format(critter=target.name, numb=self.fingers)
            else:
                return 'You missed the yoink, the {critter} got away. You have {numb} attempt left.'.format(critter=target.name, numb=self.fingers)

      

total_score = 0
collection = []
possibilities = ['worm', 'gecko', 'hedgehog', 'snake', 'monkey', 'alligator', 'T-rex']
encounters = {'worm': 0, 'gecko': 4, 'hedgehog': 5, 'snake': 7, 'monkey': 8, 'alligator': 9, 'T-rex': 10}

# choosing the predator
while True:
    selection = input('Do you want to be a guy or cheetah?')
    if selection != 'guy' and selection != 'cheetah':
        print('Please choose either guy or cheetah.')
    else:
        break

if selection == 'guy':
    pred = Catcher('guy', 0, 5)
if selection == 'cheetah':
    pred = Catcher('cheetah', 5, 4)
print(repr(pred))

# Game loop
while pred.fingers > 0:
  animal = possibilities[random.randint(0,6)]
  print('You have found a {critter}!'.format(critter = animal))
  target = Critter(animal, encounters[animal])
  if pred.bait > 0:
      choice = input('Do you want to yoink? [y/n/bait]')
      if choice == 'n':
          continue
      elif choice == 'y':
          target.can_yoink()
      elif choice == 'bait':
          target.use_bait()
          pred.bait -= 1
          if pred.bait == 0:
              print('You are out of bait.')
  else:
      choice = input('Do you want to yoink? [y/n]')
      if choice == 'n':
          continue
      elif choice == 'y':
          target.can_yoink()

# Endgame message:
if pred.name == 'guy':
    print('You ran out of yoinking fingers. You have caught {number} animals: {list} for {score} points!'.format(list=collection, score=total_score, number=len(collection)))
if pred.name == 'cheetah':
    print('You got tired from the yoinking and fell asleep. You have caught {number} animals: {list} for {score} points!'.format(list=collection, score=total_score, number=len(collection)))