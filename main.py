# %% [markdown]
# # ***PROJECT C108***

# %%
import pandas
import plotly.figure_factory as ff

data = pandas.read_csv("https://raw.githubusercontent.com/whitehatjr/bell-curve--normal-distribution/master/data.csv")

fig = ff.create_distplot([data["Avg Rating"].tolist()], ["Average Rating"])
fig.show()