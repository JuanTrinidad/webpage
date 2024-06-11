from dash import Dash, html
from . import input_geneID_text
from . import data_table1
from . import data_table2
import pandas as pd



def create_layout(app: Dash, data: pd.DataFrame, data2: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            input_geneID_text.render(app),
            html.Hr(),
            data_table1.render(app, data),
            html.Hr(),
            html.Hr(),
            data_table2.render(app, data, data2),
            ],
    )
    


'''
            html.Div(
                className="textbox",
                children=[ input_geneID_text.render(app) ]   
            ),

'''