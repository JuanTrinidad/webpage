from dash import Dash, html
import pandas as pd

# importing components
from  ..components import input_geneID_text2
from ..components import data_table_1and2






def page2_data_tables_layout(app: Dash, TABLE1_cols: list[str], TABLE2_cols: list[str]) -> html.Div:
    return html.Div(
        className="app-div2",
        children=[
            html.Div(style={'marginBottom': '20px'}),
            input_geneID_text2.render(app),
            html.Hr(),
            data_table_1and2.render(app, TABLE1_cols, TABLE2_cols),
            ],
    )
    

