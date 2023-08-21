import random


class Neuron():
    def __init__(self, type):
        self.type = type
        self.wieghts = []
        self.inputs = []
        self.output = 0
        rand = random.Random()
        self.bias = rand.random()

    def activate(self, val):
        if val > 0:
            return val
        else:
            return 0

    def calcoutput(self):
        if self.type == "I":
            self.output = self.inputs
            return
        sum = self.bias
        for i,w in zip(self.wieghts, self.inputs):
            sum += i * w
        sum = self.activate(sum)
        self.output = sum

    def setWieghts(self, wieghts):
        self.wieghts = wieghts

    def setInputs(self, inputs):
        self.inputs = inputs

    def getOutput(self):
        self.calcoutput()
        return self.output