from dash import Dash, html, dcc
import pandas as pd
from . import ids
from ..data.loader import DataSchema



def render(app:Dash, data: pd.DataFrame) -> html.Div:
    
    all_geneIDs = list(data['Gene ID'].unique())#.str[:4].unique())
    #all_geneIDs.append('Tb927.10.13280')
    return html.Div(
        children=[
            html.H4("Gene ID"),
            html.P("(first 4 characters displeyed as reference)"),
            dcc.Dropdown(
                id=ids.GENEID_DROPDOWN,
                options=[{"label": geneID, "value": geneID} for geneID in all_geneIDs],
                value='Tb927.10.13280',
                searchable=False
                
            )
            
            ]
    )