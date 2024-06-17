
from dash import Dash, html, dcc
from dash_bootstrap_components.themes  import BOOTSTRAP
from dash.dependencies import Input, Output

#import pages
from src.pages.page1_gene_summary import page1_gene_summary_layout
from src.pages.page2_data_tables import page2_data_tables_layout


#import loaders
from src.data.loader import load_annotation_data, DataSchema
from src.data.loader2 import load_annotation_data2, DataSchema2

#import components
from src.components import navigation_bar
from src.components import ids








def main() -> None:
    
    #file paths
    DATA_PATH = "./data/tables/webpage_Table1.tsv"
    DATA_PATH2 = "./data/tables/webpage_Table2.tsv"

    #load dataframes    
    data = load_annotation_data(DATA_PATH)
    data2 = load_annotation_data2(DATA_PATH2)
    


    ###########################
    # Initialize the Dash app #
    ###########################
    app = Dash(__name__,  suppress_callback_exceptions=True, external_stylesheets=[BOOTSTRAP]) #suppress_callback_exceptions=True,

    app.title = 'Kinetoplastid Structural Annotation Database'

    # define the layout of the app
    content = page1_gene_summary_layout(app, DataSchema.COLUMNS_TRITRYP, DataSchema.COLUMNS_UNIPROT, DataSchema2.COLUMNS_SRBH)

    app.layout =  html.Div([
                        dcc.Location(id='url', refresh=False),
                        navigation_bar.render(app),
                        html.Div(id='page-content', children=[content])
                        ])


    # Callback to dynamically change the page content based on URL
    @app.callback(Output('page-content', 'children'),
                Input('url', 'pathname')
                )

    def display_page(pathname):

        if pathname == '/home':
            return page1_gene_summary_layout(app, DataSchema.COLUMNS_TRITRYP, DataSchema.COLUMNS_UNIPROT, DataSchema2.COLUMNS_SRBH)
        
        elif pathname == '/dashboard':
            return page2_data_tables_layout(app, DataSchema.COLUMNS_TABLE1, DataSchema2.COLUMNS_TABLE2)
        
        else:
            # Returning a 404 page if path is not found
            return '404 - Page not found'







    ######################################################################################
    ############################ Dashboard Callback Functions ############################
    ######################################################################################

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

        return filtered_data[DataSchema.COLUMNS_TABLE1].to_dict('records'), filtered_data2[DataSchema2.COLUMNS_TABLE2].to_dict('records')


    
    
    
    app.run(debug=True)











if __name__ == '__main__':
    main()


