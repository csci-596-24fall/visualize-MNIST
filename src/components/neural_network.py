import os
import numpy as np

from utils.constant import NN_SIZE
from utils.file import load_mat

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

        self.w1 = load_mat(os.path.join(data_dir, 'weight1.txt'))
        self.w2 = load_mat(os.path.join(data_dir, 'weight2.txt'))
        self.w3 = load_mat(os.path.join(data_dir, 'weight3.txt'))

        self.b1 = load_mat(os.path.join(data_dir, 'biases1.txt'))
        self.b2 = load_mat(os.path.join(data_dir, 'biases2.txt'))
        self.b3 = load_mat(os.path.join(data_dir, 'biases3.txt'))


    def update(self, img):
        # TODO: not sure T or not T
        input_layer = img.flatten().T
        layer1 = ReLU(np.matmul(input_layer, self.w1) + self.b1)
        layer2 = ReLU(np.matmul(layer1, self.w2) + self.b2)
        layer3 = softmax(np.matmul(layer2, self.w3) + self.b3)

        print("=== peak values ===")
        print(np.min(input_layer), np.max(input_layer))
        print(np.min(layer1), np.max(layer1))
        print(np.min(layer2), np.max(layer2))
        print(np.min(layer3), np.max(layer3))

        self._layers = [
            img,
            layer1.flatten().reshape(NN_SIZE.LAYER1),
            layer2.flatten().reshape(NN_SIZE.LAYER2),
            layer3.flatten().reshape(NN_SIZE.LAYER3)
        ]

    def get_activations(self):
        return self._layers