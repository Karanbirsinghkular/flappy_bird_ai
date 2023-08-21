import copy
import random

import Neural_Net
class Player():
    def __init__(self, playable_entity, returnfitness, neuralNet):
        self.entity = playable_entity
        self.returnfitness = returnfitness
        self.neuralNet = neuralNet


    def updateInputs(self, x):
        self.neuralNet.updateInputs(x)

    def getOutputs(self):
        return self.neuralNet.getOutputs()

    def perform(self):
        if self.isAlive():
            self.neuralNet.feedforward()

    def isAlive(self):
        return self.entity.alive

    def returnfitness(self):
        return self.returnfitness()

    def mutate(self, rand_smallDev, rand_largeDev):
        rand = random.Random()
        for each in self.neuralNet.layerlist:
            for neuron in each.neuron_list:
                if neuron.type != "I":
                    for i in range(len(neuron.wieghts)):
                        r = rand.random()
                        if r < rand_largeDev:
                            neuron.wieghts[i] = 1 - 2 * rand.random()
                        elif r < rand_smallDev:
                            neuron.wieghts[i] += (1 - 2 * rand.random()) * 0.1 * neuron.wieghts[i]
                    r = rand.random()
                    if r < rand_largeDev:
                        neuron.bias = 1 - 2 * rand.random()
                    elif r < rand_smallDev:
                        neuron.bias += (1 - 2 * rand.random()) * 0.1 * neuron.bias
        self.entity.alive = True
        return Player(self.entity, self.returnfitness, copy.deepcopy(self.neuralNet))





