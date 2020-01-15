import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def hrDataSEt():
  df = pd.read_csv("./data/HR.csv")
  df = df.dropna(axis=0, how="any")
  df = df[df["last_evaluation"]<=1][df["salary"] != "nme"][df["department"]!= "sale"]
  return df