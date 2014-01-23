import time

_tick_times = []

def tic():
  _tick_times.append(time.time())
  return len(_tick_times) - 1

def toc(key = -1):
  dt = time.time()
  dt -= _tick_times[key]
  del _tick_times[key]
  print("elapsed time ", dt)
  return dt

class timeit(object):
  '''Simple function timing tool.

  Replaces the return value of the decorated function with a
  measure of how long it took to run.  There are two arguments:

  - num_runs 
  - metric

  The metric can be 'average', 'best', 'worst', or 'median'.

  '''
  def __init__(self, func, num_runs = 1, metric = 'average'):
    self.func = func
    self.num_runs = num_runs
    self.metric = metric

  def eval_times(self, times):
    import numpy as np
    import ctypes as ct
    t = np.asarray(times, dtype=ct.c_float)
    if self.metric == 'average':
      return t.mean()
    elif self.metric == 'best':
      return t.min()
    elif self.metric == 'worst':
      return t.max()
    elif self.metric == 'median':
      return np.median(t)

  def __call__(self, *args):
    times = []
    for x in xrange(self.num_runs):
      t0 = time.time()
      self.func(*args)
      times.append(time.time() - t0)
    return self.eval_times(times)

