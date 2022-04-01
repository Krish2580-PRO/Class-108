import pandas as pa
import csv
import plotly.figure_factory  as pf

data = pa.read_csv("project.csv")

average = data["Avg Rating"].tolist()

graph = pf.create_distplot(  [average]  , ["Average Graph"]  )

graph.show()