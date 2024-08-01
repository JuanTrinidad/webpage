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
                    # Red if neither of the above conditions is met
                    {
                        'if': {
                            'filter_query': '({FC TM-score Chain1} <= 0.4 || {FC TM-score Chain2} <= 0.4)',
                        },
                        'backgroundColor': '#dd9090',
                        'color': 'black',
                    },
                    # Yellow for both 'FC TM-score Chain1' and 'FC TM-score Chain2' > 0.4, if not green
                    {
                        'if': {
                            'filter_query': '{FC TM-score Chain1} > 0.4 && {FC TM-score Chain2} > 0.4',
                        },
                        'backgroundColor': '#ffe084',
                        'color': 'black',
                    },
                    # Green for both 'FC TM-score Chain1' and 'FC TM-score Chain2' > 0.5
                    {
                        'if': {
                            'filter_query': '{FC TM-score Chain1} >= 0.5 && {FC TM-score Chain2} >= 0.5',
                        },
                        'backgroundColor': '#93c47d',
                        'color': 'black',
                    },
                    # White for rows where 'FC TM-score Chain1' or 'FC TM-score Chain2' is missing
                    {
                        'if': {
                            'filter_query': '{FC TM-score Chain1} is blank || {FC TM-score Chain2} is blank',
                        },
                        'backgroundColor': 'white',
                        'color': 'black',
                    },
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