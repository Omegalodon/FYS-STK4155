from layer import Layer
import numpy as np
#from numpy.random import MT19937
#from numpy.random import RandomState, SeedSequence
rng = np.random
#rng = RandomState(MT19937(SeedSequence(123456789)))
#rng.seed(101011)
# inherit from base class Layer
class FCLayer(Layer):
    # input_size = number of input neurons
    # output_size = number of output neurons
    def __init__(self, input_size, output_size, random_state):
        #rs = RandomState(MT19937(SeedSequence(123456789)))
        #rng.seed(101011)
        self.random_state = random_state
        self.rng = np.random
        rng.seed(random_state)
        self.weights = rng.rand(input_size, output_size) - 0.5
        self.bias = np.zeros((1, output_size))



    # returns output for a given input
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = np.dot(self.input, self.weights) + self.bias 
        return self.output

    
    def backward_propagation(self, output_error, learning_rate ,lmbda):
        input_error = np.dot(output_error, self.weights.T)
        weights_error = np.dot(self.input.T, output_error)
        # dBias = output_error

        # update parameters
        self.weights -= learning_rate * weights_error + lmbda * self.weights
        self.bias -= learning_rate * output_error + lmbda * self.bias
        return input_error