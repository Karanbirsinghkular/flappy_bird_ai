import random

import NN_NEURON

class Layer():
    def __init__(self, type, num, prevlayer):
        self.type = type
        self.num = num
        self.inputs = []
        self.neuron_list = [NN_NEURON.Neuron(type) for i in range(num)]
        self.wieghts = []
        if self.type != "I":
            self.initWieghts(len(prevlayer.neuron_list))
        self.outputs = []

    def calcoutput(self):
        self.outputs = [neuron.getOutput() for neuron in self.neuron_list]

    def initWieghts(self, num):
        rand = random.Random()
        x = []

        for neuron in self.neuron_list:
            for i in range(num):
                x.append(1 - 2 * rand.random())
            neuron.wieghts = x[:]
            x.clear()

    def setInputs(self, inputs):
        if self.type == "I":
            raise Exception("Neuron of type input cannot be assigned inputs")
        for neuron in self.neuron_list:
            neuron.inputs = inputs

    def getOutputs(self):
        self.calcoutput()
        return self.outputs