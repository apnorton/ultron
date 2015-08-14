import math

##
# A node class for a ***naive*** Bayesian network.  This doesn't work for
# "multi-layered" networks, but I can modify that in the future...  I've laid
# *some* of the groundwork, but not all of it.
##
class Node:
  def __init__(self, parents, distro, var_name):
    self.parents = parents # list
    self.distro = distro # either Discrete_Distro or Continuous_Distro
    self.var_name = var_name # variable with which this variable is concerned

  # `vars` is a dictionary mapping variable names to values
  def __call__(self, values):
    if not parents:
      return distro(values[self.var_name])
    else:
      #TODO figure out the math here.
      pass

##
# Callable object that represents a discrete distribution
# Used for discrete variables (duh) in the bayesnet
##
class Discrete_Distro:
  def __init__(self, dictionary):
    self.mapping = dictionary

  def __call__(self, x):
    if (x not in self.mapping):
      return 0
    else:
      return self.mapping[x]

##
# Callable object that represents a normal distribution
# This is used for continuous variables in the bayesnet.
##
class Continuous_Distro:
  def __init__(self, (mean, variance)):
    self.mean = mean
    self.var = variance

  def __call__(self, x):
    result  = math.exp(-(x-self.mean)*(x-self.mean)/(2*self.var))
    result /= math.sqrt(2*self.var*math.pi)
    return result
