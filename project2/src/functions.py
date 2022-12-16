import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from nn import NeuralNetwork


# r squared
def R2(z_data, z_model):
    return 1 - np.sum((z_data - z_model)**2.0) / np.sum(
        (z_data - np.mean(z_data))**2.0)


# Mean Square Error
def mse(z_true, z_pred):
    return np.mean(np.power(z_true-z_pred, 2))

def d_mse(z_true, z_pred):
    return 2*(z_pred - z_true) / z_true.size



def FrankeFunction(x, y):
    # evaluation of each term
    term1 = 0.75 * np.exp(-(0.25 + (9 * x - 2)**2) - 0.25 * ((9 * y - 2)**2))
    term2 = 0.75 * np.exp(-((9 * x + 1)**2) / 49.0 - 0.1 * (9 * y + 1))
    term3 = 0.5 * np.exp(-(9 * x - 7)**2 / 4.0 - 0.25 * ((9 * y - 3)**2))
    term4 = -0.2 * np.exp(-(9 * x - 4)**2 - (9 * y - 7)**2)
    return term1 + term2 + term3 + term4

# Change to week 35 code
# Function used to define the design matrix
"""
def design(degree: int, X: np.matrix, Y: np.matrix):
    design = np.ones((len(X), int((degree + 1) * (degree + 2) / 2)))
    for i in range(1, degree + 1): 
        q = int(i * (i + 1) / 2) 
        for k in range(i + 1):
            design[:, q + k] = (X[:, 0] ** (i - k)) * (Y[:, 0] ** k)
    
    return design"""

#
def create_X(x, y, n ):
    # n --> degree 

	if len(x.shape) > 1:
		x = np.ravel(x)
		y = np.ravel(y)

	N = len(x)
	l = int((n+1)*(n+2)/2)		# Number of elements in beta
	X = np.ones((N,l))

	for i in range(1,n+1):
		q = int((i)*(i+1)/2)
		for k in range(i+1):
			X[:,q+k] = (x**(i-k))*(y**k)

	return X


def plot_fig(x_axis, y_axis_train, y_axis_test, xlabel, ylabel, title, save=False):
    plt.figure()
    plt.plot(x_axis, y_axis_train, label='train', color='red')
    plt.plot(x_axis, y_axis_test, label='test', color='blue')
    plt.grid()
    plt.legend()
    plt.xlabel(xlabel, fontsize=13)
    plt.ylabel(ylabel, fontsize=13)
    plt.title(title, fontsize=15)
    if save:
        plt.savefig(title + '.png')
    plt.show()


def accuracy(y_data, y_pred):
    return np.sum(y_data == y_pred) / len(y_predS)

"""
____________________________________________

 Activation functions and their derivatives.
_____________________________________________

"""


