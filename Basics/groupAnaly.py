import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import seaborn as sns
from hrdata import *

df = hrDataSet()

# Gini-coefficient: Gini(D) = 1 - \sum(C_k / D)^2

# hue:分组依据
# sns.barplot(x = "salary", y="left", hue="department",data=df)
# plt.show()

###
#  correlation analysis
###

# 1. correlation
sl_s = df["satisfaction_level"]
# sns.barplot(list(range(len(sl_s))), sl_s.sort_values())
# plt.show()

# sns.heatmap(df.corr(), vmin=-1, vmax=1)
# plt.show()

# 2. entropy
s1 = pd.Series(["X1", "X1", "X2", "X2", "X2", "X2"])
s2 = pd.Series(["Y1", "Y1", "Y1", "Y2", "Y2", "Y2"])
def getEntropy(s):
  if not isinstance(s, pd.core.series.Series):
    s = pd.Series(s)
  prt_ary = pd.groupby(s, by=s).count().values/float(len(s))
  return -(np.log2(prt_ary) * prt_ary).sum()

print("Entropy: ", getEntropy(s1))
print("Entropy: ", getEntropy(s2))

def getCondEntropy(s1, s2):
  '''
  the conditional entropy of s1 on the condition of s2
  '''
  d = dict()
  for i in list(range(len(s1))):
    d[s1[i]] = d.get(s1[i], []) + [s2[i]]
  return sum([getEntropy(d[k]) * len(d[k]) / float(len(s1)) for k in d])

print(getCondEntropy(s1, s2))
print(getCondEntropy(s2, s1))

def getEntropyGain(s1, s2):
  return getEntropy(s2) - getCondEntropy(s1, s2)

print("EntropyGain: ", getEntropyGain(s1, s2))
print("EntropyGain: ", getEntropyGain(s2, s1))

def getEntropyGainRatio(s1, s2):
  return getEntropyGain(s1, s2) / getEntropy(s2)

print("EntropyGainRatio: ", getEntropyGainRatio(s1, s2))
print("EntropyGainRatio: ", getEntropyGainRatio(s2, s1))

import math
def getDiscreteCorr(s1, s2):
  return getEntropyGain(s1, s2)/math.sqrt(getEntropy(s1) * getEntropy(s2))

print("discreteCorr: ", getDiscreteCorr(s1, s2))
print("discreteCorr: ", getDiscreteCorr(s2, s1))

def getProbSS(s):
  if not isinstance(s, pd.core.series.Series):
    s = pd.Series(s)
  prt_ary = pd.groupby(s, by=s).count().values / float(len(s))
  # prt_ary = s.value_counts(normalize=True)
  return sum(prt_ary ** 2)

def getGini(s1, s2):
  d = dict()
  # get the distribution of s2 on the condition of s1
  for i in list(range(len(s1))):
    d[s1[i]] = d.get(s1[i], []) + [s2[i]]
  # print(d)
  return 1 - sum([getProbSS(d[k]) * len(d[k]) / float(len(s1)) for k in d])

print("Gini: ", getGini(s1, s2))
print("Gini: ", getGini(s2, s1))

###
# Factor analysis
###

from sklearn.decomposition import PCA

my_pca = PCA(n_components=7)

lower_mat = my_pca.fit_transform(df.drop(labels=["salary", "department", "left"], axis=1)) # delete column
print("Ratio: ", my_pca.explained_variance_ratio_)

sns.heatmap(pd.DataFrame(lower_mat).corr(), vmin=-1, vmax=1)
plt.show()