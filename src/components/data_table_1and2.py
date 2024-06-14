from dash import Dash, dash_table, html
import pandas as pd


from . import ids




#PODRIA PASARLE DIRECTAMENTE DATA.COLUMNS
def render(app:Dash, data_col: list[str], data2_col: list[str] ) -> html.Div:
    
    #generando la tabla en formato dash
    table0 = dash_table.DataTable(
                id=ids.TABLE1,
                columns=[{"name": i, "id": i} for i in data_col],
                data=[], 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in data_col
        ])
    
    #generando la tabla en formato dash
    table1 = dash_table.DataTable(
                id=ids.TABLE2,
                columns=[{"name": i, "id": i} for i in data2_col],
                data=[], 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in data2_col
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