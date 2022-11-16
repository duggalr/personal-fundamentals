import random
import numpy as np
import matplotlib.pyplot as plt


# generate Gaussian distribution
def generate_normal_dist(mu=0, sigma=1, size=10000, num_bins=10):
  mu = 0 
  sigma = 1
  x = np.random.normal(mu, sigma, size=size)
  mean_x = np.mean(x)
  std_x = np.std(x)
  print("Computed Mean: {} / Computed Std: {}".format(mean_x, std_x))
  count, bins, ignored = plt.hist(x, num_bins, density=True)
  normal_prob_dist = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2))
  plt.plot(bins, normal_prob_dist, linewidth=2, color='r')
  plt.show()


# generate_normal_dist(size=100)


# coin-flip and properties of CLT
def coin_flip(n=100, num_bins=10):
  coin_choices = ['H', 'T']
  selected_values = []
  for _ in range(n):
    val = random.choice(coin_choices)
    selected_values.append(val)
  
  print("Number of Heads:", len([val for val in selected_values if val == 'H']))
  print("Number of Tails:", len([val for val in selected_values if val == 'T']))
  count, bins, ignored = plt.hist(selected_values, bins=num_bins)
  mu = n * 0.5
  sigma = mu * (0.5)
  normal_prob_dist = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2))
  plt.plot(bins, normal_prob_dist,  linewidth=2, color='r')
  plt.show()

# coin_flip(n=100000, num_bins=30)



