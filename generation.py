import copy

import population
class Generation():
    def __init__(self, pop):
        self.popnum = len(pop.playerList)
        self.currentpop = pop
        self.prevpop = pop
        self.maxFitness = 0
        self.mutatecall = 1

    def getMaxFitIndividual(self):
        return self.currentpop.getMaxFitPlayer()

    def MaxFitness(self):
        self.maxFitness = self.currentpop.getMaxFitness()

    def createNewGen(self, rs, rl):
        self.prevpop = copy.deepcopy(self.currentpop.getMaxFitPlayer().neuralNet)
        self.currentpop = self.currentpop.mutate(rs, rl, self.mutatecall)
        self.mutatecall += 1
