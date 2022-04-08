import copy

class Actor:
    def __init__(self, identity, enemy):
        self.identity = identity
        self.enemy = enemy
    
    def getIdentity(self):
        return self.identity

    def getEnemy(self):
        return self.enemy

class Stage:
    def __init__(self, identity, actors=[]):
        self.identity = identity
        self.actors = actors

    def addActor(self, Actor):
        self.actors.append(Actor)
    
    def removeActorByIdentity(self, identity):
        for i in range(len(self.actors)):
            if self.actors[i].getIdentity() == identity:
                return self.actors.pop(i)
        else:
            raise KeyError(f"{identity} not found!")

    def getActors(self):
        return self.actors

    def getIdentity(self):
        return self.identity

    def inConflict(self):
        # Do some check to see if someone will eat someone else and return True / False
        identies = {}
        # is the human here?
        # return False


        for x in self.actors:
            identies[x.getIdentity] = True

        for x in self.actors:
            if x.getEnemy() in identies:
                return True
        return False

cat = Actor("cat", "dog")
dog = Actor("dog", "cat")

left = Stage("left")
right = Stage("right")

left.addActor(cat)
left.addActor(dog)

def moveActor(l, r, a):
    newLeft = Stage(l.getIdentity(), copy.deepcopy(l.getActors())
    newRight = Stage(r.getIdentity(), copy.deepcopy(r.getActors())
    add
    remove
    check conflict
    if conflict return
    else
        iterateThrough


for actor in left.getActors():
    moveActor(left, right, actor)











    a = newLeft.removeActorByIdentity(actor)
    newRight.addActor(a)
    if newLeft.inConflict() or newRight.inConflict():
        continue
    else:
        # repeat as necessicary
