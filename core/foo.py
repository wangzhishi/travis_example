import numpy as np
import pandas as pd

def foo(a, b):
  return( [x/y for (x, y) in zip(a, b)] )