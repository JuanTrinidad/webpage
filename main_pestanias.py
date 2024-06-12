
from dash import Dash, html, dcc
from dash_bootstrap_components.themes  import BOOTSTRAP
from dash.dependencies import Input, Output

#import pages
from src.pages.page1_gene_summary import page1_gene_summary_layout
from src.pages.page2_data_tables import page2_data_tables_layout


#import loaders
from src.data.loader import load_annotation_data
from src.data.loader2 import load_annotation_data2

#import components
from src.components import navigation_bar


#file paths
DATA_PATH = "./data/tables/webpage_Table1.tsv"
DATA_PATH2 = "./data/tables/webpage_Table2.tsv"

#load dataframes    
data = load_annotation_data(DATA_PATH)
data2 = load_annotation_data2(DATA_PATH2)






def main() -> None:
    
    app = Dash(__name__,  external_stylesheets=[BOOTSTRAP]) #suppress_callback_exceptions=True,

    app.title = 'Kinetoplastid Structural Annotation Database'
    
    content = page1_gene_summary_layout(app)

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
            return page1_gene_summary_layout(app)
        
        elif pathname == '/dashboard':
            return page2_data_tables_layout(app, data, data2)
        else:
            # Returning a 404 page if path is not found
            return '404 - Page not found'


    app.run_server(debug=False)


if __name__ == '__main__':
    main()


