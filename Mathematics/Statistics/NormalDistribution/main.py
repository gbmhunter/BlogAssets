import math
import matplotlib.pyplot as plt
import numpy as np

def normal_distribution_pdf(x, mean, sd):
    scalar_fraction = 1 / (math.sqrt(2*math.pi*sd))
    exp_fraction = -1*(((x - mean)**2)/(2*sd**2))
    pd = scalar_fraction*math.exp(exp_fraction)
    return pd

def add_nd_to_plot(mean, sd, ax):
    x_a = np.arange(-10.0, 10.0, 0.01)
    pdf_a = [ normal_distribution_pdf(x, mean, sd) for x in x_a ]
    pdf_a = np.array(pdf_a)
    points = ax.plot(x_a, pdf_a, label=f'mean={mean}, sd={sd}')

if __name__ == '__main__':

    MEANS = [0.0, 0.0, 3.0]
    SDS = [1.0, 2.0, 0.5]

    fig, ax = plt.subplots()
    for idx in range(len(MEANS)):
        add_nd_to_plot(MEANS[idx], SDS[idx], ax)

    plt.title('Normal Distribution \nProbability Density Functions (PDFs)')
    plt.xlabel('Random Variable')
    plt.ylabel('PDF')
    ax.legend()
    plt.savefig('graph.png')