from dash import Dash, dash_table, html
import pandas as pd


from . import ids





def render(app:Dash) -> html.Div:
    columns = ['DataBase', 'Annotation']
    
    #generando la tabla en formato dash
    table_TRITRYPS = dash_table.DataTable(
                id=ids.TABLE_ANNOTATION_TRITRYP,
                columns=[{"name": i, "id": i} for i in columns],
                data=[], 
                page_size=50
                )
    
    #generando la tabla en formato dash
    table_UNIPROT = dash_table.DataTable(
                id=ids.TABLE_ANNOTATION_UNIPROT,
                columns=[{"name": i, "id": i} for i in columns],
                data=[], 
                page_size=50
                )   

    #generando la tabla en formato dash
    table_SRBH = dash_table.DataTable(
                id=ids.TABLE_ANNOTATION_SRBH,
                columns=[{"name": i, "id": i} for i in columns],
                data=[], 
                page_size=50
                )   
    
    
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