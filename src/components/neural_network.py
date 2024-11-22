import os
import numpy as np

from utils.constant import NN_SIZE

def ReLU(x):
    return x * (x > 0)

def softmax(x, axis = None):
    x = x - x.max(axis = axis, keepdims = True)
    y = np.exp(x)
    return y / y.sum(axis = axis, keepdims = True)


class NeuralNetwork:
    def __init__(self) -> None:
        self._layers = None
        current_dir = os.path.dirname(__file__)
        data_dir =  os.path.join(current_dir, "../data/")

        self.w = []
        self.b = []

        for i in range(NN_SIZE.NUMBER_OF_LAYER):
            w = np.load(os.path.join(data_dir, f'layer_{i + 2}_weights.npy'))
            b = np.load(os.path.join(data_dir, f'layer_{i + 2}_biases.npy'))
            self.w.append(w)
            self.b.append(b)
    

    def _calc_layer(self, cur, weight, bias, activation):
        res = np.matmul(cur, weight) + bias
        return activation(res)


    def update(self, img):
        input_layer = img.flatten()
        layer1 = self._calc_layer(input_layer, self.w[0], self.b[0], ReLU)
        layer2 = self._calc_layer(layer1, self.w[1], self.b[1], ReLU)
        layer3 = self._calc_layer(layer2, self.w[2], self.b[2], softmax)

        self._layers = [
            img,
            layer1.flatten().reshape(NN_SIZE.LAYER1),
            layer2.flatten().reshape(NN_SIZE.LAYER2),
            layer3.flatten().reshape(NN_SIZE.LAYER3)
        ]

    def get_layers(self):
        return self._layers
