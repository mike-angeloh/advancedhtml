import numpy as np

np.random.seed(42)  # for reproducibility
sales = np.cumsum(np.random.randint(50, 150, 12))  # Cumulative sum to show increasing trend

# Introduce anomalies
sales[3] += 300  # A spike in April
sales[7] -= 250  # A dip in August

import plotly.graph_objects as go

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig = go.Figure()
fig.add_trace(go.Scatter(x=months, y=sales, mode='lines+markers', name='Monthly Sales'))

fig.update_layout(
    title="Fictional Company's Monthly Sales",
    xaxis_title="Month",
    yaxis_title="Sales ($)",
    hovermode="x"
)

fig.show()

import plotly.io as pio

# Export the figure to an HTML file
pio.write_html(fig, file='output_plot.html', auto_open=True)