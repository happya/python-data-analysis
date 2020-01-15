
from hrdata import *

# line
df = hrDataSEt()
sns.set_style(style="darkgrid")
sns.set_context(context="poster", font_scale=1.2)
sns.set_palette(sns.color_palette("RdBu", n_colors=7))


f = plt.figure()
# method 1
# sub_df = df.groupby("time_spend_company").mean()
# sns.pointplot(sub_df.index, sub_df["left"])
sns.pointplot(x="time_spend_company", y = "left", data=df)
plt.show()