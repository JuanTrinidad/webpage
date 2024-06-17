from dash import Dash, dash_table, html
import pandas as pd


from . import ids





def render(app:Dash, TRITRYPS_cols:list[str], UNIPROT_cols:list[str], SRBH_cols: list[str]) -> html.Div:
    
    #generando la tabla en formato dash
    table_TRITRYPS = dash_table.DataTable(
                id=ids.TABLE_ANNOTATION_TRITRYP,
                columns=[{"name": i, "id": i} for i in TRITRYPS_cols],
                data=[], 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in TRITRYPS_cols
        ])
    
    #generando la tabla en formato dash
    table_UNIPROT = dash_table.DataTable(
                id=ids.TABLE_ANNOTATION_UNIPROT,
                columns=[{"name": i, "id": i} for i in UNIPROT_cols],
                data=[], 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in UNIPROT_cols
        ])   

    #generando la tabla en formato dash
    table_SRBH = dash_table.DataTable(
                id=ids.TABLE_ANNOTATION_SRBH,
                columns=[{"name": i, "id": i} for i in SRBH_cols],
                data=[], 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in SRBH_cols
        ])   
    
    
    return html.Div(
            className="table-container2",
            children=[
                html.H4('TritrypDB annotation data:'),
                table_TRITRYPS,
                html.Div(style={'marginBottom': '100px'}),
                html.H4('Uniprot annotation data:'),
                table_UNIPROT,
                html.Div(style={'marginBottom': '100px'}),
                html.H4('Our annotation data:'),
                table_SRBH
            ]
    )