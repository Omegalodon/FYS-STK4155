import numpy as np

# activation function and its derivative
def tanh(x):
    return np.tanh(x)

def d_tanh(x):
    return 1.0 - np.multiply(np.tanh(x), np.tanh(x))



## Here we make tuples with activation function and its derivative, in thar 



def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    
def d_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x)) 

def relu(x):
    return np.maximum(0, x)

def d_relu(x):
    x[x <= 0] = 0
    x[x > 0] = 1
    return x

def leaky_relu(x, alpha=0.01):
    return np.multiply((x >= 0), x) + np.multiply((x < 0), x * alpha)

def d_leaky_relu(x, alpha = 0.01):
    return (x >= 0) * 1 + (x < 0) * alpha
"""
def leaky_relu(x, alpha=0.01):
    return np.maximum(alpha * x, x)

def d_leaky_relu(x):
    x[x < 0] = 0.01
    x[x > 0] = 1
    return x
"""

def linear(x):
    return x

def d_linear(x):
    return np.ones(x.shape)

def elu(x, alpha = 2.0):
    x[x >= 0] = x 
    x[x < 0] = alpha * (np.exp(x) - 1) 
    return x

def d_elu(x, alpha = 2.0):
    x[x > 0] = 1 
    x[x < 0] = alpha * (np.exp(x)) 
    return x