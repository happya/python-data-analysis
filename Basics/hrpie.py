
from hrdata import *

# pie
df = hrDataSet()
sns.set_style(style="darkgrid")
sns.set_context(context="poster", font_scale=1.2)
sns.set_palette(sns.color_palette("RdBu", n_colors=7))


f = plt.figure()
lbs = df["department"].value_counts().index
# emphasize some part
explodes = [0.1 if i == "sales" else 0 for i in lbs]
plt.pie(df["department"].value_counts(normalize=True), explode=explodes, colors=sns.color_palette("Reds"), labels=lbs, autopct="%1.1f%%")
plt.show()