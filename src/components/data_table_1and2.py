from dash import Dash, dash_table, html
import dash_bootstrap_components as dbc

import pandas as pd

from . import ids


#dbc.Table


def render(app:Dash, TABLE1_cols: list[str], TABLE2_cols: list[str] ) -> html.Div:

    
    #generando la tabla en formato dash
    table0 = dash_table.DataTable(
                id=ids.TABLE1,
                columns=[{"name": i, "id": i} for i in TABLE1_cols],
                data=[], 
                page_size=50,
                style_as_list_view=True,
                sort_action='native',
                style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': '#fdfdfd',
                                }
                            ],
                style_header={
                    'fontSize': '16px',
                    'borderBottom': '2px solid black',
                    },
                style_cell={
                        'minWidth': '0px', 'maxWidth': '300px',
                        'textAlign': 'center',
                        'padding': '5px',
                        'fontSize': '14px',
                        'whiteSpace': 'normal'
                    }

            )
    
    #generando la tabla en formato dash
    table1 = dash_table.DataTable(
                id=ids.TABLE2,
                columns=[{"name": i, "id": i} for i in TABLE2_cols],
                data=[], 
                page_size=50,
                style_as_list_view=True,
                sort_action='native',
                style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': '#fdfdfd',
                                }
                            ],
                style_header={
                    'fontSize': '16px',
                    'borderBottom': '2px solid black',
                    },
                style_cell={
                        'minWidth': '0px', 'maxWidth': '300px',
                        'textAlign': 'center',
                        'padding': '5px',
                        'fontSize': '14px',
                        'whiteSpace': 'normal'
                    }

            )
    
    

    #devuelve header y tabla modificada
    return html.Div(
            children=[
                html.H4('Cluster funtional annotation data (sequence based):'),
                table0,
                html.Div(style={'marginBottom': '100px'}),
                html.H4('Structural Reciprocal Best Hit results:'),
                table1
                
            ]
    )