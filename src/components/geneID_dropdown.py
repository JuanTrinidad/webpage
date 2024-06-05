from dash import Dash, html, dcc
import pandas as pd
from . import ids
from ..data.loader import DataSchema



def render(app:Dash) -> html.Div:
    
    
    return html.Div(
        children=[
            html.H4("Gene ID"),
            html.H6("(first 4 characters displeyed as reference)")
            dcc.Dropdown(
                id=ids.GENEID_DROPDOWN,
                
                
            )
            
            ]
    )