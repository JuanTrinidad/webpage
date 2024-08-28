from dash import Dash, dcc, html
from . import ids


def render(app:Dash):
    
    return dcc.Dropdown(
                    id = ids.DROP_DOWN_PDB,
                    options=[],
                    #value='',
                    className="mt-1",
                    style={'width': '50%'}
                )