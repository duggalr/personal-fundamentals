import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import softmax


class SimpleNeuralNet(object):
  """
  Basic 1-layer NN 
  """
  def __init__(self, input_dim, num_activation_units, output_dim, learning_rate=0.01) -> None:
    self.input_dim = input_dim
    self.num_activation_units = num_activation_units
    self.output_dim = output_dim
    self.hidden_layer_weights = np.random.normal(size=(self.input_dim, self.num_activation_units))
    self.output_layer_weights = np.random.normal(size=(self.num_activation_units, self.output_dim))
    self.learning_rate = learning_rate
    self.activation_layer_values = []

  def softmax_function(self, x):
    return softmax(x, axis=0)

  def _fw_pass(self, input_vector):
    hidden_layer_z_val = np.transpose(self.hidden_layer_weights).dot(input_vector)
    relu_fc = lambda t: np.maximum(t, 0)  # relu
    hidden_layer_activation_units = relu_fc(hidden_layer_z_val)
    final_layer_z_val = np.transpose(self.output_layer_weights).dot(hidden_layer_activation_units)
    softmax_values = self.softmax_function(final_layer_z_val)
    self.activation_layer_values.append(hidden_layer_activation_units)
    self.activation_layer_values.append(softmax_values)
    return softmax_values

  def _cost_function(self, pred_values, actual_values):  # cross-entropy loss
    epsilon = 1e-5
    return (-1) * (np.sum(actual_values * np.log(pred_values + epsilon)))

  def _bw_pass(self, input_values, pred_values, actual_values):
    delta_output_layer = pred_values - actual_values
    output_layer_weight_gradient = self.activation_layer_values[0].dot(np.transpose(delta_output_layer))    
    delta_hidden_layer = self.activation_layer_values[0] * (self.output_layer_weights.dot(delta_output_layer))
    hidden_layer_weight_gradient = input_values.dot(np.transpose(delta_hidden_layer))
    # print('weight-change:', (self.learning_rate * output_layer_weight_gradient)) 
    self.output_layer_weights = self.output_layer_weights - ((self.learning_rate * output_layer_weight_gradient))
    self.hidden_layer_weights = self.hidden_layer_weights - ((self.learning_rate * hidden_layer_weight_gradient))

  def train(self, examples, labels, validation_examples=None, validation_labels=None, num_epoches=10, graph_display=True):
    """
    assuming one-hot encoding of the label
    """
    assert len(examples) == len(labels)
    if validation_examples is not None:
      assert len(validation_examples) == len(validation_labels)

    train_cost_list, validation_cost_list = [], []
    for i in range(num_epoches):
      print('On Epoch:', (i+1))
      
      epoch_cost = 0
      for y in range(len(examples)):
        input_vector = np.array(examples[y])
        input_label = np.array(labels[y])
        input_vector = input_vector.reshape(2, 1)
        input_label = input_label.reshape(2, 1)
        pred_label = self._fw_pass(input_vector)
        cost = self._cost_function(pred_label, input_label)
        epoch_cost += cost
        self._bw_pass(input_vector, pred_label, input_label)

      avg_train_cost = epoch_cost/len(examples)
      print('Average Training Cost for Epoch:', avg_train_cost)
      train_cost_list.append(avg_train_cost)

      if validation_examples is not None:
        validation_cost = 0
        for y in range(len(validation_examples)):
          input_vector = np.array(validation_examples[y]).reshape(2, 1)
          input_label = np.array(validation_labels[y]).reshape(2, 1)
          pred_label = self._fw_pass(input_vector)
          cost = self._cost_function(pred_label, input_label)
          validation_cost += cost
        
        avg_validation_cost = validation_cost/len(validation_examples)
        print('Average Validation Cost for Epoch:', avg_validation_cost)
        validation_cost_list.append(avg_validation_cost)

    if graph_display:
      x_train_vals = list(range(1, num_epoches+1))
      plt.plot(x_train_vals, train_cost_list, label = "train curve")
      if validation_examples is not None:
        plt.plot(x_train_vals, validation_cost_list, label = "validation curve")
      plt.xlabel('num-epoches')
      plt.ylabel('train/val-curves')
      plt.show()


  def predict(self, input_vector):
    return self._fw_pass(input_vector)



# examples = [
#   [2,4],
#   [4,6],
#   [1,3],
#   [6,10],
#   [5,7],
#   [9,11],
#   [15,21],
#   [22,30],
#   [12,24],
#   [7,13],
#   [16,18],
#   [16,17],
#   [20,21],
#   [30,32],
#   [35,39]
# ]

# labels = [
#   [1, 0],
#   [1, 0],
#   [0, 1],
#   [1, 0],
#   [0, 1],
#   [0, 1],
#   [0, 1],
#   [1, 0],
#   [1, 0],
#   [0, 1],
#   [1, 0],
#   [0, 1],
#   [0, 1],
#   [1, 0],
#   [0, 1],
# ]

# validation_examples = [
#   [6,8],
#   [3,4],
#   [11,19],
#   [1,1],
#   [2,4]
# ]

# validation_labels = [
#   [1, 0],
#   [0, 1],
#   [0, 1],
#   [0, 1],
#   [1, 0]
# ]
n = SimpleNeuralNet(input_dim=2, num_activation_units=2, output_dim=2)
# n.train(examples, labels, validation_examples, validation_labels, num_epoches=10, graph_display=True)
# prediction = n.predict(np.array(validation_examples[0]).reshape(2, 1))
# print(prediction)



linear_input_examples = [
  [0, 1],
  [1, 2],
  [2, 1],
  [2, 2]
]

linear_input_labels = [
  [1, 0],
  [1, 0],
  [0, 1],
  [0, 1]
]

n = SimpleNeuralNet(input_dim=2, num_activation_units=4, output_dim=2)
n.train(linear_input_examples, linear_input_labels, num_epoches=100, graph_display=False)
print(n.predict([3, 3]))
print(n.predict([1.5, 3]))
print(n.predict([1.5, 1.5]))

# TODO: why is it predicting 50/50? (double-check the fw/bw-pass); test data on pytorch?


# pred_values = n._fw_pass(np.array(examples[0]).reshape(2, 1))
# print(pred_values)
# cost = n._cost_function(pred_values, np.array(labels[0]).reshape(2, 1))
# print(n.output_layer_weights, n.hidden_layer_weights)
# n._bw_pass(np.array(examples[0]).reshape(2, 1), pred_values, np.array(labels[0]).reshape(2, 1))
# print(n.output_layer_weights, n.hidden_layer_weights)
# n.train(examples, labels, num_epoches=10)

# input_vector = np.asarray([2,4])
# n = SimpleNeuralNet(input_dim=2, num_activation_units=4, output_dim=2)
# input_vector = input_vector.reshape(2, 1)
# actual_values = np.asarray([1,0])
# softmax_values = n.fw_pass(input_vector)
# print('predictions: {} / actual: {}'.format(softmax_values, actual_values,))
# print(n.cost_function(softmax_values, actual_values))
# n.bw_pass(input_vector, softmax_values, actual_values)




