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
                page_size=50,
                style_as_list_view=True,
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
    table_UNIPROT = dash_table.DataTable(
                id=ids.TABLE_ANNOTATION_UNIPROT,
                columns=[{"name": i, "id": i} for i in columns],
                data=[], 
                page_size=50,
                style_as_list_view=True,
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
    table_SRBH = dash_table.DataTable(
                id=ids.TABLE_ANNOTATION_SRBH,
                columns=[{"name": i, "id": i} for i in columns],
                data=[], 
                page_size=50,
                style_as_list_view=True,
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