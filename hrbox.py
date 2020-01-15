
from hrdata import *

# box
df = hrDataSet()
sns.set_style(style="darkgrid")
sns.set_context(context="poster", font_scale=1.2)
sns.set_palette(sns.color_palette("RdBu", n_colors=7))


f = plt.figure()
# saturation: which quantile
# whis: k
sns.boxplot(y=df["time_spend_company"], saturation=0.75, whis=3)
plt.show()