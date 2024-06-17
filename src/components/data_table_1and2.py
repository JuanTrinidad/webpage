from dash import Dash, dash_table, html
import pandas as pd


from . import ids





def render(app:Dash, TABLE1_cols: list[str], TABLE2_cols: list[str] ) -> html.Div:

    
    #generando la tabla en formato dash
    table0 = dash_table.DataTable(
                id=ids.TABLE1,
                columns=[{"name": i, "id": i} for i in TABLE1_cols],
                data=[], 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in TABLE1_cols
        ])
    
    #generando la tabla en formato dash
    table1 = dash_table.DataTable(
                id=ids.TABLE2,
                columns=[{"name": i, "id": i} for i in TABLE2_cols],
                data=[], 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in TABLE2_cols
        ])
    
    

    #devuelve header y tabla modificada
    return html.Div(
            className="table-container2",
            children=[
                html.H4('Cluster funtional annotation data (sequence based):'),
                table0,
                html.Div(style={'marginBottom': '100px'}),
                html.H4('Structural Reciprocal Best Hit results:'),
                table1
                
            ]
    )