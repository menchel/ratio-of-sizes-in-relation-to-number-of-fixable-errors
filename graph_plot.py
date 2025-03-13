from itertools import product
from math import comb
import matplotlib.pyplot as plt


def check_if_word_is_locally_bounded(n,word, l, delta):
    'iterate over all the windows'
    for i in range(n - l + 1):
        window = word[i:i+l]
        'check the current window'
        if sum(window) > l // 2 - delta:
            return False
    return True

def count_amount_of_n_l_delta_locally_bounded_codes(n, l, delta):
    vectors_counter = 0
    'iterate over all possible n sized vectors'
    for word in product([0, 1], repeat=n):
        if check_if_word_is_locally_bounded(n,word, l, delta):
            vectors_counter += 1
    return vectors_counter


#calculate the lower part of the upper bound for |C|
def compute_binomial_sum(n, t):
    return sum(comb(n, i) for i in range(t + 1))


def plot_all(n, delta, max_value_of_t, l_values):
    t_values = list(range(max_value_of_t + 1))

    'iterating over the values of l, to plot all of them on the grid'
    for l in l_values:
        S = count_amount_of_n_l_delta_locally_bounded_codes(n, l, delta)
        all_ratios = []
        for t in t_values:
            low = compute_binomial_sum(n, t)
            rate = (2 ** n) / low
            ratio = S / rate
            all_ratios.append(ratio)

        'plotting the specific l value'
        plt.plot(t_values, all_ratios, marker='o', label=f'l={l}')

    'color a line for 1, the wanted ration lower bound'
    plt.axhline(y=1, color='r', linestyle='--', label='Ratio = 1')

    'plotting details'
    plt.xlabel("t")
    plt.ylabel("Ratio of |S| size over approximation of |C|")
    plt.title(f"Ratio Analysis for n={n}, delta={delta}")
    plt.grid()
    plt.legend()
    plt.savefig("plot_multiple_l_values.png")


if __name__ == '__main__':

    'recieve input'
    print("Enter vector size n")
    n = int(input())
    print("Enter delta")
    delta = int(input())
    print("Enter maximum t value")
    max_value_of_t = int(input())
    
    print("Enter window sizes (comma separated):")
    l_values = list(map(int, input().split(',')))

    plot_all(n, delta, max_value_of_t, l_values)
