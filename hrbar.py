
from hrdata import *

# bar
df = hrDataSEt()
sns.set_style(style="darkgrid")
sns.set_context(context="poster", font_scale=1.2)
sns.set_palette(sns.color_palette("RdBu", n_colors=7))
sns.countplot(x="department",hue="salary", data=df)

# # add title
# plt.title("salary")
# # add label
# plt.xlabel("salary")
# plt.ylabel("number")
# # add ticks
# plt.xticks(np.arange(len(df["salary"].value_counts()))+ 0.5, df["salary"].value_counts().index)
# # axis limits
# plt.axis([0, 4, 0, 10000])
# # plot bar graph
# plt.bar(np.arange(len(df["salary"].value_counts()))+0.5, df["salary"].value_counts(), width=0.5)
# # annotate
# for x, y in zip(np.arange(len(df["salary"].value_counts()))+0.5, df["salary"].value_counts()):
#   plt.text(x, y, y, ha="center", va="bottom")
plt.show()