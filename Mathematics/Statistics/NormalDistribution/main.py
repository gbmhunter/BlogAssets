import math
import matplotlib.pyplot as plt
import numpy as np

def normal_distribution_pdf(x, mean, sd):
    scalar_fraction = 1 / (math.sqrt(2*math.pi*sd))
    exp_fraction = -1*(((x - mean)**2)/(2*sd**2))
    pd = scalar_fraction*math.exp(exp_fraction)
    return pd

if __name__ == '__main__':

    MEAN = 0.0
    SD = 1.0

    x_a = np.arange(-10.0, 10.0, 0.01)
    pdf_a = [ normal_distribution_pdf(x, MEAN, SD) for x in x_a ]
    pdf_a = np.array(pdf_a)

    fig, ax = plt.subplots()

    points = ax.scatter(x_a, pdf_a, label='Data points')

    plt.title('Normal Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('y')
    ax.legend()
    plt.savefig('graph.png')