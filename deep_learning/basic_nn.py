import numpy as np
from scipy.special import softmax


class SimpleNeuralNet(object):
  """
  Basic 1-layer NN 
  """
  
  def __init__(self, input_dim, num_activation_units, output_dim, learning_rate=0.1) -> None:
    self.input_dim = input_dim
    self.num_activation_units = num_activation_units
    self.output_dim = output_dim
    self.hidden_layer_weights = np.random.normal(size=(self.input_dim, self.num_activation_units))
    self.output_layer_weights = np.random.normal(size=(self.num_activation_units, self.output_dim))
    self.learning_rate = learning_rate
    self.activation_layer_values = []

  def softmax_function(self, x):
    return softmax(x, axis=0)
    # return np.exp(x)/np.sum(np.exp(x))

  def _fw_pass(self, input_vector):
    hidden_layer_z_val = np.transpose(self.hidden_layer_weights).dot(input_vector)
    relu_fc = lambda t: np.maximum(t, 0)  # relu
    hidden_layer_activation_units = relu_fc(hidden_layer_z_val)
    final_layer_z_val = np.transpose(self.output_layer_weights).dot(hidden_layer_activation_units)
    softmax_values = self.softmax_function(final_layer_z_val)
    self.activation_layer_values.append(hidden_layer_activation_units)
    self.activation_layer_values.append(softmax_values)
    return softmax_values
    # assert len(input_vector) == self.input_dim
    # activation_units = np.multiply(np.transpose(input_vector), np.transpose(self.hidden_layer_weights))     
    # # activation_units = np.transpose(input_vector).dot(np.transpose(self.hidden_layer_weights))
    # relu_fc = lambda t: np.maximum(t, 0) 
    # final_activation_units = relu_fc(activation_units)
    # final_output = final_activation_units.dot(self.output_layer_weights)
    # softmax_values = self.softmax_function(final_output)
    # self.layer_values.append(final_activation_units)
    # self.layer_values.append(softmax_values)
    # return softmax_values

  def _cost_function(self, pred_values, actual_values):  # cross-entropy loss
    epsilon = 1e-5
    return (-1) * (np.sum(actual_values * np.log(pred_values + epsilon)))

  def _bw_pass(self, input_values, pred_values, actual_values):
    delta_output_layer = pred_values - actual_values
    output_layer_weight_gradient = self.activation_layer_values[0].dot(np.transpose(delta_output_layer))    
    # print(delta_output_layer, delta_output_layer.shape)
    # print(output_layer_weight_gradient, output_layer_weight_gradient.shape)
    delta_hidden_layer = self.activation_layer_values[0] * (self.output_layer_weights.dot(delta_output_layer))
    hidden_layer_weight_gradient = input_values.dot(np.transpose(delta_hidden_layer))
    # print(hidden_layer_weight_gradient.shape)
    # print(self.output_layer_weights, (self.learning_rate * output_layer_weight_gradient))
    self.output_layer_weights = self.output_layer_weights - (self.learning_rate * output_layer_weight_gradient)
    self.hidden_layer_weights = self.hidden_layer_weights - (self.learning_rate * hidden_layer_weight_gradient)
    # print(self.output_layer_weights, self.hidden_layer_weights)
    # output_layer_weight_gradient = self.layer_values[0] * np.transpose(delta_final_layer)
    # self.output_layer_weights = self.output_layer_weights - np.transpose((self.learning_rate * output_layer_weight_gradient))
    # # print(self.hidden_layer_weights, delta_final_layer)
    # delta_tmp = self.hidden_layer_weights.dot(np.transpose(delta_final_layer))
    # delta_first_layer = np.multiply(self.layer_values[0], delta_tmp)
    # print(delta_first_layer)
    # print(self.output_layer_weights)
    # print(self.output_layer_weights.shape, delta_final_layer.shape)
    # delta_second_layer = np.dot(self.layer_values[0], (self.output_layer_weights * np.transpose(delta_final_layer)))
    # print(delta_second_layer)
    # first_layer_weight_gradient = input_values * np.transpose(delta_second_layer)

  def train(self, examples, labels, num_epoches=10):
    """
    assuming one-hot encoding of the label
    """
    assert len(examples) == len(labels)
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

      print('Average Cost for Epoch:', (epoch_cost/len(examples)))

  def predict(self, input_vector):
    return self._fw_pass(input_vector)



examples = [
  [2,4],
  [4,6],
  [1,3],
  [6,10],
  [5,7],
  [9,11],
  [15,21],
  [22,30],
  [12,24],
  [7,13],
  [16,18],
  [16,17],
  [20,21],
  [30,32],
  [35,39]
]

labels = [
  [1, 0],
  [1, 0],
  [0, 1],
  [1, 0],
  [0, 1],
  [0, 1],
  [0, 1],
  [1, 0],
  [1, 0],
  [0, 1],
  [1, 0],
  [0, 1],
  [0, 1],
  [1, 0],
  [0, 1],
]

n = SimpleNeuralNet(input_dim=2, num_activation_units=4, output_dim=2)
n.train(examples, labels, num_epoches=10)
ex_val = [6,8]
prediction = n.predict(np.array(ex_val).reshape(2, 1))
print(prediction)

# TODO:
  # fix softmax and cross-entropy error first
  # **test the network <-- what to do about 0.5's? 
    # **after confident, implement in pytorch

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




