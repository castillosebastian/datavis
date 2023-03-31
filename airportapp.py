import plotly.graph_objects as go # or plotly.express as px
import polars as pl
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc


# data
codepl=pl.read_csv('airport_code.csv')
frepl=pl.read_csv('airport_frequencies.csv')
result = codepl.join(frepl, on='ident')
result_us = result.filter(pl.col('iso_country') == 'US')
    
# map
fig = px.scatter_mapbox(result.to_pandas(), lat="latitude_deg", lon="longitude_deg", hover_name="municipality", 
                        hover_data=["municipality", "name", "type"],
                        color="type",
                        zoom=3, height=1000)
fig.update_layout(mapbox_style="open-street-map")

fig.update_layout(margin={"r":20,"t":20,"l":20,"b":20})


fig = go.Figure(fig) # or any Plotly Express function e.g. px.bar(...)

# fig.add_trace( ... )
# fig.update_layout( ... )

app = dash.Dash(
__name__, external_stylesheets=[dbc.themes.DARKLY],
)

    
app.layout = html.Div([
    html.Div(
            [
                html.Div(
                    [                        
                        dcc.Markdown(
                            """
                            #   Aeropuertos en el mundo
                            """.replace(
                                            "  ", ""
                                        ),
                                        className="title",
                        ),                        
                    ]
                ),
            ]
        ),
    dcc.Graph(figure=fig),
    ])

app.run_server(debug=True)  # Turn off reloader if inside Jupyter