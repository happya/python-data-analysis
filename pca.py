import numpy as np
import pandas as pd

def myPCA(data, n_components = 100000):
  # data: each row is a dim
  # each column is a piece of data
  mean_vals = np.mean(data, axis=0) # axis = 0, get mean with respect to column
  mid = data - mean_vals
  cov_mat = np.cov(data, rowvar=False) # only get covariance for columns
  from scipy import linalg
  eig_vals, eig_vects = linalg.eig(np.mat(cov_mat))
  eig_val_index = np.argsort(eig_vals) # argsort to get the index of the sorted eigen value
  eig_val_index = eig_val_index[:-(n_components + 1) : -1]
  eig_vects = eig_vects[:, eig_val_index]
  low_dim_mat = np.dot(mid, eig_vects)
  return low_dim_mat, eig_vals

data = np.array([np.array([2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1]),\
  np.array([2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9])]).T
print(myPCA(data, n_components=1))
