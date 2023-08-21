import NN_LAYER

class NN():
    def __init__(self, inputnum, outputnum, layernum, layerneuronnum):
        self.inputnum = inputnum + 1 # +1 for the bias neuron
        self.outputnum = outputnum
        self.layernum = layernum
        self.layerneuronnum = layerneuronnum
        self.inputLayer = NN_LAYER.Layer("I", inputnum, None)
        self.hiddenlayerlist = []
        if layernum > 0:
            self.hiddenlayerlist.append(NN_LAYER.Layer("H", layerneuronnum, self.inputLayer))
            for i in range(layernum - 1):
                self.hiddenlayerlist.append(NN_LAYER.Layer("H", layerneuronnum, self.hiddenlayerlist[i]))
        if len(self.hiddenlayerlist) > 0:
            self.outputlayer = NN_LAYER.Layer("O", outputnum, self.hiddenlayerlist[-1])
        else:
            self.outputlayer = NN_LAYER.Layer("O", outputnum, self.inputLayer)
        self.layerlist = []
        self.layerlist.append(self.inputLayer)
        self.layerlist.extend(self.hiddenlayerlist)
        self.layerlist.append(self.outputlayer)

    def feedforward(self):
        for i in range(len(self.layerlist)):
            if i == 0:
                continue
            if i != 0:
                self.layerlist[i].setInputs(self.layerlist[i - 1].getOutputs())
            if i == len(self.layerlist) - 1:
                self.layerlist[-1].calcoutput()

    def updateInputs(self, inputs):
        for neuron, input in zip(self.inputLayer.neuron_list, inputs):
            neuron.inputs = input

    def getOutputs(self):
        return self.outputlayer.getOutputs()
