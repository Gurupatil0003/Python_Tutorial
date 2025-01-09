```python
import plotly.graph_objects as go

# Data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Create line plot
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

# Customize layout
fig.update_layout(title='Basic Line Plot',
                  xaxis_title='X-axis',
                  yaxis_title='Y-axis')

# Show the plot
fig.show()


```

