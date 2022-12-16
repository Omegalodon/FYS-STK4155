class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.d_loss = None

    # add layer to network
    def add_layer(self, layer):
        self.layers.append(layer)

    # cost function
    def cost_function(self, loss, d_loss):
        self.loss = loss
        self.d_loss = d_loss

    # predict output for given input
    def predict(self, input_data):
        # sample dimension first
        samples = len(input_data)
        result = []

        # run network over all samples
        for i in range(samples):
            # forward propagation
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)

        return result

    # train the network
    def fit(self, x_train, y_train, epochs, learning_rate, lmbda):
        # sample dimension first
        samples = len(x_train)

        # training loop
        for i in range(epochs):
            err = 0
            for j in range(samples):
                # forward propagation
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                # compute loss (for display purpose only)
                err += self.loss(y_train[j], output)

                # backward propagation
                error = self.d_loss(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate,lmbda)

            # calculate average error on all samples
            err /= samples
            print(f'epoch {i+1}/{epochs}   error= {err:.4f}')
