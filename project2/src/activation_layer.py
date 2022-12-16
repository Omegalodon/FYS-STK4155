from layer import Layer

# inherit from base class Layer
class ActivationLayer(Layer):
    def __init__(self, activation, d_activation):
        self.activation = activation
        self.d_activation = d_activation

    # returns the activated input
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return self.output

    # Returns input_error=dE/dX for a given output_error=dE/dY.
    # learning_rate is not used because there is no "learnable" parameters.
    def backward_propagation(self, output_error, learning_rate,lmbda):
        return self.d_activation(self.input) * output_error
