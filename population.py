import random


class Population():
    def __init__(self, playerList):
        self.num = len(playerList)
        self.playerList = playerList
        self.toppers = []
        self.toppersscore = []

    def perform(self):
        for each in self.playerList:
            each.perform()

    def getMaxFitness(self):
        return getMaxVal([player.returnfitness() for player in self.playerList])

    def getMaxFitPlayer(self):
        return self.playerList[getMaxIndex([player.returnfitness() for player in self.playerList])]

    def isAlive(self):
        return all([player.isAlive() for player in self.playerList])

    def mutate(self, rand_smallDev, rand_largeDev, gen):
        oldplayerlist = self.playerList[:]
        newplayerlist = []
        player1 = oldplayerlist[getMaxIndex([x.returnfitness() for x in oldplayerlist])]
        # newplayerlist.append(player1)
        oldplayerlist.remove(player1)
        player2 = oldplayerlist[getMaxIndex([x.returnfitness() for x in oldplayerlist])]
        # newplayerlist.append(player2)
        oldplayerlist.remove(player2)
        player3 = oldplayerlist[getMaxIndex([x.returnfitness() for x in oldplayerlist])]
        # newplayerlist.append(player3)
        oldplayerlist.remove(player3)

        print("Max fitness in GENERATION NO. " + str(gen) + " is " + str(player1.returnfitness()))

        self.toppers.append(player1)
        self.toppersscore.append(player1.returnfitness())
        self.toppers.append(player2)
        self.toppersscore.append(player2.returnfitness())
        self.toppers.append(player3)
        self.toppersscore.append(player3.returnfitness())

        temp = []
        for i in range(3):
            ind = getMaxIndex(self.toppersscore)
            temp.append(self.toppers[ind])
            self.toppers.remove(self.toppers[ind])
            self.toppersscore.remove(self.toppersscore[ind])

        self.toppers = temp[:]
        newplayerlist.extend(self.toppers)

        rand = random.Random()
        for each,i in zip(oldplayerlist, range(len(oldplayerlist))):
            r = rand.random()
            if r < 0.6:
                newplayerlist.append(player1.mutate(rand_smallDev, rand_largeDev))
                continue
            if r < 0.9:
                newplayerlist.append(player2.mutate(rand_smallDev, rand_largeDev))
                continue
            if r < 1:
                newplayerlist.append(player3.mutate(rand_smallDev, rand_largeDev))
                continue
        return Population(newplayerlist[:])#changed



def getMaxVal(val_list):
    ans = 0
    for val in val_list:
        ans = max(ans, val)
    return ans

def getMaxIndex(val_list):
    return val_list.index(getMaxVal(val_list))

def getMax(val_list):
    return val_list[getMaxIndex(val_list)]
