import numpy as np

# loss function and its derivative
def mse(y_true, y_pred):
    return np.mean((y_true-y_pred)**2)

def d_mse(y_true, y_pred):
    return 2*(y_pred-y_true)/y_true.size

def cross_entropy(y_true, y_pred):
    loss = - np.sum(y_true*np.log(y_pred)+(1-y_true)*np.log(1-y_pred))
    return loss / float(y_pred.shape[0])

def d_cross_entropy(y_true, y_pred):
    term = y_pred*(1-y_pred)
    loss = (y_pred - y_true) / (term)
    return loss



