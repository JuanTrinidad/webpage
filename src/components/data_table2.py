from dash import Dash, dash_table, Input, Output, callback, html
from . import ids
from ..data.loader import DataSchema
from ..data.loader2 import DataSchema2
import pandas as pd



def render(app:Dash, data: pd.DataFrame, data2: pd.DataFrame ) -> html.Div:
    
    #generando la tabla en formato dash
    table = dash_table.DataTable(
                id=ids.TABLE2,
                columns=[{"name": i, "id": i} for i in data2.columns],
                data=data2.to_dict('records'), 
                page_size=50,
                style_data_conditional=[
            {
                'if': {'column_id': i},
                'textOverflow': 'ellipsis',
                'maxWidth': '150px',
            } for i in data2.columns
        ])
    
    # Cada vez que se modifique el valor del input (textbox), se actualiza la tabla.
    @app.callback(
        Output(ids.TABLE2, 'data'),
        Input(ids.TEXT_INPUT1, 'value')
    )
    
    # funcion que corre cuando se modifica el input, actualizando la tabla
    def update_table(value):
        # filtro por geneID y me quedo con la estructura representante
        clusterID = data[data[DataSchema.GENEID] == value][DataSchema.CLUSTERESTRUCTURE].unique()

        #filtro el df para  ver el cluster completo
        filtered_data = data2[data2[DataSchema2.CRS_QUERY].isin(clusterID)]
        #lo ordeno para presentar.
        filtered_data = filtered_data.sort_values(by=DataSchema2.SPP)
        
        return filtered_data.to_dict('records')
    

    #devuelve header y tabla modificada
    return html.Div(
            className="table-container2",
            children=[
                html.H4('Structural Reciprocal Best Hit results:'),
                table
            ]
    )