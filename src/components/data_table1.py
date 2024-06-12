from dash import Dash, dash_table, Input, Output, html
from . import ids
from ..data.loader import DataSchema
import pandas as pd



def render(app:Dash, data: pd.DataFrame ) -> html.Div:
    
    #generando la tabla en formato dash
    table = dash_table.DataTable(
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
    
    # Cada vez que se modifique el valor del input (textbox), se actualiza la tabla.
    @app.callback(
        Output(ids.TABLE1, 'data'),
        Input(ids.TEXT_INPUT1, 'value')
    )
    
    # funcion que corre cuando se modifica el input, actualizando la tabla
    def update_table(value: str):
        # filtro por geneID y me quedo con la estructura representante
        clusterID = data[data[DataSchema.GENEID] == value][DataSchema.CLUSTERESTRUCTURE].unique()
        #filtro el df para  ver el cluster completo
        filtered_data = data[data[DataSchema.CLUSTERESTRUCTURE].isin(clusterID)]
        #lo ordeno para presentar.
        filtered_data = filtered_data.sort_values(by=DataSchema.ORGANISM)
        
        return filtered_data.to_dict('records')
    

    #devuelve header y tabla modificada
    return html.Div(
            className="table-container",
            children=[
                html.H4('Cluster funtional annotation data (sequence based):'),
                table
            ]
    )