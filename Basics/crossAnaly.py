import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import seaborn as sns
from hrdata import *

df = hrDataSet()

# left rate between departments
dp_indices = df.groupby(by="department").indices
# get left
sales_values = df["left"].iloc[dp_indices["sales"]].values
technical_values = df["left"].iloc[dp_indices["technical"]].values
# T-test pvalue
print(ss.ttest_ind(sales_values, technical_values)[1])
dp_keys = list(dp_indices.keys()) # get each department
dp_t_mat = np.zeros([len(dp_keys), len(dp_keys)])
for i in range(len(dp_keys)):
  for j in range(len(dp_indices)):
    p_value = ss.ttest_ind(df["left"].iloc[dp_indices[dp_keys[i]]].values, \
      df["left"].iloc[dp_indices[dp_keys[j]]].values)[1]
    if p_value < 0.05:
      dp_t_mat[i][j] = -1
    else:
      dp_t_mat[i][j] = p_value

sns.heatmap(dp_t_mat, xticklabels=dp_keys, yticklabels=dp_keys)
# plt.show()

# pivot table
piv_tb = pd.pivot_table(df, values="left", index=["promotion_last_5years", "salary"],\
                        columns=["Work_accident"], aggfunc=np.mean)
print(piv_tb)
sns.heatmap(piv_tb, vmin=0, vmax=1)
# plt.show()