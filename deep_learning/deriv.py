import matplotlib.pyplot as plt
  

class CustomFunction(object):
  """
  One variable function with constant and exponent
  """

  def __init__(self, c=1, exponent=1) -> None:
    self.c = c
    self.exponent = exponent
  
  def calc_y_val(self, x):
    return self.c * (x ** self.exponent)

  def calc_slope(self, x1, x2):
    y2 = self.calc_y_val(x2)
    y1 = self.calc_y_val(x1)
    return (y2-y1) / (x2-x1)

  def calculate_derv_at_point(self, p):
    new_exponent = self.exponent - 1
    new_constant_val = self.exponent * self.c
    if new_exponent == 0:
      return new_constant_val
    else:
      return new_constant_val * (p ** new_exponent)    

  def plot_func(self, n):
    x_vals = list(range(0,n))
    y_vals = [self.c * (i ** self.exponent) for i in range(0,n)]
    plt.plot(x_vals, y_vals, label = "function")
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.show()

# fn = CustomFunction(c=5, exponent=1)
# print(fn.calc_y_val(x=5))
# print(fn.calc_slope(35, 34))
# print(fn.calculate_derv_at_point(p=10))

# non_linear_fn = CustomFunction(c=2, exponent=2)
# print(non_linear_fn.calc_y_val(x=3))
# print(non_linear_fn.calc_slope(4,3))
# print(non_linear_fn.calculate_derv_at_point(3))
# non_linear_fn.plot_func(n=20)


