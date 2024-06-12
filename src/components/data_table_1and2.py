from dash import Dash, dash_table, Input, callback, Output, html
import pandas as pd


from . import ids
from ..data.loader import DataSchema
from ..data.loader2 import DataSchema2




def render(app:Dash, data: pd.DataFrame, data2: pd.DataFrame ) -> html.Div:
    
    #generando la tabla en formato dash
    table0 = dash_table.DataTable(
                id=ids.TABLE1,
                columns=[{"name": i, "id": i} for i in data.columns],
                data=[], 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in data.columns
        ])
    
    #generando la tabla en formato dash
    table1 = dash_table.DataTable(
                id=ids.TABLE2,
                columns=[{"name": i, "id": i} for i in data2.columns],
                data=[], 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in data2.columns
        ])
    
    # Cada vez que se modifique el valor del input (textbox), se actualizan las tablas.
    @app.callback(
        [Output(ids.TABLE1, 'data'), 
         Output(ids.TABLE2, 'data')],
        [Input(ids.TEXT_INPUT2, 'value')]
    )
    
    # funcion que corre cuando se modifica el input, actualizando la tabla
    def update_tables(value):

        ######################
        # TABLE 0
        ######################
        # filtro por geneID y me quedo con la estructura representante
        clusterID = data[data[DataSchema.GENEID] == value][DataSchema.CLUSTERESTRUCTURE].unique()
        #filtro el df para  ver el cluster completo
        filtered_data = data[data[DataSchema.CLUSTERESTRUCTURE].isin(clusterID)]
        #lo ordeno para presentar.
        filtered_data = filtered_data.sort_values(by=DataSchema.ORGANISM)
        
        ######################
        # TABLE 1
        ######################
        #filtro el df para  ver el cluster completo
        filtered_data2 = data2[data2[DataSchema2.CRS_QUERY].isin(clusterID)]
        #lo ordeno para presentar.
        filtered_data2 = filtered_data2.sort_values(by=[DataSchema2.FC_TMSCORE1, DataSchema2.FC_TMSCORE2], ascending=False)

        return filtered_data.to_dict('records'), filtered_data2.to_dict('records')
    

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