import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    res = {}
    probabilities = {}
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        if total in res:
            res[total] += 1
        else:
            res[total] = 1

    for k, v in res.items():
        probabilities[k] = v / num_rolls
    return probabilities  


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Sum')
    plt.ylabel('probabilities')
    plt.title('Mante Karlo')

    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')

    plt.show()



if __name__ == "__main__":

    for i in [100, 1000, 10000, 100000]:
        probs = simulate_dice_rolls(i)
        plot_probabilities(probs)
