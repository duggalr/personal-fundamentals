import math
import random
import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt


# Implementation of SOM and using it for finding clusters (2D arrays only)


def graph_data(X, y, weight_map):
  fig, ax = plt.subplots()
  scatter = ax.scatter(X[:, 0], X[:, 1], c=y)  
  # plt.scatter(np.array(examples)[:, 0], np.array(examples)[:, 0], c=labels, cmap="RdBu")
  ax.legend(*scatter.legend_elements())
  ax.scatter(weight_map[:, 0], weight_map[:, 1])
  # ax.set_xlabel('Input : X1')
  # ax.set_ylabel('Input : X2')
  plt.show()


def update_weight_map(input_vector, weight_map, radius_sq, learning_rate):
  # bmu_idx = np.argmin( np.sqrt(((input_vector - weight_map)).sum(axis=1)) )  # euclidean distance; getting 'BMU' (min(ED))

  assert (input_vector.shape[0] == weight_map.shape[1]), "Input Vector and Weight Map shapes not compatible"
  input_vector = input_vector.reshape(1, input_vector.shape[0])
  ed = np.sqrt(((input_vector - weight_map)**2).sum(axis=1))
  # bmu_idx = np.unravel_index( np.argmin(ed, axis=None), ed.shape )  
  bmu_idx = np.argmin(ed, axis=None)
  g, h = bmu_idx, 1
  for i in range(weight_map.shape[0]):
    dist_sq = np.square(i - g)
    dist_fn = math.exp( (-dist_sq) / (2*radius_sq) ) 
    val_to_update = learning_rate * dist_fn * (input_vector - weight_map[i])
    weight_map[i] += val_to_update[0]
  



X, y = make_blobs(n_samples=10, centers=3, n_features=2, random_state=0)
N = 10
num_features = 2
weight_map = np.random.rand(N, num_features)
num_epoches = 100
learning_rate = 0.1
lr_decay = 0.05
radius_sq = 1
radius_decay = 0.05

# graph_data(X, y, weight_map)

for epoch in range(num_epoches):
  print(f"On Epoch: {epoch}")
  np.random.shuffle(X)
  for i_vec in X:
    update_weight_map(
      input_vector=i_vec, weight_map=weight_map, radius_sq=radius_sq, learning_rate=learning_rate
    )
  # utilizing learning-rate/radius decay after each epoch
  learning_rate = learning_rate * math.exp(-epoch * lr_decay)
  radius_sq = radius_sq * math.exp(-epoch * radius_decay)
  
# fig, ax = plt.subplots()
# scatter = ax.scatter(weight_map[:, 0], weight_map[:, 1])  
# plt.show()
# graph_data(X, y, weight_map)


# graph_data(X, y, we
# ight_map)
# print(X)
# print(weight_map)
# print(X[0], weight_map[0])
# input_vector = random.choice(X)
# euclid_distance(input_vector, weight_map, radius_sq=1, learning_rate=0.1)
  




