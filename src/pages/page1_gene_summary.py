from dash import Dash, html
import dash_bootstrap_components as dbc


# importing components
from  ..components import input_geneID_text
from ..components import gene_summary_annotation





def page1_gene_summary_layout(app: Dash):
    
    return html.Div(children = [
        html.Div(style={'marginBottom': '20px'}),
        input_geneID_text.render(app), 
        gene_summary_annotation.render(app)
        ]
    )
            
    
