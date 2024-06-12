from dash import Dash, html
import pandas as pd

# importing components
from  ..components import input_geneID_text





def page1_gene_summary_layout(app: Dash) -> html.Div:
    
    return html.Div(
        className="app-div1",
        children=[
            html.Div(style={'marginBottom': '20px'}),
            input_geneID_text.render(app),
            html.Hr(),
            ],
    )
    
