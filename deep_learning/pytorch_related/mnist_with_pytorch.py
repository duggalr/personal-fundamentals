import os
import pickle
import gzip
from pathlib import Path
import math
import requests
import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset
from torch import optim
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt




# # MNIST pytorch example

def prepare_mnist_dataset():
  FILENAME = "mnist.pkl.gz"
  pt = Path(os.path.join('/Users/rahul/Documents/main/projects/personal_learning_projects/fundamentals/deep_learning/pytorch_related/data', FILENAME))
  if not pt.exists():
    URL = "https://github.com/pytorch/tutorials/raw/master/_static/"
    content = requests.get(URL + FILENAME).content
    pt.open('wb').write(content)

  with gzip.open((pt).as_posix(), "rb") as f:

    ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")
  
  return x_train, y_train, x_valid, y_valid



class SimpleNN(nn.Module):
  """
  1-Layer NN with 784 activation units and softmax as output; trained via CE-loss function with SdGD
  """
  def __init__(self):
    super().__init__()
    self.lin = nn.Linear(784, 10)

  def forward(self, xb):
    return self.lin(xb)


x_train, y_train, x_valid, y_valid = prepare_mnist_dataset()
print(x_train.shape)
# plt.imshow(x_train[0].reshape((28, 28)), cmap="gray")
# plt.show()

train_ds = TensorDataset(x_train, y_train)
loss_func = F.cross_entropy

epochs = 10
lr = 0.1
batch_size = 64
model = SimpleNN()
opt = optim.SGD(model.parameters(), lr=lr)

train_ds = TensorDataset(x_train, y_train)
train_dl = DataLoader(train_ds, batch_size=batch_size)

for epoch in range(epochs):
  for xb, yb in train_dl:
    pred = model(xb)
    loss = loss_func(pred, yb)
    loss.backward()
    opt.step()
    opt.zero_grad()

print(loss_func(model(xb), yb))




