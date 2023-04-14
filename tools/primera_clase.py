import plotly.graph_objs as go
import numpy as np
import pandas as pd

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Plotly trace object
trace = go.Scatter(x=x, y=y)

# Create the layout object
layout = go.Layout(title='Sin Wave')

# Create the Figure object
fig = go.Figure(data=[trace], layout=layout)

# Show the plot
fig.show()

# Numpy

