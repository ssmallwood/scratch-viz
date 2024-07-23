import plotly.graph_objects as go
import pandas as pd

# Sample data
data = {
    'Year': [2002, 2012, 2022],
    'Ohio Students': [5053, 5478, 5337],
    'Non-Ohio Students': [929, 1737, 2723]
}

df = pd.DataFrame(data)

# Create the plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=df['Year'], y=df['Ohio Students'], name='Ohio Students', mode='lines+markers'))
fig.add_trace(go.Scatter(x=df['Year'], y=df['Non-Ohio Students'], name='Non-Ohio Students', mode='lines+markers'))

fig.update_layout(
    title='Ohio State University Student Demographics',
    xaxis_title='Year',
    yaxis_title='Number of Students',
    legend_title='Student Origin'
)

# Save the plot as an HTML file
fig.write_html("osu_demographics.html", full_html=False, include_plotlyjs='cdn')