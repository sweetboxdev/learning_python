import copy
class Character:

    def __init__(self, identity, enemy, humanSide):
        self.identity=identity
        self.enemy=enemy
        self.humanSide=humanSide

    def getIdentity(self):
        return self.identity

    def getEnemy(self):
        return self.enemy

class Stage:

    def __init__(self,side):
        self.side = side
        self.actors = []

    def addActor(self,actor):
        self.actors.append(actor)

    def removeActor(self,actor):
        try: self.actors.remove(actor)
        except: print(f'Actor not found on {self.side}')

    def actorList(self):
        return self.actors


def getSide(actor):
    for i in lActors:
        if actor in lActors:
            print(f'{actor.identity} is on the left.')
            return 'left'
    for i in rActors:
        if actor in rActors:
            print(f'{actor.identity} is on the right.')
            return 'right'




fox = Character('fox',None,None)
goose = Character('goose','fox',None)
corn = Character('corn','goose',None)
human = Character('human',None,'left')
leftSide = Stage('left')
rightSide = Stage('right')
lActors = leftSide.actors
rActors = rightSide.actors
leftSide.addActor(fox)
leftSide.addActor(goose)
leftSide.addActor(corn)
changableStage = copy.deepcopy(Stage)

def leftIdentities():
    r = []
    for i in lActors:
        r.append(i.identity)
    print(r)

def rightIdentities():
    r = []
    for i in rActors:
        r.append(i.identity)
    print(r)

def deathCheck():
    lEnemies = []
    rEnemies = []
    namesLeft = []
    namesRight = []
    for i in lActors:
        lEnemies.append(i.enemy)
        namesLeft.append(i.identity)
    for i in rActors:
        rEnemies.append(i.enemy)
        namesRight.append(i.identity)
    for i in lActors:
        print(f'Is {i.enemy} in {namesLeft}?')
        if i.enemy in namesLeft:
            print(f'{i.identity}:Yes, {i.enemy} is on the Left side')
            print('---Ending Move---')
            return False
        else:
            print(f'{i.identity}: No, {i.enemy} is not on the Left side')
        for i in rActors:
            print(f'is {i.enemy} in {namesRight}?')
            if i.enemy in namesRight:
                print(f'{i.identity}: Yes, {i.enemy} is on the Right side')
                print('---Ending Move---')
                return False
        else:
            print(f'No, {i.enemy} is not on the Right side')

def moveActor():
    count = 1
    if human.humanSide == 'left':
        clActors = copy.deepcopy(leftSide.actors)
        for i in clActors:
            print(f'Start move {count}. Attempting {i.identity}')
            print(leftIdentities())
            leftSide.removeActor(i)
            rightSide.addActor(i)
            print('---Left side list after move ---')
            print(leftIdentities())
            print('---Right side list after move---')
            print(rightIdentities())
            if deathCheck() == False:
                rightSide.removeActor(i)
                leftSide.addActor(i)
                print('Side after removal')
                print(leftIdentities())
                print(rightIdentities())
                print('Failed attempt, restarting.')
                count = count + 1
                continue
            else:
                print('Move Successful. Moving on...')
                human.humanSide = 'right'
                break



moveActor()






print('----- Left side -------')
for i in leftSide.actors:
    print(Character.getIdentity(i))
print('------ Right Side -------')
for i in rightSide.actors:
    print(Character.getIdentity(i))

