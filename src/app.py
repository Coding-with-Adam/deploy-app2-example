# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from pathlib import Path

csv_path = Path(__file__).parent.parent/'data'/'shades.csv'
df = pd.read_csv(csv_path)

# Initialize the app
app = Dash(__name__)
server = app.server

# App layout
app.layout = html.Div([
    dcc.Dropdown(options=sorted(df.brand.unique()), value="Revlon", clearable=False, id='brand-dropdown'),
    dcc.Graph(id='scatter-graph')
])

# Add controls to build the interaction
@callback(
    Output(component_id='scatter-graph', component_property='figure'),
    Input(component_id='brand-dropdown', component_property='value')
)
def update_graph(brand_chosen):
    dff = df[df.brand==brand_chosen]
    fig = px.scatter(dff, x='H', y='L')
    return fig


# Run the app
if __name__ == '__main__':
   app.run(debug=True)

