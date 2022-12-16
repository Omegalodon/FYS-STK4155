

## Here we make tuples with activation function and its derivative, in thar 

def tanh(x):
    return (np.tanh(x),1 - np.tanh(x)**2)

def d_tanh(x):
    return 1 - np.tanh(x)**2
 


def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    
def d_sigmoid(x):
    return self.sigmoid(x) * (1 - self.sigmoid(x)) 

def relu(x):
    return np.maximum(0, x)

def d_relu(x):
    x[x <= 0] = 0
    x[x > 0] = 1
    return x

def leaky_relu(x, alpha=0.01):
    return np.maximum(alpha * x, x)

def d_leaky_relu(x):
    x[x < 0] = 0.01
    x[x > 0] = 1
    return x

def linear(x):
    return x

def d_linear(x):
    return np.ones(x.shape)


tanh_ = (tanh, d_tanh)
sigmoid_ = (sigmoid, d_sigmoid)
relu_ = (relu, d_relu)
leaky_relu_ = (leaky_relu, d_leaky_relu)
linear_ = (linear,d_linear)

