
from hrdata import *

# histogram
df = hrDataSet()
sns.set_style(style="darkgrid")
sns.set_context(context="poster", font_scale=1.2)
sns.set_palette(sns.color_palette("RdBu", n_colors=7))


f = plt.figure()
f.add_subplot(1, 3, 1)
# kde: true/false, display lines or not
# hist: true/false, display histogram or not
sns.distplot(df["satisfaction_level"], bins = 10)

f.add_subplot(1, 3, 2)
sns.distplot(df["last_evaluation"], bins=10)

f.add_subplot(1, 3, 3)
sns.distplot(df["average_monthly_hours"], bins=10)
plt.show()